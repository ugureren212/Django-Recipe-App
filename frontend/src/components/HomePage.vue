<template>
  <div>
    <header>
      <h1
        class="text-center font-black pb-6 text-4xl bg-clip-text text-transparent bg-gradient-to-r from-purple-500 to-pink-500 md:text-5xl lg:text-6xl"
      >
        Recipe App
      </h1>
    </header>
    <div id="mainContent">
      <div class="grid grid-cols-3 gap-4">
        <div class="col-span-1"><RecipeForum /></div>
        <div class="col-span-2"><RecipeList /></div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import RecipeList from "./RecipeList.vue";
import RecipeForum from "./RecipeForum.vue";

export default defineComponent({
  name: "HomePage",
  components: { RecipeList, RecipeForum },
});
</script>

<style scoped></style>
