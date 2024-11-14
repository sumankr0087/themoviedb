<template>
  <div>
    <div class="flex items-center gap-4">
      <div class="flex items-center justify-center space-2">
        <div class="chart flex items-center justify-center">
          <div class="w-16 h-16 inline-block transition-transform duration-200 transform scale-100 details">
            <div class="inline-block w-16 h-16 rounded-full p-1 bg-[#081c22]">
              <div class="relative inline-block w-full h-full text-center" data-bar-color="#21d07a">
                <div class="progress-container">
                  <!-- <canvas ref="canvas"></canvas> -->
                  <canvas ref="canvas" height="120" width="120" style="height: 60px; width: 60px;"></canvas>

                </div>
              </div>
            </div>

          </div>
          <div class="text font-bold ml-1">User<br>Score</div>
          <ul class="flex items-center justify-between ml-4">
            <li
              class="flex items-center justify-center cursor-pointer rounded-full transition-all duration-150 w-9 h-9 bg-[#0B204A]"
              title="Grinning face"><img
                src="https://www.themoviedb.org/assets/2/v8/1f600-f53b445a86235a4ef54899ad2f1a936e3ff6d1dcdaafc9ed63d6a6070491c0a1.svg"
                class="w-7 h-7"></li>
            <li
              class="ml-[-0.75rem] flex items-center justify-center cursor-pointer rounded-full transition-all duration-150 w-9 h-9 bg-[#0B204A]"
              title="Smiling face with heart eyes"><img
                src="https://www.themoviedb.org/assets/2/v8/1f60d-f12478ffe50d98da9d6cafbf29ef1777b8d1d2bb123224c978ca9ba4e6e6159b.svg"
                class="w-7 h-7"></li>
          </ul>
        </div>
      </div>
      <div class="border-[1px] border-[#9F96965C] h-6"></div>
      <div class="bg-[#032541] rounded-full px-4 py-2 flex items-center gap-2">
        <div class="flex items-center text-white font-medium cursor-pointer transform">
          <div class="flex flex-nowrap items-center whitespace-nowrap">
            What's your <span
              class="flex pl-1 underline underline-offset-2 decoration-2 decoration-[#26a4df]">Vibe</span>?
            <svg viewBox="0 0 16 16" fill="currentColor" class="size-4 ml-1">
              <path fill-rule="evenodd"
                d="M15 8A7 7 0 1 1 1 8a7 7 0 0 1 14 0ZM9 5a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM6.75 8a.75.75 0 0 0 0 1.5h.75v1.75a.75.75 0 0 0 1.5 0v-2.5A.75.75 0 0 0 8.25 8h-1.5Z"
                clip-rule="evenodd" />
            </svg>

          </div>
        </div>

      </div>
    </div>

    <div class="lg:flex hidden items-center gap-4 mt-4">
      <div class="mb-5 w-full h-17 flex items-center justify-start">
        <div class="mr-5 box-border bg-[#032541] rounded-full w-[46px] h-[46px] flex items-center justify-center">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-4">
            <path
              d="M3 4.75a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM6.25 3a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM6.25 7.25a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM6.25 11.5a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM4 12.25a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM3 9a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" />
          </svg>

        </div>
        <div class="mr-5 box-border bg-[#032541] rounded-full w-[46px] h-[46px] flex items-center justify-center">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-4">
            <path
              d="M2 6.342a3.375 3.375 0 0 1 6-2.088 3.375 3.375 0 0 1 5.997 2.26c-.063 2.134-1.618 3.76-2.955 4.784a14.437 14.437 0 0 1-2.676 1.61c-.02.01-.038.017-.05.022l-.014.006-.004.002h-.002a.75.75 0 0 1-.592.001h-.002l-.004-.003-.015-.006a5.528 5.528 0 0 1-.232-.107 14.395 14.395 0 0 1-2.535-1.557C3.564 10.22 1.999 8.558 1.999 6.38L2 6.342Z" />
          </svg>
        </div>
        <div class="mr-5 box-border bg-[#032541] rounded-full w-[46px] h-[46px] flex items-center justify-center">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-4">
            <path
              d="M3.75 2a.75.75 0 0 0-.75.75v10.5a.75.75 0 0 0 1.28.53L8 10.06l3.72 3.72a.75.75 0 0 0 1.28-.53V2.75a.75.75 0 0 0-.75-.75h-8.5Z" />
          </svg>
        </div>


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
    </div>

    <!-- Fixed Footer for Mobile and Tablet Views -->
    <footer class="lg:hidden fixed bottom-0 left-0 w-full bg-[#032541] py-2">
      <div class="flex gap-4 justify-center py-3 rounded-b-lg">
        <div class="provider">
          <img src="https://media.themoviedb.org/t/p/original/zdTSUEVZFXp3E0EkOMGN99QPVJp.jpg" width="36" height="36"
            alt="Now Streaming on Hotstar">
        </div>
        <div class="">
          <span>
            <h4 class="leading-[1em] block opacity-80 text-sm font-normal m-0">Now Streaming</h4>
            <h3 class="block text-[1em] leading-[1em] m-0">Watch
                Now</h3>
          </span>
        </div>
      </div>
      <div class="flex items-center justify-between px-20">
        <div class="box-border rounded-full w-[46px] h-[46px] flex items-center justify-center bg-[#032541]">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-6">
            <path
              d="M3 4.75a1 1 0 1 0 0-2 1 1 0 0 0 0 2ZM6.25 3a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM6.25 7.25a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM6.25 11.5a.75.75 0 0 0 0 1.5h7a.75.75 0 0 0 0-1.5h-7ZM4 12.25a1 1 0 1 1-2 0 1 1 0 0 1 2 0ZM3 9a1 1 0 1 0 0-2 1 1 0 0 0 0 2Z" />
          </svg>
        </div>

        <div class="box-border rounded-full w-[46px] h-[46px] flex items-center justify-center bg-[#032541]">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-6">
            <path
              d="M2 6.342a3.375 3.375 0 0 1 6-2.088 3.375 3.375 0 0 1 5.997 2.26c-.063 2.134-1.618 3.76-2.955 4.784a14.437 14.437 0 0 1-2.676 1.61c-.02.01-.038.017-.05.022l-.014.006-.004.002h-.002a.75.75 0 0 1-.592.001h-.002l-.004-.003-.015-.006a5.528 5.528 0 0 1-.232-.107 14.395 14.395 0 0 1-2.535-1.557C3.564 10.22 1.999 8.558 1.999 6.38L2 6.342Z" />
          </svg>
        </div>

        <div class="box-border rounded-full w-[46px] h-[46px] flex items-center justify-center bg-[#032541]">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-6">
            <path
              d="M3.75 2a.75.75 0 0 0-.75.75v10.5a.75.75 0 0 0 1.28.53L8 10.06l3.72 3.72a.75.75 0 0 0 1.28-.53V2.75a.75.75 0 0 0-.75-.75h-8.5Z" />
          </svg>
        </div>
        <div class="box-border rounded-full w-[46px] h-[46px] flex items-center justify-center bg-[#032541]">
          <svg viewBox="0 0 16 16" fill="currentColor" class="size-6">
            <path fill-rule="evenodd"
              d="M8 1.75a.75.75 0 0 1 .692.462l1.41 3.393 3.664.293a.75.75 0 0 1 .428 1.317l-2.791 2.39.853 3.575a.75.75 0 0 1-1.12.814L7.998 12.08l-3.135 1.915a.75.75 0 0 1-1.12-.814l.852-3.574-2.79-2.39a.75.75 0 0 1 .427-1.318l3.663-.293 1.41-3.393A.75.75 0 0 1 8 1.75Z"
              clip-rule="evenodd" />
          </svg>

        </div>
      </div>
    </footer>

  </div>
