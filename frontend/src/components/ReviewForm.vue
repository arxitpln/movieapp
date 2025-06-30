<template>
  <v-form @submit.prevent="submit">
    <v-slider v-model="grade" min="1" max="5" step="1" label="Note" />
    <v-btn type="submit">Ajouter un avis</v-btn>
  </v-form>
</template>

<script setup>
import { ref } from 'vue'
const grade = ref(3)
const emit = defineEmits(['submit'])

function submit() {
  emit('submit', { grade: grade.value })
  grade.value = 3
}
</script>
