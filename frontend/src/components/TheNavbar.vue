<template>
  <nav class="bg-[#011e37] text-white">
    <div class="px-4 lg:px-16">
      <div class="flex items-center justify-between h-16">
        <!-- Mobile Menu Button -->
        <button class="block lg:hidden p-2">
          <svg viewBox="0 0 16 16" fill="currentColor" class="w-8 h-8 text-white">
            <path fill-rule="evenodd"
              d="M2 3.75A.75.75 0 0 1 2.75 3h10.5a.75.75 0 0 1 0 1.5H2.75A.75.75 0 0 1 2 3.75ZM2 8a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H2.75A.75.75 0 0 1 2 8Zm0 4.25a.75.75 0 0 1 .75-.75h10.5a.75.75 0 0 1 0 1.5H2.75a.75.75 0 0 1-.75-.75Z"
              clip-rule="evenodd" />
          </svg>
        </button>

        <!-- Center Logo for Mobile -->
        <div class="block lg:hidden absolute left-1/2 transform -translate-x-1/2">
          <img
            src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_square_2-d537fb228cf3ded904ef09b136fe3fec72548ebc1fea3fbbd1ad9e36364db38b.svg"
            alt="The Movie Database (TMDB)" width="50" height="40" />
        </div>

        <!-- Desktop Navigation Menu -->
        <div class="hidden lg:flex items-center gap-x-6">
          <img
            src="https://www.themoviedb.org/assets/2/v4/logos/v2/blue_short-8e7b30f73a4020692ccca9c88bafe5dcb6f8a62a4c6bc55cd9ba82bb2cd95f6c.svg"
            alt="The Movie Database (TMDB)" width="154" height="20" />

          <div class="hidden lg:flex space-x-6">
            <div v-for="item in menuItems" :key="item.label" class="relative group">
              <button class="py-2 text-sm font-medium">
                {{ item.label }}
              </button>
              <div class="hidden group-hover:block absolute z-50 mt-2 w-48 bg-white text-gray-800 rounded shadow-lg">
                <div v-for="subItem in item.items" :key="subItem" class="px-4 py-2 hover:bg-gray-100 cursor-pointer">
                  {{ subItem }}
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Right-side Icons for Desktop -->
        <div class="flex lg:hidden gap-x-4">
          <div>
            <svg viewBox="0 0 16 16" fill="currentColor" class="size-6">
              <path
                d="M8 8a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM12.735 14c.618 0 1.093-.561.872-1.139a6.002 6.002 0 0 0-11.215 0c-.22.578.254 1.139.872 1.139h9.47Z" />
            </svg>
          </div>
          <img
            src="https://www.themoviedb.org/assets/2/v4/glyphicons/basic/glyphicons-basic-28-search-blue-177462d06db81ff2a02aa022c1c0be5ba4200d7bd3f51091ed9298980e3a26a1.svg"
            alt="Search Icon" width="30" height="24" />
        </div>

        <!-- User Options for Desktop -->
        <div class="hidden lg:flex items-center gap-x-4">
          <button class="font-bold">
            <svg viewBox="0 0 16 16" fill="currentColor" class="w-6 h-6">
              <path
                d="M8.75 3.75a.75.75 0 0 0-1.5 0v3.5h-3.5a.75.75 0 0 0 0 1.5h3.5v3.5a.75.75 0 0 0 1.5 0v-3.5h3.5a.75.75 0 0 0 0-1.5h-3.5v-3.5Z" />
            </svg>
          </button>

          <button class="hover:bg-white hover:text-black border rounded px-1">
            <span class="text-sm">EN</span>
          </button>

          <button class="bg-transparent px-3 py-1">Login</button>
          <button class="bg-transparent px-3 py-1">Join TMDB</button>
          <button class="text-blue-500">
            <img
              src="https://www.themoviedb.org/assets/2/v4/glyphicons/basic/glyphicons-basic-28-search-blue-177462d06db81ff2a02aa022c1c0be5ba4200d7bd3f51091ed9298980e3a26a1.svg"
              alt="Search Icon" width="30" height="24" />
          </button>
        </div>
      </div>
    </div>

    <!-- Sub-navigation Links -->
    <div class="bg-white py-4 text-black flex justify-center space-x-6">
      <div v-for="link in ['Overview', 'Media', 'Fandom', 'Share']" :key="link" class="flex items-center space-x-2">
        <div>{{ link }}</div>
        <span>
          <svg class="w-4 h-4" viewBox="0 0 512 512">
            <path d="M256 352 128 160h256z"></path>
          </svg>
        </span>
      </div>
    </div>
  </nav>
</template>

<script lang="ts">
export default {
  name: 'TheNavbar',
  data() {
    return {
      menuItems: [
        { label: 'Movies', items: ['Popular', 'Now Playing', 'Upcoming', 'Top Rated'] },
        { label: 'TV Shows', items: ['Popular', 'Airing Today', 'On TV', 'Top Rated'] },
        { label: 'People', items: ['Popular People'] },
        { label: 'More', items: ['Discussions', 'Leaderboard', 'Support', 'API'] },
      ],
    };
  },
};
</script>
