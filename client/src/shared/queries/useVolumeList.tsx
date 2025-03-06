import { useQuery } from '@tanstack/react-query'
import { api } from '@/shared/utils/fetch'
import { TVolume } from '@/shared/types/models/volume'

export type TResponse = TVolume

export const QKEY_VOLUME_LIST = 'VOLUME_LIST'

export const useVolumeList = () => {
  return useQuery({
    queryKey: [QKEY_VOLUME_LIST],
    queryFn: async ({ signal }) => {
      const { data } = await api.get<TResponse>('/api/volumes', {
        signal
      })
      return data
    }
  })
}
