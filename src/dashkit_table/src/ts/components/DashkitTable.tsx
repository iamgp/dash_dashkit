import { HotTable, HotTableClass } from "@handsontable/react";
import Handsontable from "handsontable";
import React, { useRef } from "react";

import { NumericCellType, registerCellType } from "handsontable/cellTypes";

import "handsontable/styles/handsontable.min.css";
import "handsontable/styles/ht-theme-horizon.min.css";
import "handsontable/styles/ht-theme-main.min.css";

registerCellType("numeric", NumericCellType);

console.log("Handsontable version:", Handsontable.version);
(window as any).__HANDSONTABLE_VERSION__ = Handsontable.version;

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

const DashkitTable: React.FC<DashkitTableProps> = ({
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
}) => {
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
        cellProperties.className = `${cellClassName} attio-cell`.trim();
      } else {
        cellProperties.className = "attio-cell";
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
    <div className={`attio-table-container ${className || ""}`.trim()}>
      <HotTable
        key={themeName}
        ref={hotRef}
        {...hotSettings}
        themeName={themeName}
        afterChange={handleAfterChange}
        headerClassName={`${headerClassName || ""} attio-header`.trim()}
      />
    </div>
  );
};

export default DashkitTable;
