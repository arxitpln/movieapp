<template>
  <v-container v-if="movie">
    <h2>{{ movie.title }}</h2>
    <MovieForm :movie="movie" @update="saveEdit" />
    <p>Note moyenne : {{ movie.average_grade }}</p>
    <ul>
      <li v-for="actor in movie.actors" :key="actor.id">
        {{ actor.first_name }} {{ actor.last_name }}
      </li>
    </ul>
    <ReviewForm @submit="addReview" />
  </v-container>
</template>

<script setup>
import { useMovieStore } from '../stores/movieStore';
import { onMounted, computed } from 'vue';
import { useRoute } from 'vue-router';
import MovieForm from '../components/MovieForm.vue';
import ReviewForm from '../components/ReviewForm.vue';

const store = useMovieStore();
const route = useRoute();

onMounted(() => {
  store.fetchMovie(route.params.id);
});

const movie = computed(() => store.selectedMovie);

const saveEdit = (data) => {
  store.updateMovie(parseInt(route.params.id), data);
};

const addReview = (review) => {
  store.addReview(parseInt(route.params.id), review);
};
</script>
