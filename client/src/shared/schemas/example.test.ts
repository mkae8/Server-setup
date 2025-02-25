import { expect, test } from 'vitest'

import { FormSchema } from './example'

test('bar', () => {
  expect(
    FormSchema.parse({
      foo: 'bar'
    })
  ).toStrictEqual({
    foo: 'bar'
  })
})
