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
export default function ContributionGraphBlock({
  id,
  activity = 0,
  dayIndex = 0,
  weekIndex = 0,
  date,
  count = 0,
  size = 12,
  margin = 2,
  radius = 2,
  className,
  style,
  onClick,
  setProps
}: ContributionGraphBlockProps) {
  
  const getActivityColor = (level: number) => {
    const colors = ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'];
    return colors[Math.max(0, Math.min(4, level))] || colors[0];
  };

  const blockStyle: React.CSSProperties = {
    width: `${size}px`,
    height: `${size}px`,
    backgroundColor: getActivityColor(activity),
    borderRadius: `${radius}px`,
    cursor: onClick ? 'pointer' : 'default',
    transition: 'all 0.1s ease',
    ...style
  };

  return (
    <div
      id={id}
      className={className}
      style={blockStyle}
      data-activity={activity}
      data-date={date}
      data-count={count}
      data-day-index={dayIndex}
      data-week-index={weekIndex}
      onClick={onClick}
    />
  );
}