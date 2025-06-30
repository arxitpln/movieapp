<template>
  <v-form @submit.prevent="$emit('update', { title, description, actors })">
    <v-text-field label="Titre" v-model="title" />
    <v-textarea label="Description" v-model="description" />
    <v-textarea label="Acteurs (prénom nom, séparés par des virgules)" v-model="actorInput" />
    <v-btn type="submit">Mettre à jour</v-btn>
  </v-form>
</template>

<script setup>
import { ref, watch } from 'vue';

const props = defineProps(['movie']);
const emit = defineEmits(['update']);

const title = ref('');
const description = ref('');
const actorInput = ref('');
const actors = ref([]);

watch(() => props.movie, (movie) => {
  if (movie) {
    title.value = movie.title;
    description.value = movie.description;
    actorInput.value = movie.actors.map(a => `${a.first_name} ${a.last_name}`).join(', ');
  }
}, { immediate: true });

watch(actorInput, (input) => {
  actors.value = input.split(',').map(s => {
    const [first_name, last_name] = s.trim().split(' ');
    return { first_name, last_name };
  });
});
</script>
