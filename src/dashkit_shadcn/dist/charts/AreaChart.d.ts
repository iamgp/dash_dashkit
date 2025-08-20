import React from "react";
export interface AreaChartProps {
    /** The ID used to identify this component in Dash callbacks. */
    id?: string;
    /** Custom CSS class for the container */
    className?: string;
    /** Chart configuration object with data key mappings and colors */
    config?: object;
    /** Array of data points for the chart */
    data?: object[];
    /** The key in data objects to use for the area values */
    dataKey?: string;
    /** The key in data objects to use for x-axis labels */
    xAxisKey?: string;
    /** The key in data objects to use for y-axis labels */
    yAxisKey?: string;
    /** Whether to show the x-axis */
    showXAxis?: boolean;
    /** Whether to show the y-axis */
    showYAxis?: boolean;
    /** Whether to show the grid */
    showGrid?: boolean;
    /** Whether to show tooltips */
    showTooltip?: boolean;
    /** Whether to show the legend */
    showLegend?: boolean;
    /** Stack ID for stacked areas */
    stackId?: string;
    /** Fill opacity for the area */
    fillOpacity?: number;
    /** Stroke width for the area line */
    strokeWidth?: number;
    /** Curve type for the area */
    curve?: string;
    /** Custom styling */
    style?: React.CSSProperties;
    /** Children components */
    children?: React.ReactNode;
    /** Callback used by Dash to push prop changes from the client */
    setProps?: (props: Partial<AreaChartProps>) => void;
}
/**
 * AreaChart renders an area chart using shadcn/ui styling and Recharts.
 */
export default function AreaChart({ id, className, config, data, dataKey, xAxisKey, yAxisKey, showXAxis, showYAxis, showGrid, showTooltip, showLegend, stackId, fillOpacity, strokeWidth, curve, style, children, setProps, }: AreaChartProps): import("react/jsx-runtime").JSX.Element;
