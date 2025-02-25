import { resolve } from 'path'
import { defineConfig } from 'vite'

// Plugins
import react from '@vitejs/plugin-react-swc'
import tailwindcss from '@tailwindcss/vite'
// import eslintPlugin from 'vite-plugin-eslint'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    tailwindcss()
    // eslintPlugin({
    //   cache: false,
    //   include: ['./src/**/*.ts', './src/**/*.tsx'],
    //   exclude: []
    // })
  ],
  server: {
    port: 4000
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, './src')
    }
  }
})
