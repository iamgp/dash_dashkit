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
  /** Custom tooltip format string. Use {count}, {date}, {dayName}, {monthName}, {year} as placeholders */
  tooltipFormat?: string;
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
export default function ContributionGraphCalendar({
  id,
  data = [],
  monthsToShow = 12,
  blockSize = 12,
  blockMargin = 2,
  blockRadius = 2,
  showMonthLabels = true,
  showWeekdayLabels = true,
  showTooltips = false,
  tooltipFormat,
  className,
  children,
  setProps
}: ContributionGraphCalendarProps) {
  
  // Create a date range for the last N months
  const today = new Date();
  const startDate = new Date(today);
  startDate.setMonth(today.getMonth() - monthsToShow);
  startDate.setDate(1);
  
  // Create a map of dates to contribution counts
  const contributionMap = new Map(
    data.map(d => [d.date, d.count])
  );
  
  // Get the activity level based on contribution count
  const getActivityLevel = (count: number): number => {
    if (count === 0) return 0;
    if (count <= 3) return 1;
    if (count <= 6) return 2;
    if (count <= 9) return 3;
    return 4;
  };
  
  // Generate all weeks and days for the date range
  const weeks: Date[][] = [];
  const currentDate = new Date(startDate);
  
  // Start from the first Sunday before or on the start date
  const firstSunday = new Date(currentDate);
  firstSunday.setDate(currentDate.getDate() - currentDate.getDay());
  currentDate.setTime(firstSunday.getTime());
  
  while (currentDate <= today) {
    const week: Date[] = [];
    for (let i = 0; i < 7; i++) {
      week.push(new Date(currentDate));
      currentDate.setDate(currentDate.getDate() + 1);
    }
    weeks.push(week);
  }
  
  // Month labels
  const monthLabels = weeks.reduce((labels: Array<{month: string, weekIndex: number}>, week, index) => {
    const firstDay = week[0];
    const prevWeek = weeks[index - 1];
    
    if (index === 0 || (prevWeek && firstDay.getMonth() !== prevWeek[0].getMonth())) {
      labels.push({
        month: firstDay.toLocaleDateString('en-US', { month: 'short' }),
        weekIndex: index
      });
    }
    return labels;
  }, []);
  
  const weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
  
  const getTooltipText = (day: Date, count: number): string => {
    if (tooltipFormat) {
      const date = day.toISOString().split('T')[0];
      const dayName = day.toLocaleDateString('en-US', { weekday: 'long' });
      const monthName = day.toLocaleDateString('en-US', { month: 'long' });
      const year = day.getFullYear();
      
      return tooltipFormat
        .replace('{count}', count.toString())
        .replace('{date}', date)
        .replace('{dayName}', dayName)
        .replace('{monthName}', monthName)
        .replace('{year}', year.toString());
    }
    
    const dateStr = day.toLocaleDateString('en-US', { 
      weekday: 'short', 
      month: 'short', 
      day: 'numeric', 
      year: 'numeric' 
    });
    return `${count} contribution${count !== 1 ? 's' : ''} on ${dateStr}`;
  };
  
  const containerStyle: React.CSSProperties = {
    fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
    fontSize: '12px',
    color: '#656d76',
    width: '100%',
    maxWidth: '100%',
    overflowX: 'auto'
  };
  
  const graphStyle: React.CSSProperties = {
    display: 'flex',
    gap: '8px'
  };
  
  const weekdayStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: `${blockMargin}px`,
    paddingTop: showMonthLabels ? '20px' : '0',
    minWidth: '24px'
  };
  
  const calendarStyle: React.CSSProperties = {
    flex: 1,
    minWidth: 'fit-content'
  };
  
  const monthLabelsStyle: React.CSSProperties = {
    position: 'relative',
    height: '16px',
    marginBottom: '4px'
  };
  
  const weeksStyle: React.CSSProperties = {
    display: 'flex',
    gap: `${blockMargin}px`
  };
  
  const weekStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    gap: `${blockMargin}px`
  };

  return (
    <div id={id} className={className} style={containerStyle}>
      <div style={graphStyle}>
        {showWeekdayLabels && (
          <div style={weekdayStyle}>
            {weekdays.map((day, index) => (
              <div
                key={day}
                style={{
                  height: `${blockSize}px`,
                  display: 'flex',
                  alignItems: 'center',
                  fontSize: '9px',
                  lineHeight: 1
                }}
              >
                {index % 2 === 1 ? day : ''}
              </div>
            ))}
          </div>
        )}
        
        <div style={calendarStyle}>
          {showMonthLabels && (
            <div style={monthLabelsStyle}>
              {monthLabels.map(({ month, weekIndex }) => (
                <div
                  key={`${month}-${weekIndex}`}
                  style={{
                    position: 'absolute',
                    left: `${weekIndex * (blockSize + blockMargin)}px`,
                    fontSize: '10px',
                    color: '#656d76'
                  }}
                >
                  {month}
                </div>
              ))}
            </div>
          )}
          
          <div style={weeksStyle}>
            {weeks.map((week, weekIndex) => (
              <div key={weekIndex} style={weekStyle}>
                {week.map((day, dayIndex) => {
                  const dateStr = day.toISOString().split('T')[0];
                  const count = contributionMap.get(dateStr) || 0;
                  const activity = getActivityLevel(count);
                  
                  if (typeof children === 'function') {
                    return (
                      <div key={`${weekIndex}-${dayIndex}`}>
                        {children({ activity, dayIndex, weekIndex, date: dateStr, count })}
                      </div>
                    );
                  }
                  
                  return (
                    <div
                      key={`${weekIndex}-${dayIndex}`}
                      style={{
                        width: `${blockSize}px`,
                        height: `${blockSize}px`,
                        borderRadius: `${blockRadius}px`,
                        backgroundColor: getActivityLevel(count) === 0 ? '#ebedf0' : 
                                        getActivityLevel(count) === 1 ? '#9be9a8' :
                                        getActivityLevel(count) === 2 ? '#40c463' :
                                        getActivityLevel(count) === 3 ? '#30a14e' : '#216e39',
                        cursor: 'pointer'
                      }}
                      data-activity={activity}
                      data-date={dateStr}
                      data-count={count}
                      title={showTooltips ? getTooltipText(day, count) : undefined}
                    />
                  );
                })}
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}