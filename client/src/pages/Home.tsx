import LoginForm from './forms/login'
import SignupForm from './forms/signup'

export default function Home() {
  return (
    <div className="flex w-full gap-4 p-8">
      <SignupForm />
      <LoginForm />
    </div>
  )
}
