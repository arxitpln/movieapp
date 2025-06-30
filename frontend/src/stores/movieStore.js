import { defineStore } from 'pinia'
import axios from 'axios'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export const useMovieStore = defineStore('movie', {
  state: () => ({
    movies: [],
    selectedMovie: null,
    count: 0,
    page: 1
  }),
  actions: {
    async fetchMovies(page = 1) {
      const response = await axios.get(`${API_BASE}/movies/?page=${page}&count=5`)
      this.movies = response.data.results
      this.count = response.data.count
      this.page = page
    },
    async fetchMovie(id) {
      const response = await axios.get(`${API_BASE}/movies/${id}/`)
      this.selectedMovie = response.data
    },
    async updateMovie(id, data) {
      const response = await axios.put(`${API_BASE}/movies/${id}/`, data)
      this.selectedMovie = response.data
    },
    async addReview(movieId, review) {
      await axios.post(`${API_BASE}/reviews/`, {
        grade: review.grade,
        movie: movieId
      })
      await this.fetchMovie(movieId) // refresh
    }
  }
})
