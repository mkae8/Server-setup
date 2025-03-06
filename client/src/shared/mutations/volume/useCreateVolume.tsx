import { z } from 'zod'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '@/shared/utils/fetch'
import { QKEY_VOLUME_LIST } from '@/shared/queries/useVolumeList'
import { toast } from 'sonner'
import { TVolume } from '@/shared/types/models/volume'

export type TResponse = TVolume

export const CreateVolumeSchema = z.object({
  volume_year: z.string().min(1),
  volume_no: z.string().min(1),
  title_en: z.string().min(1),
  title_mn: z.string().min(1),
  title_tr: z.string().min(1)
})

export type TParams = z.infer<typeof CreateVolumeSchema>

export type TOpts = TParams

export const useCreateVolume = () => {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: async (opts: TOpts) => {
      const payload = CreateVolumeSchema.parse(opts)
      const { data } = await api.post<TResponse>('/api/volume', payload)
      return data
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: [QKEY_VOLUME_LIST] })
    },
    onSuccess: () => {
      toast.success('Volume has been successfully created!')
    }
  })
}
