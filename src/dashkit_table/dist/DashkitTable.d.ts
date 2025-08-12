import React from "react";
import "handsontable/styles/handsontable.min.css";
import "handsontable/styles/ht-theme-horizon.min.css";
import "handsontable/styles/ht-theme-main.min.css";
export interface DashkitTableProps {
    id?: string;
    data?: any[] | any[][];
    columns?: any[];
    themeName?: string;
    className?: string;
    cellClassName?: string;
    headerClassName?: string;
    height?: number | string;
    width?: number | string;
    rowHeaders?: boolean;
    colHeaders?: boolean;
    licenseKey?: string;
    columnSorting?: boolean;
    multiColumnSorting?: boolean;
    filters?: boolean;
    dropdownMenu?: boolean;
    contextMenu?: boolean;
    rowHeight?: number;
    stretchH?: string;
    settings?: any;
    setProps?: (props: Partial<DashkitTableProps>) => void;
}
declare const DashkitTable: React.FC<DashkitTableProps>;
export default DashkitTable;
