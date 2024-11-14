<template>
  <div class="relative">
    <!-- Content visible on mobile/tablet -->
    <div class="bg-cover bg-no-repeat lg:hidden mb-[9rem]">
      <div class="shadow-none min-w-full w-full h-auto rounded-none">
        <div class="min-w-full w-full rounded-none">
          <div
            style="background-image: url('https://media.themoviedb.org/t/p/w1000_and_h450_multi_faces/aJn9XeesqsrSLKcHfHP4u5985hn.jpg');">
            <div class="p-[1.25rem] z-4 overflow-hidden rounded-lg" style="width: calc(((100vw / 2.222222) - 40px) / 1.5);
            background-image: linear-gradient(to right, rgba(10.5, 31.5, 73.5, 1) 20%, rgba(10.5, 31.5, 73.5, 0) 50%);">
              <img class="w-full"
                src="https://media.themoviedb.org/t/p/w116_and_h174_face/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg"
                srcset="https://media.themoviedb.org/t/p/w116_and_h174_face/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg 1x, https://media.themoviedb.org/t/p/w220_and_h330_face/y4MBh0EjBlMuOzv9axM4qJlmhzz.jpg 2x"
                alt="Guardians of the Galaxy Vol. 2">
            </div>
          </div>
        </div>

        <div class="flex-grow bg-[#0B204AFF] text-white">
          <h1 class="w-full m-0 py-4 md:text-4xl text-2xl flex justify-center font-semibold">
            {{ movie.Title }}
            <span class="opacity-80 font-normal">({{ movie.Year }})</span>
          </h1>

          <MovieActions class="mb-6 justify-center flex" />


          <div class="lg:flex hidden flex-wrap items-center gap-2 text-sm mb-4">
            <span class="border rounded-sm py-[.06em] px-[4px] pb-[.15em] border-[#ffffff99] text-[#ffffff99]">{{
              movie.Rated }}</span>
            <span class="font-normal text-sm">{{ formatDate(movie.Released) }}</span>
            <span class="w-1 h-1 bg-white rounded-full"></span>
            <span class="font-normal text-sm">{{ movie.Genre }}</span>
            <span class="w-1 h-1 bg-white rounded-full"></span>
            <span class="font-normal text-sm">{{ formatRuntime(movie.Runtime) }}</span>
          </div>
          <!-- mobile view -->
          <div class="bg-[#0000001A] py-3">
            <div class="flex flex-wrap justify-center items-center gap-2 text-sm">
              <span class="border rounded-sm py-[.06em] px-[4px] pb-[.15em] border-[#ffffff99] text-[#ffffff99]">{{
                movie.Rated }}</span>
              <span class="font-normal text-sm">{{ formatDate(movie.Released) }}</span>

              <span class="w-1 h-1 bg-white rounded-full"></span>
              <span class="font-normal text-sm">{{ formatRuntime(movie.Runtime) }}</span>
              <div class="mr-5 box-border flex items-center rounded-full w-auto h-[46px]">
                <div>
                  <svg viewBox="0 0 16 16" fill="currentColor" class="size-5">
                    <path
                      d="M3 3.732a1.5 1.5 0 0 1 2.305-1.265l6.706 4.267a1.5 1.5 0 0 1 0 2.531l-6.706 4.268A1.5 1.5 0 0 1 3 12.267V3.732Z" />
                  </svg>
                </div>

                <span class="ml-2">Play Trailer</span>
              </div>
            </div>
            <span class="font-normal flex justify-center text-sm">{{ movie.Genre }}</span>
          </div>


          <div class="mt-8 ml-8">
            <h3 class="mb-0 text-base font-light italic opacity-70">Obviously.</h3>
            <h3 class="font-semibold text-[1.3em] mb-2">Overview</h3>
            <p class="text-sm leading-[1.5rem] font-light">{{ movie.Plot }}</p>
          </div>

          <div class="mt-6 ml-8 grid grid-cols-2 gap-x-8 gap-y-4">
            <div v-if="movie.Director">
              <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ movie.Director }}</span>
              <span class="block text-sm leading-[1.5rem] font-light">Director, Writer</span>
            </div>
            <div v-for="(writer, index) in uniqueWriters" :key="'writer-' + index" class="flex-1 min-w-[120px]">
              <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ writer }}</span>
              <span class="block text-sm leading-[1.5rem] font-light">Writer</span>
            </div>

            <div v-for="(actor, index) in uniqueActors" :key="'actor-' + index" class="flex-1 min-w-[120px]">
              <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ actor }}</span>
              <span class="block text-sm leading-[1.5rem] font-light">Actor</span>
            </div>
          </div>
        </div>


      </div>
    </div>

    <!-- Content visible only on desktop -->
    <div class="relative hidden lg:block min-h-[595px] bg-gray-900 text-white"
      :style="{ backgroundImage: `url('https://media.themoviedb.org/t/p/w1920_and_h800_multi_faces/aJn9XeesqsrSLKcHfHP4u5985hn.jpg')` }">
      <div class="absolute inset-0 bg-gradient-to-r from-gray-900 via-gray-900/70 to-transparent"></div>
      <div class="mx-auto custom_bg px-16 py-8 relative z-10">
        <div class="lg:flex flex-col md:flex-row gap-8">
          <div class="w-80 flex-shrink-0">
            <img :src="movie.Poster" :alt="movie.Title" class="rounded shadow-lg w-full">
            <div class="bg-[#011e37]">
              <div class="hidden lg:flex gap-4 justify-center py-3 rounded-b-lg">
                <div class="provider">
                  <img src="https://media.themoviedb.org/t/p/original/zdTSUEVZFXp3E0EkOMGN99QPVJp.jpg" width="36"
                    height="36" alt="Now Streaming on Hotstar">
                </div>
                <div class="">
                  <span>
                    <h4 class="leading-[1em] block opacity-80 text-sm font-normal m-0">Now Streaming</h4>
                    <h3 class="block text-[1em] leading-[1em] m-0">Watch
                        Now</h3>
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div class="flex-grow">
            <h1 class="w-full m-0 p-0 text-[2.2rem] font-semibold">
              {{ movie.Title }}
              <span class="opacity-80 font-normal">({{ movie.Year }})</span>
            </h1>

            <div class="flex flex-wrap items-center gap-2 text-sm mb-4">
              <span class="border rounded-sm py-[.06em] px-[4px] pb-[.15em] border-[#ffffff99] text-[#ffffff99]">{{
                movie.Rated }}</span>
              <span class="font-normal text-sm">{{ formatDate(movie.Released) }}</span>
              <span class="w-1 h-1 bg-white rounded-full"></span>
              <span class="font-normal text-sm">{{ movie.Genre }}</span>
              <span class="w-1 h-1 bg-white rounded-full"></span>
              <span class="font-normal text-sm">{{ formatRuntime(movie.Runtime) }}</span>
            </div>

            <MovieActions class="mb-6" />

            <div class="mt-8">
              <h3 class="mb-0 text-base font-light italic opacity-70">Obviously.</h3>
              <h3 class="font-semibold text-[1.3em] mb-2">Overview</h3>
              <p class="text-sm leading-[1.5rem] font-light">{{ movie.Plot }}</p>
            </div>

            <div class="mt-6 grid grid-cols-3 gap-x-8 gap-y-4">
              <div v-if="movie.Director">
                <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ movie.Director }}</span>
                <span class="block text-sm leading-[1.5rem] font-light">Director, Writer</span>
              </div>
              <div v-for="(writer, index) in uniqueWriters" :key="'writer-' + index" class="flex-1 min-w-[120px]">
                <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ writer }}</span>
                <span class="block text-sm leading-[1.5rem] font-light">Writer</span>
              </div>

              <div v-for="(actor, index) in uniqueActors" :key="'actor-' + index" class="flex-1 min-w-[120px]">
                <span class="text-base font-semibold m-0 p-0 overflow-hidden truncate">{{ actor }}</span>
                <span class="block text-sm leading-[1.5rem] font-light">Actor</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>
