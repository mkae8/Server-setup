import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import axios from 'axios'
import { useState } from 'react'

export default function SignupForm() {
  const [data, setData] = useState({
    full_name: '',
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
    axios.post('http://localhost:8000/sign_up', data).catch((err) => {
      console.log(err)
    })
    console.log(data)
  }
  return (
    <form
      onSubmit={handleSubmit}
      className="max-w-xs grow space-y-3 rounded-md border p-3"
    >
      <Label>Full Name</Label>
      <Input name="full_name" onChange={handleChange} />
      <Label>Email</Label>
      <Input name="email" onChange={handleChange} />
      <Label>Password</Label>
      <Input name="password" onChange={handleChange} />
      <Button className="w-full">Signup</Button>
    </form>
  )
}
