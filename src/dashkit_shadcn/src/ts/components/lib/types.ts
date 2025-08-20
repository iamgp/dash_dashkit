import React from "react"

export interface ChartConfig {
  [key: string]: {
    label?: React.ReactNode
    icon?: React.ComponentType
    color?: string
    theme?: {
      light: string
      dark: string
    }
  }
}

export interface ChartDataPoint {
  [key: string]: any
}

export interface BaseChartProps {
  id?: string
  className?: string
  config: ChartConfig
  data: ChartDataPoint[]
  children?: React.ReactNode
}

export interface DashChartProps extends BaseChartProps {
  setProps?: (props: any) => void
}