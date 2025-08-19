import React from "react";
import { cn } from "./lib/utils";
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
export default function ContributionGraph({
  id,
  data = [],
  className,
  style,
  children,
  setProps
}: ContributionGraphProps) {
  
  const containerStyle: React.CSSProperties = {
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    fontSize: '12px',
    color: '#656d76',
    width: '100%',
    maxWidth: '100%',
    ...style
  };

  return (
    <div 
      id={id}
      className={cn("contribution-graph", className)} 
      style={containerStyle}
      data-testid="contribution-graph"
    >
      {children}
    </div>
  );
}