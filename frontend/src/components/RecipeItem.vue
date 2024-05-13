<template>
  <div>
    <div class="text-black-200" v-if="isLoading">Loading...</div>
    <div v-else>
      <div v-for="recipe in recipesList.recipes" :key="recipe">
        <div
          class="m-auto my-2 grid grid-cols-2 max-w-7xl rounded overflow-hidden bg-white p-s border-2 border-black"
        >
          <div class="px-4 py-2 content-center">
            <div class="font-bold text-xl mb-2">{{ recipe.title }}</div>
            <p class="text-gray-700 text-base mb-4">
              <span class="font-bold">Description:</span>
              {{ recipe.description }}
            </p>
            <p class="text-gray-700 text-base mb-4">
              <span class="font-bold">Instructions:</span>
              {{ recipe.instructions }}
            </p>
            <p class="text-gray-700 text-base mb-4">
              <span class="font-bold">Cooking Time:</span>
              {{ recipe.cooking_time }} |
              <span class="font-bold">Total Time:</span>
              {{ recipe.total_time }}
            </p>
            <p class="text-gray-700 text-base mb-4">
              <span class="font-bold">Difficulty Level:</span>
              {{ recipe.difficulty_level }}
            </p>
          </div>

          <div class="m-2 bg-pink-300 rounded-lg overflow-hidden shadow-md">
            <span @click="handleDeleteClick(recipe.id)" class="bin-icon"
              ><i class="gg-trash float-right m-2"></i
            ></span>

            <div class="px-6 py-4">
              <div
                class="font-bold text-xl mb-4 text-gray-700 border-b-2 border-black"
              >
                Recipe Ingredients
              </div>

              <div
                v-for="ingredientList in recipe.recipe_ingredients"
                :key="ingredientList"
              >
                <div class="bg-white rounded-lg p-3 mb-4">
                  <p class="text-gray-700 font-semibold mb-1">
                    Ingredient: {{ ingredientList.ingredient.name }}
                  </p>
                  <p class="text-gray-700 mb-1">
                    Category: {{ ingredientList.ingredient.category }}
                  </p>
                  <p class="text-gray-700">
                    Measurements: {{ ingredientList.quantity }}
                    {{ ingredientList.measurement_unit }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

async function deleteRecipe(recipeId: number) {
  try {
    const url = `http://localhost:8000/recipes/${recipeId}`;
    const response = await fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    });

    if (!response.ok) {
      throw new Error("Failed to delete the recipe");
    } else {
      location.reload();
    }
  } catch (error) {
    console.error("Error deleting the recipe:", error);
  }
}

export default defineComponent({
  name: "RecipeItem",
  props: {
    recipesList: Object,
  },
  methods: {
    handleDeleteClick(recipeId: number) {
      deleteRecipe(recipeId);
    },
  },
});
</script>

<style></style>
