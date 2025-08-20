import React from "react";
import { ChartConfig } from "../lib/types";
interface ChartContainerProps {
    id?: string;
    className?: string;
    config: ChartConfig;
    children: React.ReactElement;
}
declare const ChartContainer: React.ForwardRefExoticComponent<ChartContainerProps & React.RefAttributes<HTMLDivElement>>;
export { ChartContainer };
