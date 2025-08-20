import React from "react";
interface ChartLegendProps {
    content?: React.ReactNode;
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
declare const ChartLegend: ({ content, ...props }: ChartLegendProps) => React.DetailedReactHTMLElement<{
    [key: string]: any;
}, HTMLElement> | null;
declare const ChartLegendContent: React.ForwardRefExoticComponent<Omit<ChartLegendContentProps, "ref"> & React.RefAttributes<HTMLDivElement>>;
export { ChartLegend, ChartLegendContent };
