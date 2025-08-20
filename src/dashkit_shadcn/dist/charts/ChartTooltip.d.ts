import React from "react";
interface ChartTooltipProps {
    content?: React.ReactElement | ((props: any) => React.ReactNode);
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
declare const ChartTooltip: ({ content, cursor, ...props }: ChartTooltipProps) => import("react/jsx-runtime").JSX.Element;
declare const ChartTooltipContent: React.ForwardRefExoticComponent<Omit<ChartTooltipContentProps, "ref"> & React.RefAttributes<HTMLDivElement>>;
export { ChartTooltip, ChartTooltipContent };
