import React from "react";
import { ContributionDay } from "./lib/types";
export interface ContributionGraphCalendarProps {
    /** The ID used to identify this component in Dash callbacks. */
    id?: string;
    /** Array of contribution data */
    data?: ContributionDay[];
    /** Number of months to show */
    monthsToShow?: number;
    /** Block size in pixels */
    blockSize?: number;
    /** Block margin in pixels */
    blockMargin?: number;
    /** Block border radius in pixels */
    blockRadius?: number;
    /** Show month labels */
    showMonthLabels?: boolean;
    /** Show weekday labels */
    showWeekdayLabels?: boolean;
    /** Enable tooltips */
    showTooltips?: boolean;
    /** Custom CSS class */
    className?: string;
    /** Children render function or components */
    children?: React.ReactNode | ((props: {
        activity: number;
        dayIndex: number;
        weekIndex: number;
        date: string;
        count: number;
    }) => React.ReactNode);
    /** Callback used by Dash to push prop changes from the client */
    setProps?: (props: Partial<ContributionGraphCalendarProps>) => void;
}
/**
 * ContributionGraphCalendar renders the calendar grid for contributions.
 */
export default function ContributionGraphCalendar({ id, data, monthsToShow, blockSize, blockMargin, blockRadius, showMonthLabels, showWeekdayLabels, showTooltips, className, children, setProps }: ContributionGraphCalendarProps): import("react/jsx-runtime").JSX.Element;
