import React from "react"
import { cn } from "../lib/utils"
import { Tooltip } from "recharts"

interface ChartTooltipProps {
  content?: React.ReactElement | ((props: any) => React.ReactNode)
  cursor?: boolean | object
  [key: string]: any
}

interface ChartTooltipContentProps {
  active?: boolean
  payload?: any[]
  label?: string
  labelKey?: string
  nameKey?: string
  indicator?: "dot" | "line" | "dashed"
  hideLabel?: boolean
  hideIndicator?: boolean
  className?: string
  [key: string]: any
}

const ChartTooltip = ({ content, cursor, ...props }: ChartTooltipProps) => {
  // This is essentially a wrapper for Recharts Tooltip
  // We need to pass through to Recharts' Tooltip component
  return (
    <Tooltip
      cursor={cursor}
      content={content}
      {...props}
    />
  )
}

const ChartTooltipContent = React.forwardRef<
  HTMLDivElement,
  ChartTooltipContentProps
>(
  (
    {
      active,
      payload,
      label,
      labelKey,
      nameKey,
      indicator = "dot",
      hideLabel = false,
      hideIndicator = false,
      className,
      ...props
    },
    ref
  ) => {
    const tooltipLabel = hideLabel ? null : (
      <div className="font-medium">{label}</div>
    )

    if (!active || !payload?.length) {
      return null
    }

    const nestLabel = payload.length === 1 && indicator !== "dot"

    return (
      <div
        ref={ref}
        className={cn(
          "border-border/50 bg-background grid min-w-[8rem] items-start gap-1.5 rounded-lg border px-2.5 py-1.5 text-xs shadow-xl",
          className
        )}
        {...props}
      >
        {!nestLabel ? tooltipLabel : null}
        <div className="grid gap-1.5">
          {payload.map((item: any, index: number) => {
            const key = `${nameKey || item.dataKey || item.name || "value"}`
            const indicatorColor = item.color || item.fill || "var(--color-" + key + ")"

            return (
              <div
                key={`item-${index}`}
                className={cn(
                  "flex w-full items-stretch gap-2 [&>svg]:h-2.5 [&>svg]:w-2.5 [&>svg]:text-muted-foreground",
                  indicator === "dot" && "items-center"
                )}
              >
                {!hideIndicator && (
                  <div
                    className={cn(
                      "shrink-0 rounded-[2px] border-[--color-border] bg-[--color-bg]",
                      {
                        "h-2.5 w-2.5": indicator === "dot",
                        "w-1": indicator === "line",
                        "w-0 border-[1.5px] border-dashed bg-transparent":
                          indicator === "dashed",
                        "my-0.5": nestLabel && indicator === "dashed",
                      }
                    )}
                    style={
                      {
                        "--color-bg": indicatorColor,
                        "--color-border": indicatorColor,
                      } as React.CSSProperties
                    }
                  />
                )}
                <div
                  className={cn(
                    "flex flex-1 justify-between leading-none",
                    nestLabel ? "items-end" : "items-center"
                  )}
                >
                  <div className="grid gap-1.5">
                    {nestLabel ? tooltipLabel : null}
                    <span className="text-muted-foreground">
                      {item.name || item.dataKey}
                    </span>
                  </div>
                  <span className="text-foreground font-mono font-medium tabular-nums">
                    {typeof item.value === "number"
                      ? item.value.toLocaleString()
                      : item.value}
                  </span>
                </div>
              </div>
            )
          })}
        </div>
      </div>
    )
  }
)
ChartTooltipContent.displayName = "ChartTooltipContent"

export { ChartTooltip, ChartTooltipContent }