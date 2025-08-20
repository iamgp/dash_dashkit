import React from "react";
interface ChartTooltipProps {
    content?: React.ReactNode;
    cursor?: boolean | object;
    [key: string]: any;
}
interface ChartTooltipContentProps {
    active?: boolean;
    payload?: any[];
    label?: string;
    labelKey?: string;
    nameKey?: string;
    indicator?: "dot" | "line" | "dashed";
    hideLabel?: boolean;
    hideIndicator?: boolean;
    className?: string;
    [key: string]: any;
}
declare const ChartTooltip: ({ content, ...props }: ChartTooltipProps) => React.ReactElement<{
    [key: string]: any;
    cursor?: boolean | object;
}, string | React.JSXElementConstructor<any>> | null;
declare const ChartTooltipContent: React.ForwardRefExoticComponent<Omit<ChartTooltipContentProps, "ref"> & React.RefAttributes<HTMLDivElement>>;
export { ChartTooltip, ChartTooltipContent };
