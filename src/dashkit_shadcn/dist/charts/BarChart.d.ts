import React from "react";
export interface BarChartProps {
    /** The ID used to identify this component in Dash callbacks. */
    id?: string;
    /** Custom CSS class for the container */
    className?: string;
    /** Chart configuration object with data key mappings and colors */
    config?: object;
    /** Array of data points for the chart */
    data?: object[];
    /** The key in data objects to use for the bar values */
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
    /** Stack ID for stacked bars */
    stackId?: string;
    /** Border radius for the bars */
    radius?: number;
    /** Maximum bar size */
    maxBarSize?: number;
    /** Custom styling */
    style?: React.CSSProperties;
    /** Children components */
    children?: React.ReactNode;
    /** Callback used by Dash to push prop changes from the client */
    setProps?: (props: Partial<BarChartProps>) => void;
}
/**
 * BarChart renders a bar chart using shadcn/ui styling and Recharts.
 */
export default function BarChart({ id, className, config, data, dataKey, xAxisKey, yAxisKey, showXAxis, showYAxis, showGrid, showTooltip, showLegend, stackId, radius, maxBarSize, style, children, setProps, }: BarChartProps): import("react/jsx-runtime").JSX.Element;
