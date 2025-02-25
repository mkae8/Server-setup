import { useForm } from 'react-hook-form'

import { zodResolver } from '@hookform/resolvers/zod'
import { Button } from '../ui/button'
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage
} from '@/components/ui/form'
import { Input } from '../ui/input'
import { FormSchema, type TFormSchema } from '@/shared/schemas/example'

export default function FoobarForm() {
  const form = useForm<TFormSchema>({
    defaultValues: {
      foo: ''
    },
    resolver: zodResolver(FormSchema)
  })
  return (
    <Form {...form}>
      <form
        onSubmit={form.handleSubmit((data) => {
          console.log(data)
        })}
        className="w-full max-w-xs space-y-8"
      >
        <FormField
          control={form.control}
          name="foo"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Foo</FormLabel>
              <FormControl>
                <Input placeholder="bar" {...field} />
              </FormControl>
              <FormDescription>Type bar.</FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button
          type="submit"
          disabled={
            !form.formState.isDirty || form.formState.isSubmitSuccessful
          }
        >
          {form.formState.isSubmitSuccessful ? 'Success' : 'Submit'}
        </Button>
      </form>
    </Form>
  )
}
