import { HotTable, HotTableClass } from "@handsontable/react";
import Handsontable from "handsontable";
import { useRef } from "react";

import { NumericCellType, registerCellType } from "handsontable/cellTypes";

import "handsontable/styles/handsontable.min.css";
import "handsontable/styles/ht-theme-horizon.min.css";
import "handsontable/styles/ht-theme-main.min.css";

registerCellType("numeric", NumericCellType);

console.log("Handsontable version:", Handsontable.version);
(window as any).__HANDSONTABLE_VERSION__ = Handsontable.version;

export interface DashkitTableProps {
  /** The ID used to identify this component in Dash callbacks. */
  id?: string;
  /**
   * Data for the table. Accepts either:
   * - Array of objects (records) when used with column definitions using `data: <fieldName>`
   * - 2D array (matrix) when used with index-based columns (`data: <columnIndex>`)
   */
  data?: any[] | any[][];
  /** Column configuration passed through to Handsontable. */
  columns?: any[];
  /** Theme name for native Handsontable themes (e.g. `ht-theme-main`, `ht-theme-horizon`). */
  themeName?: string;
  /** Custom CSS class for the outer table container. */
  className?: string;
  /** Custom CSS class applied to all table cells. */
  cellClassName?: string;
  /** Custom CSS class applied to all column/row headers. */
  headerClassName?: string;
  /** Table height in pixels or CSS size. */
  height?: number | string;
  /** Table width in pixels or CSS size. */
  width?: number | string;
  /** Show row headers. */
  rowHeaders?: boolean;
  /** Show column headers. */
  colHeaders?: boolean;
  /** Handsontable license key string. */
  licenseKey?: string;
  /** Enable single-column sorting. */
  columnSorting?: boolean;
  /** Enable multi-column sorting. */
  multiColumnSorting?: boolean;
  /** Enable filter functionality. */
  filters?: boolean;
  /** Enable dropdown menu. */
  dropdownMenu?: boolean;
  /** Enable context menu. */
  contextMenu?: boolean;
  /** Row height in pixels. */
  rowHeight?: number;
  /** Column stretching behaviour. */
  stretchH?: string;
  /** Additional Handsontable settings to merge into the base config. */
  settings?: any;
  /** Callback used by Dash to push prop changes from the client. */
  setProps?: (props: Partial<DashkitTableProps>) => void;
}

/**
 * DashkitTable is a modern Handsontable component for Dash with native theme support.
 *
 * Provides a full-featured data grid with ergonomic defaults and theme-aware styling.
 * Supports both record-style rows and 2D arrays. Pass additional Handsontable options via `settings`.
 */
export default function DashkitTable({
  id,
  data = [],
  columns,
  themeName = "ht-theme-main",
  className = "",
  cellClassName = "",
  headerClassName = "",
  height = 400,
  width = "100%",
  rowHeaders = false,
  colHeaders = true,
  licenseKey = "non-commercial-and-evaluation",
  columnSorting = true,
  multiColumnSorting = false,
  filters = false,
  dropdownMenu = false,
  contextMenu = false,
  rowHeight = 35,
  stretchH = "all",
  settings = {},
  setProps,
}: DashkitTableProps) {
  const hotRef = useRef<HotTableClass>(null);
  console.log("DashkitTable rendered with themeName:", themeName);

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
    cells: function (row: number, col: number) {
      const cellProperties: any = {};
      if (cellClassName) {
        cellProperties.className = `${cellClassName} dashkit-cell`.trim();
      } else {
        cellProperties.className = "dashkit-cell";
      }
      return cellProperties;
    },
    ...settings,
  };

  const handleAfterChange = (changes: Handsontable.CellChange[] | null) => {
    if (changes && setProps && hotRef.current) {
      const hot = (hotRef.current as any).hotInstance;
      if (hot) {
        setProps({ data: hot.getData() });
      }
    }
  };

  return (
    <div className={`dashkit-table-container ${className || ""}`.trim()}>
      <HotTable
        key={themeName}
        ref={hotRef}
        {...hotSettings}
        themeName={themeName}
        afterChange={handleAfterChange}
        headerClassName={`${headerClassName || ""} dashkit-header`.trim()}
      />
    </div>
  );
}
