import { Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <main className="mx-auto w-full max-w-screen-xl">
      <Outlet />
    </main>
  )
}
