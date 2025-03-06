'use client'

import { useVolumeList } from '@/shared/queries/useVolumeList'

export const FetchVolumeData = () => {
  const { isSuccess, data } = useVolumeList()

  return (
    <div className="flex h-[500px] w-[400px] overflow-scroll">
      <div className="flex w-full flex-col gap-4">
        {isSuccess &&
          data?.map((volume) => (
            <div
              key={volume.volume_no || volume.id}
              className="rounded-lg border p-4 hover:shadow-md"
            >
              <div className="mb-2 flex justify-between">
                <h3 className="font-semibold">Year: {volume.volume_year}</h3>
                <h3 className="font-semibold">Volume: {volume.volume_no}</h3>
              </div>
              <div>
                <p className="text-sm font-medium">
                  English: {volume.title_en}
                </p>
                <p className="text-sm font-medium">
                  Mongolian: {volume.title_mn}
                </p>
                <p className="text-sm font-medium">
                  Turkish: {volume.title_tr}
                </p>
              </div>
            </div>
          ))}
      </div>
    </div>
  )
}
