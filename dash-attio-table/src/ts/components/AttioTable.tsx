import React, { useEffect, useRef } from 'react';
import { HotTable, HotTableClass } from '@handsontable/react';
import Handsontable from 'handsontable';

// Import Handsontable styles
import 'handsontable/styles/handsontable.min.css';
import 'handsontable/styles/ht-theme-main.min.css';
import 'handsontable/styles/ht-theme-horizon.min.css';

export interface AttioTableProps {
  /**
   * The ID used to identify this component in Dash callbacks
   */
  id?: string;

  /**
   * Data for the table
   */
  data?: any[][];

  /**
   * Column configuration
   */
  columns?: any[];

  /**
   * Theme name - supports Handsontable native themes
   */
  themeName?: 'ht-theme-main' | 'ht-theme-main-dark' | 'ht-theme-horizon' | 'ht-theme-horizon-dark';

  /**
   * Custom CSS class for the table container
   */
  className?: string;

  /**
   * Custom CSS class for table cells
   */
  cellClassName?: string;

  /**
   * Custom CSS class for headers
   */
  headerClassName?: string;

  /**
   * Table height
   */
  height?: number | string;

  /**
   * Table width
   */
  width?: number | string;

  /**
   * Show row headers
   */
  rowHeaders?: boolean;

  /**
   * Show column headers
   */
  colHeaders?: boolean | string[];

  /**
   * License key for Handsontable
   */
  licenseKey?: string;

  /**
   * Enable column sorting
   */
  columnSorting?: boolean;

  /**
   * Enable multi-column sorting
   */
  multiColumnSorting?: boolean;

  /**
   * Enable filters
   */
  filters?: boolean;

  /**
   * Enable dropdown menu
   */
  dropdownMenu?: boolean | string[];

  /**
   * Enable context menu
   */
  contextMenu?: boolean | string[];

  /**
   * Custom row height
   */
  rowHeight?: number;

  /**
   * Stretch columns to fill container
   */
  stretchH?: 'none' | 'last' | 'all';

  /**
   * Any additional Handsontable settings
   */
  settings?: any;

  /**
   * Callback when data changes
   */
  setProps?: (props: Partial<AttioTableProps>) => void;
}

/**
 * AttioTable is a modern Handsontable component for Dash with native theming support.
 * It provides a full-featured data grid with native Handsontable themes and extensive customization options.
 */
const AttioTable: React.FC<AttioTableProps> = ({
  id,
  data = [],
  columns,
  themeName = 'ht-theme-main',
  className = '',
  cellClassName = '',
  headerClassName = '',
  height = 400,
  width = '100%',
  rowHeaders = false,
  colHeaders = true,
  licenseKey = 'non-commercial-and-evaluation',
  columnSorting = true,
  multiColumnSorting = false,
  filters = false,
  dropdownMenu = false,
  contextMenu = false,
  rowHeight = 35,
  stretchH = 'all',
  settings = {},
  setProps
}) => {
  const hotRef = useRef<HotTableClass>(null);

  // Base Handsontable configuration  
  const hotSettings: any = {
    data,
    columns,
    height,
    width,
    rowHeaders,
    colHeaders,
    licenseKey,
    columnSorting,
    multiColumnSorting,
    filters,
    dropdownMenu,
    contextMenu,
    stretchH,
    rowHeights: rowHeight,
    // Apply theme
    themeName,
    // Custom cell renderer for styling
    cells: function(row: number, col: number) {
      const cellProperties: any = {};
      if (cellClassName) {
        cellProperties.className = `${cellClassName} attio-cell`;
      }
      return cellProperties;
    },
    // Override default settings with any custom ones
    ...settings
  };

  // Handle data changes
  const handleAfterChange = (changes: Handsontable.CellChange[] | null) => {
    if (changes && setProps && hotRef.current) {
      const hot = (hotRef.current as any).hotInstance;
      if (hot) {
        setProps({ data: hot.getData() });
      }
    }
  };

  return (
    <div className={`attio-table-container ${themeName} ${className}`}>
      <HotTable
        ref={hotRef}
        {...hotSettings}
        afterChange={handleAfterChange}
        className={`${cellClassName} attio-cell`}
        headerClassName={`${headerClassName} attio-header`}
      />
    </div>
  );
};

export default AttioTable;