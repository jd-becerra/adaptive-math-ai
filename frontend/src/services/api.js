const API_URL = 'http://localhost:12000'

export async function generateExercise(data) {

    const response = await fetch(
        `${API_URL}/exercises/generate`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    )

    return response.json()
}

export async function submitAnswer(data) {

    const response = await fetch(
        `${API_URL}/student/answer`,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    )

    return response.json()
}