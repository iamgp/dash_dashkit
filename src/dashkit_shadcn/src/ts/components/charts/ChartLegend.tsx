import React from "react"
import { cn } from "../lib/utils"

interface ChartLegendProps {
  content?: React.ReactNode
  [key: string]: any
}

interface ChartLegendContentProps {
  nameKey?: string
  payload?: Array<{
    value: string
    type: string
    color: string
    [key: string]: any
  }>
  className?: string
  [key: string]: any
}

const ChartLegend = ({ content, ...props }: ChartLegendProps) => {
  return content ? React.createElement("div", props, content) : null
}

const ChartLegendContent = React.forwardRef<
  HTMLDivElement,
  ChartLegendContentProps
>(({ className, payload, nameKey, ...props }, ref) => {
  if (!payload?.length) {
    return null
  }

  return (
    <div
      ref={ref}
      className={cn("flex items-center justify-center gap-4", className)}
      {...props}
    >
      {payload.map((item: any, index: number) => {
        const key = `${nameKey || item.value || "value"}`
        
        return (
          <div
            key={`item-${index}`}
            className="flex items-center gap-1.5 [&>svg]:h-3 [&>svg]:w-3 [&>svg]:text-muted-foreground"
          >
            <div
              className="h-2 w-2 shrink-0 rounded-[2px] border-[--color-border] bg-[--color-bg]"
              style={
                {
                  "--color-bg": item.color,
                  "--color-border": item.color,
                } as React.CSSProperties
              }
            />
            <span className="text-muted-foreground">{item.value}</span>
          </div>
        )
      })}
    </div>
  )
})
ChartLegendContent.displayName = "ChartLegendContent"

export { ChartLegend, ChartLegendContent }