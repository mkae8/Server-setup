import { useQuery } from '@tanstack/react-query'
import { api } from '@/shared/utils/fetch'
import { TIssue } from '../types/models/issue'

export type TResponse = TIssue

export const QKEY_VOLUME_LIST = 'ISSUE_LIST'

export const useIssueList = () => {
  return useQuery({
    queryKey: [QKEY_VOLUME_LIST],
    queryFn: async ({ signal }) => {
      const { data } = await api.get<TResponse>('api/issue', { signal })
      return data
    }
  })
}
