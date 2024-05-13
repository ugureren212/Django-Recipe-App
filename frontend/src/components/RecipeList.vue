<template>
  <div>
    <div class="text-center my-4">
      <h3
        class="text-center mb-4 text-2xl font-extrabold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-4xl dark:text-white"
      >
        Recipe List
      </h3>
    </div>
    <RecipeItem :recipesList="recipesList" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from "vue";
import RecipeItem from "./RecipeItem.vue";

let recipesList = ref([]);
const isLoading = ref(true);

export default defineComponent({
  name: "RecipeList",
  components: { RecipeItem },
  setup() {
    onMounted(async () => {
      // fetch recipes and passes it down to RecipeItem child component
      try {
        const response = await fetch("http://localhost:8000/recipes/");
        if (!response.ok) throw new Error("Failed to fetch");
        const data = await response.json();
        recipesList.value = data;
        isLoading.value = false;
      } catch (err) {
        isLoading.value = true;
        console.log(err);
      }
    });

    return { recipesList, isLoading };
  },
});
</script>

<style></style>
