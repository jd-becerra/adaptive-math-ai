const BASE_URL = 'http://localhost:8000'

export async function fetchExercises() {
  const response = await fetch(`${BASE_URL}/exercises/`)
  return response.json()
}
