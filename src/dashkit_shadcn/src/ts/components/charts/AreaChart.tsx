import React from "react"
import {
  Area,
  AreaChart as RechartsAreaChart,
  CartesianGrid,
  XAxis,
  YAxis,
  ResponsiveContainer,
  Tooltip,
  Legend,
} from "recharts"
import { ChartContainer } from "./ChartContainer"
import { ChartTooltip, ChartTooltipContent } from "./ChartTooltip"
import { ChartLegend, ChartLegendContent } from "./ChartLegend"

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
export default function AreaChart({
  id,
  className,
  config = {},
  data = [],
  dataKey = "value",
  xAxisKey = "name",
  yAxisKey,
  showXAxis = true,
  showYAxis = false,
  showGrid = true,
  showTooltip = true,
  showLegend = false,
  stackId,
  fillOpacity = 0.6,
  strokeWidth = 2,
  curve = "monotone",
  style,
  children,
  setProps,
}: AreaChartProps) {
  return (
    <ChartContainer
      id={id}
      className={className}
      config={config as any}
    >
      <ResponsiveContainer width="100%" height="100%">
        <RechartsAreaChart
          data={data}
          margin={{
            left: 12,
            right: 12,
            top: 12,
            bottom: 12,
          }}
        >
          {showGrid && <CartesianGrid vertical={false} />}
          {showXAxis && (
            <XAxis
              dataKey={xAxisKey}
              tickLine={false}
              axisLine={false}
              tickMargin={8}
            />
          )}
          {showYAxis && (
            <YAxis
              dataKey={yAxisKey}
              tickLine={false}
              axisLine={false}
              tickMargin={8}
            />
          )}
          {showTooltip && (
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent />}
            />
          )}
          {showLegend && (
            <ChartLegend
              content={<ChartLegendContent />}
            />
          )}
          <Area
            dataKey={dataKey}
            type={curve as any}
            fill={`var(--color-${dataKey})`}
            fillOpacity={fillOpacity}
            stroke={`var(--color-${dataKey})`}
            strokeWidth={strokeWidth}
            stackId={stackId}
          />
        </RechartsAreaChart>
      </ResponsiveContainer>
    </ChartContainer>
  )
}