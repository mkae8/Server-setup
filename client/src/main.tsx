import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { errorHandler } from './shared/utils/fetch'
import Routes from './Routes'
import './index.css'

const router = createBrowserRouter(Routes)

const queryClient = new QueryClient({
  defaultOptions: {
    mutations: {
      onError: errorHandler
    }
  }
})
ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <QueryClientProvider client={queryClient}>
      <RouterProvider router={router} />
    </QueryClientProvider>
  </React.StrictMode>
)