</template>

<script>
export default {
  data() {
    return {
      progress: 76, // Example progress percentage
      radius: 50,   // Circle radius
      lineWidth: 10, // Line width for the circle
      trackColor: '#2c462b', // Track color (green)
      progressColor: '#21d07a', // Progress color (light green)
      canvasSize: 120, // Size of the canvas (width and height)
    };
  },
  mounted() {
    this.drawProgressCircle();
  },
  methods: {
    drawProgressCircle() {
      const canvas = this.$refs.canvas;
      const ctx = canvas.getContext('2d');

      // Check if ctx is available (canvas context)
      if (ctx) {
        // Clear canvas before drawing new circle
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        // Set the canvas width and height based on canvasSize
        canvas.width = this.canvasSize;
        canvas.height = this.canvasSize;

        // Draw the background circle (track)
        ctx.beginPath();
        ctx.arc(this.canvasSize / 2, this.canvasSize / 2, this.radius, 0, 2 * Math.PI); // Full circle (360 degrees)
        ctx.lineWidth = this.lineWidth;
        ctx.strokeStyle = this.trackColor;
        ctx.stroke();

        // Draw the progress arc
        const progressAngle = (this.progress / 100) * 2 * Math.PI; // Calculate angle based on progress
        ctx.beginPath();
        ctx.arc(this.canvasSize / 2, this.canvasSize / 2, this.radius, -Math.PI / 2, -Math.PI / 2 + progressAngle); // Arc from -90 degrees
        ctx.lineWidth = this.lineWidth;
        ctx.strokeStyle = this.progressColor;
        ctx.stroke();

        ctx.fillStyle = this.progressColor;
        ctx.font = '30px Arial';
        ctx.fillStyle = '#fff';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`${this.progress}%`, this.canvasSize / 2, this.canvasSize / 2);
      }
    },
  },
};
</script>


<style scoped>
.progress-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 100%;
}

canvas {
  border-radius: 50%;
  /* Optional: To make the canvas round */
}
</style>

