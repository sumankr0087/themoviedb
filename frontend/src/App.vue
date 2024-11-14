
<template>
  <div class="min-h-screen bg-[#1a1a1a]">
    <TheNavbar />
    <main>
      <div v-if="error" class="p-4 text-red-500">
        {{ error }}
      </div>
      <div v-else-if="movie">
        <MovieHeader :movie="movie" />
      </div>
      <div v-else class="p-4 text-white">
        Loading...
      </div>
    </main>
  </div>
</template>

<script lang="ts">
import axios from 'axios';
import TheNavbar from './components/TheNavbar.vue';
import MovieHeader from './components/MovieHeader.vue';
import type { Movie } from './types/movie';

export default {
  name: 'App',
  components: {
    TheNavbar,
    MovieHeader,
  },
  data() {
    return {
      movie: null as Movie | null,
      error: '',
    };
  },
  async mounted() {
    try {
      const response = await axios.get('https://www.omdbapi.com/?i=tt3896198&apikey=d2132124');
      this.movie = response.data;
    } catch (e) {
      this.error = 'Failed to load movie data';
      console.error(e);
    }
  },
};
</script>

