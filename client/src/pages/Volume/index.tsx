import {
  CreateVolumeSchema,
  TParams,
  useCreateVolume
} from '@/shared/mutations/volume/useCreateVolume'
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form'
import { Input } from '@/components/ui/input'
import { Button } from '@/components/ui/button'

const VolumeCreatePage = () => {
  const { mutate, isPending } = useCreateVolume()

  const form = useForm<TParams>({
    resolver: zodResolver(CreateVolumeSchema),
    defaultValues: {
      title_tr: '',
      title_mn: '',
      title_en: '',
      volume_year: '',
      volume_no: ''
    }
  })

  const onSubmit = (data: TParams) => {
    if (isPending) return
    mutate(data, {
      onSettled: () => {
        form.reset()
      }
    })
  }
  return (
    <div>
      <Form {...form}>
        <form
          className="bg-card text-card-foreground flex h-max max-w-xs grow flex-col gap-4 rounded-lg border p-2 shadow-sm"
          onSubmit={form.handleSubmit(onSubmit)}
        >
          <div className="space-y-1">
            <div>Create User</div>
            <div>Please input the field below</div>
          </div>
          <div className="space-y-4 rounded-lg">
            <FormField
              control={form.control}
              name="volume_year"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Volume year</FormLabel>
                  <FormControl>
                    <Input
                      className="bg-card"
                      placeholder="Volume year"
                      inputMode="numeric"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="volume_no"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Volume no</FormLabel>
                  <FormControl>
                    <Input
                      className="bg-card"
                      placeholder="Volume year"
                      inputMode="numeric"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="title_tr"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>title tr</FormLabel>
                  <FormControl>
                    <Input
                      className="bg-card"
                      placeholder="Volume year"
                      inputMode="text"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="title_mn"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>title_mn</FormLabel>
                  <FormControl>
                    <Input
                      className="bg-card"
                      placeholder="Volume year"
                      inputMode="text"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
            <FormField
              control={form.control}
              name="title_en"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>title_en</FormLabel>
                  <FormControl>
                    <Input
                      className="bg-card"
                      placeholder="Volume year"
                      inputMode="text"
                      {...field}
                    />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />
          </div>
          <Button
            isLoading={isPending}
            disabled={isPending || !form.formState.isDirty}
            type="submit"
          >
            Create Volume
          </Button>
        </form>
      </Form>
    </div>
  )
}

export default VolumeCreatePage
