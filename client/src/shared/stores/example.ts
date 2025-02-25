import { create } from 'zustand'
import { immer } from 'zustand/middleware/immer'

type ExampleStore = {
  count: number
}

type Actions = {
  increment: () => void
  decrement: () => void
  reset: () => void
}

const IState: ExampleStore = {
  count: 0
}

const ResetState: ExampleStore = {
  count: 0
}

export const useExampleStore = create(
  immer<ExampleStore & Actions>((set) => ({
    ...IState,
    increment: () =>
      set((state) => {
        state.count += 1
      }),
    decrement: () =>
      set((state) => {
        state.count -= 1
      }),
    reset: () => set(ResetState)
  }))
)
