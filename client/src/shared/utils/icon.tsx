import type { ForwardRefExoticComponent, RefAttributes } from 'react'
import type { LucideIcon } from 'lucide-react'

export interface IconProps extends React.SVGAttributes<SVGElement> {
  children?: never
  color?: string
}

// Type for Lucide + Radix icons
export type TIcon =
  | ForwardRefExoticComponent<IconProps & RefAttributes<SVGSVGElement>>
  | LucideIcon
