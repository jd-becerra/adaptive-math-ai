<template>
  <div>

    <h2>Student Panel</h2>

    <p>
      <router-link to="/">
        Back to Main Panel
      </router-link>
    </p>

    <div v-if="completed">

      <h3>No more questions!</h3>

      <button @click="startQuiz">
        Restart Quiz
      </button>

    </div>

    <div v-else-if="currentQuestion">

      <p>
        {{ currentQuestion.question }}
      </p>

      <input
        v-model="studentAnswer"
        :disabled="loading"
        placeholder="Type your answer"
      />

      <button
        @click="submit"
        :disabled="loading || !studentAnswer.trim()"
      >
        {{ loading ? 'Checking...' : 'Submit' }}
      </button>

      <p v-if="loading">
        Calculating results...
      </p>

      <p v-if="!loading && feedback">
        {{ feedback }}
      </p>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const API_URL = 'http://localhost:12000'

const currentQuestion = ref(null)
const studentAnswer = ref('')
const feedback = ref('')
const completed = ref(false)
const loading = ref(false)

async function startQuiz() {

  loading.value = true

  try {

    const response = await fetch(
      `${API_URL}/student/start`,
      {
        method: 'POST'
      }
    )

    const data = await response.json()

    currentQuestion.value = data.question

    completed.value = false

    feedback.value = ''

  } catch(error) {

    console.error(error)

  } finally {

    loading.value = false
  }
}

async function submit() {

  // Prevent double clicks
  if (loading.value) return

  // Prevent empty answers
  if (!studentAnswer.value.trim()) return

  loading.value = true

  try {

    const response = await fetch(
      `${API_URL}/student/answer`,
      {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          topic: currentQuestion.value.topic,
          question: currentQuestion.value.question,
          correct_answer: currentQuestion.value.answer,
          student_answer: studentAnswer.value
        })
      }
    )

    const data = await response.json()

    feedback.value = data.correct
      ? 'Correct!'
      : 'Incorrect!'

    currentQuestion.value = data.next_question

    completed.value = data.completed

    studentAnswer.value = ''

  } catch(error) {

    console.error(error)

    feedback.value = 'Something went wrong.'

  } finally {

    loading.value = false
  }
}

onMounted(() => {
  startQuiz()
})
</script>