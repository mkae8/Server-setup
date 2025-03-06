import { z } from 'zod'
import { useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '@/shared/utils/fetch'
import { QKEY_VOLUME_LIST } from '@/shared/queries/useVolumeList'
import { toast } from 'sonner'
import { TVolume } from '@/shared/types/models/volume'

export type TResponse = TVolume

export const UpdateVolumeSchema = z.object({
  id: z.string().optional(),
  volume_year: z.string().min(1),
  volume_no: z.string().min(1),
  title_en: z.string().min(1),
  title_mn: z.string().min(1),
  title_tr: z.string().min(1)
})

export type TParams = z.infer<typeof UpdateVolumeSchema>

export type TOpts = TParams

export const useUpdateVolume = () => {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: async (opts: TOpts) => {
      const payload = UpdateVolumeSchema.parse(opts)

      if (payload.id) {
        const { data } = await api.put<TResponse>(
          `/api/volume/${payload.id}`,
          payload
        )
        return data
      } else {
        const { data } = await api.post<TResponse>('/api/volume', payload)
        return data
      }
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: [QKEY_VOLUME_LIST] })
    },
    onSuccess: (data) => {
      toast.success(`Volume has been successfully ${data} updated`)
    }
  })
}
