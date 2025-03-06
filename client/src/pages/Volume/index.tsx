import { FetchVolumeData } from './volume_form/fetchVolumeData'
import VolumeCreatePage from './volume_form/form'

const VolumePage = () => {
  return (
    <div className="mt-20 flex items-center gap-10">
      <VolumeCreatePage />
      <FetchVolumeData />
    </div>
  )
}

export default VolumePage
