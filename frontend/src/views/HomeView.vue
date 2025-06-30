<template>
  <v-container>
    <v-row>
      <MovieCard
        v-for="movie in movieStore.movies"
        :key="movie.id"
        :movie="movie"
        @click="$router.push(`/movie/${movie.id}`)"
      />
    </v-row>
    <v-pagination
      v-model="currentPage"
      :length="Math.ceil(movieStore.count / MOVIES_PER_PAGE)"
      @input="changePage"
    />
  </v-container>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useMovieStore } from '../stores/movieStore'
import { MOVIES_PER_PAGE } from '@/config'
import MovieCard from '../components/MovieCard.vue'

const movieStore = useMovieStore()
const currentPage = ref(movieStore.page)

const changePage = (page) => {
  movieStore.fetchMovies(page)
}

watch(currentPage, changePage)
movieStore.fetchMovies()
</script>
