import React from "react";
interface ChartLegendProps {
    content?: React.ReactElement | ((props: any) => React.ReactNode);
    [key: string]: any;
}
interface ChartLegendContentProps {
    nameKey?: string;
    payload?: Array<{
        value: string;
        type: string;
        color: string;
        [key: string]: any;
    }>;
    className?: string;
    [key: string]: any;
}
declare const ChartLegend: ({ content, ...props }: ChartLegendProps) => import("react/jsx-runtime").JSX.Element;
declare const ChartLegendContent: React.ForwardRefExoticComponent<Omit<ChartLegendContentProps, "ref"> & React.RefAttributes<HTMLDivElement>>;
export { ChartLegend, ChartLegendContent };
