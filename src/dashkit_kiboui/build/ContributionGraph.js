"use strict";
var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = ContributionGraph;
var jsx_runtime_1 = require("react/jsx-runtime");
var utils_1 = require("./lib/utils");
/**
 * ContributionGraph is a GitHub-style contribution graph component for Dash.
 *
 * Displays activity levels over time in a calendar-style grid format.
 * Supports theming, tooltips, and various customization options.
 */
function ContributionGraph(_a) {
    var id = _a.id, _b = _a.data, data = _b === void 0 ? [] : _b, _c = _a.blockSize, blockSize = _c === void 0 ? 12 : _c, _d = _a.blockMargin, blockMargin = _d === void 0 ? 2 : _d, _e = _a.blockRadius, blockRadius = _e === void 0 ? 2 : _e, className = _a.className, _f = _a.showMonthLabels, showMonthLabels = _f === void 0 ? true : _f, _g = _a.showWeekdayLabels, showWeekdayLabels = _g === void 0 ? true : _g, _h = _a.colorScheme, colorScheme = _h === void 0 ? 'github' : _h, _j = _a.colors, colors = _j === void 0 ? ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'] : _j, _k = _a.showTooltips, showTooltips = _k === void 0 ? false : _k, tooltipContent = _a.tooltipContent, _l = _a.monthsToShow, monthsToShow = _l === void 0 ? 12 : _l, setProps = _a.setProps;
    // Create a date range for the last N months
    var today = new Date();
    var startDate = new Date(today);
    startDate.setMonth(today.getMonth() - monthsToShow);
    startDate.setDate(1); // Start from the first day of the month
    // Create a map of dates to contribution counts
    var contributionMap = new Map(data.map(function (d) { return [d.date, d.count]; }));
    // Get the activity level based on contribution count
    var getActivityLevel = function (count) {
        if (count === 0)
            return 0;
        if (count <= 3)
            return 1;
        if (count <= 6)
            return 2;
        if (count <= 9)
            return 3;
        return 4;
    };
    // Generate all weeks and days for the date range
    var weeks = [];
    var currentDate = new Date(startDate);
    // Start from the first Sunday before or on the start date
    var firstSunday = new Date(currentDate);
    firstSunday.setDate(currentDate.getDate() - currentDate.getDay());
    currentDate.setTime(firstSunday.getTime());
    while (currentDate <= today) {
        var week = [];
        for (var i = 0; i < 7; i++) {
            week.push(new Date(currentDate));
            currentDate.setDate(currentDate.getDate() + 1);
        }
        weeks.push(week);
    }
    // Month labels
    var monthLabels = weeks.reduce(function (labels, week, index) {
        var firstDay = week[0];
        var isFirstWeekOfMonth = firstDay.getDate() <= 7;
        if (isFirstWeekOfMonth || index === 0) {
            labels.push({
                month: firstDay.toLocaleDateString('en-US', { month: 'short' }),
                weekIndex: index
            });
        }
        return labels;
    }, []);
    var weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    var handleBlockClick = function (day, count) {
        if (setProps) {
            var dateStr_1 = day.toISOString().split('T')[0];
            setProps({
                data: data.map(function (d) {
                    return d.date === dateStr_1 ? __assign(__assign({}, d), { count: count }) : d;
                }).concat(data.find(function (d) { return d.date === dateStr_1; }) ? [] : [{ date: dateStr_1, count: count }])
            });
        }
    };
    var getTooltipText = function (day, count) {
        if (tooltipContent) {
            return tooltipContent({ date: day.toISOString().split('T')[0], count: count });
        }
        var dateStr = day.toLocaleDateString('en-US', {
            weekday: 'short',
            month: 'short',
            day: 'numeric',
            year: 'numeric'
        });
        return "".concat(count, " contribution").concat(count !== 1 ? 's' : '', " on ").concat(dateStr);
    };
    var containerStyle = {
        '--block-size': "".concat(blockSize, "px"),
        '--block-margin': "".concat(blockMargin, "px"),
        '--block-radius': "".concat(blockRadius, "px"),
        '--color-level-0': colors[0],
        '--color-level-1': colors[1],
        '--color-level-2': colors[2],
        '--color-level-3': colors[3],
        '--color-level-4': colors[4],
    };
    // CSS styles as objects for proper React rendering
    var baseStyles = {
        contributionGraph: {
            fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif',
            fontSize: '12px',
            color: '#656d76'
        },
        graphContainer: {
            display: 'flex',
            gap: '8px',
            marginTop: '8px'
        },
        weekdayLabels: {
            display: 'flex',
            flexDirection: 'column',
            gap: "".concat(blockMargin, "px"),
            paddingTop: '20px',
            minWidth: '24px'
        },
        weekdayLabel: {
            height: "".concat(blockSize, "px"),
            display: 'flex',
            alignItems: 'center',
            fontSize: '9px',
            lineHeight: 1
        },
        weeksContainer: {
            overflowX: 'auto',
            flex: 1
        },
        monthLabels: {
            display: 'flex',
            height: '16px',
            marginBottom: '4px'
        },
        monthLabel: {
            fontSize: '10px',
            color: '#656d76',
            marginRight: '8px'
        },
        weeks: {
            display: 'flex',
            gap: "".concat(blockMargin, "px")
        },
        week: {
            display: 'flex',
            flexDirection: 'column',
            gap: "".concat(blockMargin, "px")
        }
    };
    var getDayStyle = function (level) {
        var baseStyle = {
            width: "".concat(blockSize, "px"),
            height: "".concat(blockSize, "px"),
            borderRadius: "".concat(blockRadius, "px"),
            cursor: 'pointer',
            transition: 'all 0.1s ease'
        };
        var backgroundColor = colors[level] || '#ebedf0';
        if (colorScheme === 'github') {
            var githubColors = ['#ebedf0', '#9be9a8', '#40c463', '#30a14e', '#216e39'];
            backgroundColor = githubColors[level] || '#ebedf0';
        }
        return __assign(__assign({}, baseStyle), { backgroundColor: backgroundColor });
    };
    return ((0, jsx_runtime_1.jsx)("div", { id: id, className: (0, utils_1.cn)("contribution-graph", className), style: __assign(__assign({}, containerStyle), baseStyles.contributionGraph), "data-color-scheme": colorScheme, children: (0, jsx_runtime_1.jsxs)("div", { style: baseStyles.graphContainer, children: [showWeekdayLabels && ((0, jsx_runtime_1.jsx)("div", { style: baseStyles.weekdayLabels, children: weekdays.map(function (day, index) { return (index % 2 === 1 ? ((0, jsx_runtime_1.jsx)("div", { style: baseStyles.weekdayLabel, children: day }, day)) : ((0, jsx_runtime_1.jsx)("div", { style: baseStyles.weekdayLabel }, day))); }) })), (0, jsx_runtime_1.jsxs)("div", { style: baseStyles.weeksContainer, children: [showMonthLabels && ((0, jsx_runtime_1.jsx)("div", { style: baseStyles.monthLabels, children: monthLabels.map(function (_a) {
                                var month = _a.month, weekIndex = _a.weekIndex;
                                return ((0, jsx_runtime_1.jsx)("div", { style: __assign(__assign({}, baseStyles.monthLabel), { marginLeft: weekIndex === 0 ? 0 : "".concat((weekIndex * (blockSize + blockMargin)) - 32, "px") }), children: month }, "".concat(month, "-").concat(weekIndex)));
                            }) })), (0, jsx_runtime_1.jsx)("div", { style: baseStyles.weeks, children: weeks.map(function (week, weekIndex) { return ((0, jsx_runtime_1.jsx)("div", { style: baseStyles.week, children: week.map(function (day, dayIndex) {
                                    var dateStr = day.toISOString().split('T')[0];
                                    var count = contributionMap.get(dateStr) || 0;
                                    var level = getActivityLevel(count);
                                    return ((0, jsx_runtime_1.jsx)("div", { style: getDayStyle(level), "data-level": level, "data-date": dateStr, "data-count": count, title: showTooltips ? getTooltipText(day, count) : undefined, onClick: function () { return handleBlockClick(day, count); } }, "".concat(weekIndex, "-").concat(dayIndex)));
                                }) }, weekIndex)); }) })] })] }) }));
}
