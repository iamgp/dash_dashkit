import React from "react";
import "handsontable/styles/handsontable.min.css";
import "handsontable/styles/ht-theme-main.min.css";
import "handsontable/styles/ht-theme-horizon.min.css";
export interface AttioTableProps {
    /**
     * The ID used to identify this component in Dash callbacks
     */
    id?: string;
    /**
     * Data for the table. Supports either a 2D array (matrix) or an array of objects.
     */
    data?: any[] | any[][];
    /**
     * Column configuration
     */
    columns?: any[];
    /**
     * Theme name - supports Handsontable native themes
     */
    themeName?: string;
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
    colHeaders?: boolean;
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
    dropdownMenu?: boolean;
    /**
     * Enable context menu
     */
    contextMenu?: boolean;
    /**
     * Custom row height
     */
    rowHeight?: number;
    /**
     * Stretch columns to fill container
     */
    stretchH?: string;
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
declare const AttioTable: React.FC<AttioTableProps>;
export default AttioTable;
