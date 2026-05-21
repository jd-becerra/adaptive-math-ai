<template>
  <div>
    <h2>Teacher Panel</h2>

    <p>
      <router-link to="/">
        Back to Main Panel
      </router-link>
    </p>

    <input v-model="question" placeholder="Question" />

    <button @click="generate">
      Generate Variants
    </button>

    <pre>{{ result }}</pre>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { generateExercise } from '../services/api'

const question = ref('')
const result = ref('')

async function generate() {

  result.value = await generateExercise({
    topic: 'math',
    question: question.value,
    answer: '10',
    difficulty: 1
  })
}
</script>