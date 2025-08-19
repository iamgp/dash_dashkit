import React from "react";
import type { ContributionDay } from "./lib/types";
export interface ContributionGraphProps {
    /** The ID used to identify this component in Dash callbacks. */
    id?: string;
    /** Array of contribution data with date and count */
    data?: ContributionDay[];
    /** Custom CSS class for the container */
    className?: string;
    /** Custom styling */
    style?: React.CSSProperties;
    /** Children components */
    children?: React.ReactNode;
    /** Callback used by Dash to push prop changes from the client */
    setProps?: (props: Partial<ContributionGraphProps>) => void;
}
/**
 * ContributionGraph is the main container for a GitHub-style contribution graph.
 *
 * This is a composable component that should contain ContributionGraphCalendar
 * and other contribution graph components.
 */
export default function ContributionGraph({ id, data, className, style, children, setProps }: ContributionGraphProps): import("react/jsx-runtime").JSX.Element;
