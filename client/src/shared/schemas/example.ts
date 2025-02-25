import { z } from 'zod'
export const FormSchema = z.object({
  foo: z.union([z.literal('bar'), z.literal('')])
})

export type TFormSchema = z.infer<typeof FormSchema>
