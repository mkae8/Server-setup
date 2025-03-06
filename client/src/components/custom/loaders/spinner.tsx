import { cn } from '@/lib/utils'
import { LoaderIcon } from 'lucide-react'
import type { IconProps } from '@/shared/utils/icon'

const Spinner = (props: IconProps) => {
  const { className, ...rest } = props
  return (
    <LoaderIcon size={15} className={cn('animate-spin', className)} {...rest} />
  )
}

export default Spinner