<script lang="ts">
import { defineComponent } from 'vue';
import type { Movie } from '../types/movie';
import MovieActions from './MovieActions.vue';

export default defineComponent({
  name: 'MovieDetail',
  components: {
    MovieActions
  },
  props: {
    movie: {
      type: Object as () => Movie,
      required: true
    }
  },
  computed: {
    formatDate(): (date: string) => string {
      return (date: string) => {
        const options = { day: '2-digit', month: '2-digit', year: 'numeric' };
        const formattedDate = new Date(date).toLocaleDateString('en-IN', options);
        return `${formattedDate} (IN)`;
      };
    },
    formatRuntime(): (runtime: string) => string {
      return (runtime: string) => {
        const minutes = parseInt(runtime);
        const hours = Math.floor(minutes / 60);
        const remainingMinutes = minutes % 60;
        return `${hours}h ${remainingMinutes}m`;
      };
    },
    uniqueWriters() {
      const writers = this.movie.Writer.split(',').map(w => w.trim());
      const uniqueWritersSet = new Set(writers);
      uniqueWritersSet.delete(this.movie.Director);
      return Array.from(uniqueWritersSet);
    },
    uniqueActors() {
      const actors = this.movie.Actors.split(',').map(a => a.trim());
      const uniqueActorsSet = new Set(actors);
      return Array.from(uniqueActorsSet);
    }
  }
});
</script>

<style scoped>
.backdrop-blur {
  backdrop-filter: blur(10px);
}

.custom_bg {
    background-image: linear-gradient(to right, rgba(10.5, 31.5, 73.5, 1) calc((50vw - 170px) - 340px), rgba(10.5, 31.5, 73.5, 0.84) 50%, rgba(10.5, 31.5, 73.5, 0.84) 100%);
}
</style>
