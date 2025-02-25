import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { useState } from 'react'

import { Amplify } from 'aws-amplify'
import { signIn } from 'aws-amplify/auth'

Amplify.configure({
  Auth: {
    Cognito: {
      userPoolId: import.meta.env.VITE_AWS_COGNITO_USER_POOL_ID,
      userPoolClientId: import.meta.env.VITE_AWS_COGNITO_APP_CLIENT_ID
    }
  }
})

export default function LoginForm() {
  const [data, setData] = useState({
    email: '',
    password: ''
  })

  const handleChange: React.ChangeEventHandler<HTMLInputElement> = (e) => {
    setData({
      ...data,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit: React.FormEventHandler<HTMLFormElement> = (e) => {
    e.preventDefault()
    
    signIn({
      username: data.email,
      password: data.password
    }).catch((e) => {
      console.log(e)
    })
  }

  return (
    <form
      onSubmit={handleSubmit}
      className="max-w-xs grow space-y-3 rounded-md border p-3"
    >
      <Label>Email</Label>
      <Input name="email" onChange={handleChange} />
      <Label>Password</Label>
      <Input name="password" onChange={handleChange} />
      <Button className="w-full">Login</Button>
    </form>
  )
}
