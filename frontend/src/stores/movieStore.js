import { defineStore } from 'pinia'
import axios from 'axios'
import { MOVIES_PER_PAGE } from '@/config'

const API_BASE = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

export const useMovieStore = defineStore('movie', {
  state: () => ({
    movies: [],
    selectedMovie: null,
    count: 0,
    page: 1,
  }),
  actions: {
    async fetchMovies(page = 1) {
      if (page === this.page && this.movies.length > 0) return
      const response = await axios.get(`${API_BASE}/movies/?page=${page}&count=${MOVIES_PER_PAGE}`)
      this.movies = response.data.results
      this.count = response.data.count
      this.page = page
    },
    async fetchMovie(id) {
      if (this.selectedMovie?.id === id) return
      const response = await axios.get(`${API_BASE}/movies/${id}/`)
      this.selectedMovie = response.data
    },
    async updateMovie(id, data) {
      if (this.selectedMovie?.id === id) {
        const hasChanged = Object.keys(data).some(key => data[key] !== this.selectedMovie[key])
        if (!hasChanged) return
      }

      const response = await axios.put(`${API_BASE}/movies/${id}/`, data)
      this.selectedMovie = response.data
      const index = this.movies.findIndex(m => m.id === id)
      if (index !== -1) {
        this.movies[index] = response.data
      }
    },
    async addReview(movieId, review) {
      await axios.post(`${API_BASE}/reviews/`, {
        grade: review.grade,
        movie: movieId
      })
      if (this.selectedMovie?.id === movieId) {
        await this.fetchMovie(movieId)
      }
    }
  }
})
