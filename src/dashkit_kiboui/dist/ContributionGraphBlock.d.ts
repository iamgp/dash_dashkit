import React from "react";
export interface ContributionGraphBlockProps {
    /** The ID used to identify this component in Dash callbacks. */
    id?: string;
    /** Activity level (0-4) */
    activity?: number;
    /** Day index in the week (0-6) */
    dayIndex?: number;
    /** Week index in the calendar */
    weekIndex?: number;
    /** Date string in ISO format */
    date?: string;
    /** Count of contributions */
    count?: number;
    /** Block size in pixels */
    size?: number;
    /** Block margin in pixels */
    margin?: number;
    /** Block border radius in pixels */
    radius?: number;
    /** Custom CSS class */
    className?: string;
    /** Custom styling */
    style?: React.CSSProperties;
    /** Click handler */
    onClick?: () => void;
    /** Callback used by Dash to push prop changes from the client */
    setProps?: (props: Partial<ContributionGraphBlockProps>) => void;
}
/**
 * ContributionGraphBlock represents a single day in the contribution calendar.
 */
export default function ContributionGraphBlock({ id, activity, dayIndex, weekIndex, date, count, size, margin, radius, className, style, onClick, setProps }: ContributionGraphBlockProps): import("react/jsx-runtime").JSX.Element;
