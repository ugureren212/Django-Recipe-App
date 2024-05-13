<template>
  <form
    @submit="submitForm"
    class="max-w-xl mx-auto p-4 m-4 rounded-lg bg-white"
  >
    <!--Main Forum Section -->
    <h3
      class="text-center mb-4 text-2xl font-extrabold leading-none tracking-tight text-gray-900 md:text-3xl lg:text-4xl dark:text-white"
    >
      Forum Content
    </h3>

    <div>
      <label for="title" class="block text-sm font-medium text-black"
        >Title:</label
      >
      <input
        type="text"
        id="title"
        name="title"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        v-model="recipeDetailData.title"
        required
      />
    </div>

    <div class="mt-4">
      <label for="description" class="block text-sm font-medium text-black"
        >Description:</label
      >
      <textarea
        id="description"
        name="description"
        rows="3"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        v-model="recipeDetailData.description"
        required
      ></textarea>
    </div>

    <div class="mt-4">
      <label for="instructions" class="block text-sm font-medium text-black"
        >Instructions:</label
      >
      <textarea
        id="instructions"
        name="instructions"
        rows="4"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        v-model="recipeDetailData.instructions"
        required
      ></textarea>
    </div>

    <div class="mt-4">
      <label for="cooking_time" class="block text-sm font-medium text-black"
        >Cooking Time:</label
      >
      <input
        type="text"
        id="cooking_time"
        name="cooking_time"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        v-model="recipeDetailData.cooking_time"
        required
      />
    </div>

    <div class="mt-4">
      <label for="total_time" class="block text-sm font-medium text-black"
        >Total Time:</label
      >
      <input
        type="text"
        id="total_time"
        name="total_time"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        v-model="recipeDetailData.total_time"
        required
      />
    </div>

    <div class="mt-4">
      <label for="difficulty_level" class="block text-sm font-medium text-black"
        >Difficulty Level:</label
      >
      <select
        id="difficulty_level"
        name="difficulty_level"
        class="mt-1 p-2 border border-black rounded-md w-full focus:outline-none focus:ring focus:ring-pink-500"
        required
      >
        <option value="Easy">Easy</option>
        <option value="Medium">Medium</option>
        <option value="Hard">Hard</option>
      </select>
    </div>
    <br />
    <div class="mt-4">
      <label
        for="recipe_ingredients"
        class="block text-l font-medium text-black"
        >Recipe Ingredients:</label
      >
    </div>

    <!--Ingrediant Section -->
    <div class="mt-4">
      <label for="ingredient" class="block text-sm font-medium text-black"
        >Ingredients:</label
      >
      <div>
        <div
          v-for="(ingredient, index) in ingredientsData.recipe_ingredients"
          :key="index"
          class="grid grid-cols-2 gap-4"
        >
          <div class="border border-gray-200 p-2 rounded-md">
            <label>Ingredient Name:</label>
            <input
              v-model="
                ingredientsData.recipe_ingredients[index].ingredient.name
              "
              type="text"
              class="mt-1 p-2 border border-black rounded-md focus:outline-none focus:ring focus:ring-pink-500"
              required
            />
          </div>
          <div class="border border-gray-200 p-2 rounded-md">
            <label>Category:</label>
            <input
              v-model="
                ingredientsData.recipe_ingredients[index].ingredient.category
              "
              type="text"
              class="mt-1 p-2 border border-black rounded-md focus:outline-none focus:ring focus:ring-pink-500"
              required
            />
          </div>
          <div class="border border-gray-200 p-2 rounded-md">
            <label>Quantity:</label>
            <input
              v-model="ingredientsData.recipe_ingredients[index].quantity"
              type="number"
              step="0.01"
              class="mt-1 p-2 border border-black rounded-md focus:outline-none focus:ring focus:ring-pink-500"
              required
            />
          </div>
          <div class="border border-gray-200 p-2 rounded-md">
            <label>Measurement Unit:</label>
            <input
              v-model="
                ingredientsData.recipe_ingredients[index].measurement_unit
              "
              type="text"
              class="mt-1 p-2 border border-black rounded-md focus:outline-none focus:ring focus:ring-pink-500"
              required
            />
          </div>
        </div>
      </div>
      <button
        type="button"
        @click="addIngredientField"
        class="mt-2 py-1 px-3 bg-pink-500 text-white rounded-md hover:bg-pink-600"
      >
        Add Ingredient
      </button>
    </div>

    <div class="mt-4">
      <button
        type="submit"
        class="py-2 px-4 bg-pink-500 text-white rounded-md hover:bg-pink-600"
      >
        Submit
      </button>
    </div>
  </form>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    // setting default form values
    const recipeDetailData = ref({
      id: 0,
      title: "Lemon Cake",
      description: "A light and refreshing lemon cake.",
      instructions: "Mix all ingredients and bake at 180°C for 45 minutes.",
      cooking_time: "00:45:00",
      total_time: "01:30:00",
      difficulty_level: "Medium",
    });
    // setting default ingredients values
    const ingredientsData = ref({
      recipe_ingredients: [
        {
          ingredient: { name: "Lemon", category: "Fruit" },
          quantity: 3,
          measurement_unit: "pieces",
        },
      ],
    });

    // creates new ingredients field
    const addIngredientField = () => {
      ingredientsData.value.recipe_ingredients.push({
        ingredient: { name: "", category: "" },
        quantity: null,
        measurement_unit: "",
      });
    };

    const submitForm = () => {
      // combines recipe details and ingredients details
      const recipeData = {
        id: Math.floor(Math.random() * 1000) + 1,
        title: recipeDetailData.value.title,
        description: recipeDetailData.value.description,
        instructions: recipeDetailData.value.instructions,
        cooking_time: recipeDetailData.value.cooking_time,
        total_time: recipeDetailData.value.total_time,
        difficulty_level: recipeDetailData.value.difficulty_level,
        ...ingredientsData.value,
      };

      fetch("http://localhost:8000/recipes/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(recipeData),
      })
        .then((response) => {
          if (response.ok) {
            console.log("Recipe data sent successfully");
          } else {
            console.error("Failed to send recipe data");
          }
        })
        .catch((error) => {
          console.error("Error:", error);
        });
    };

    return {
      ingredientsData,
      recipeDetailData,
      addIngredientField,
      submitForm,
    };
  },
};
</script>

<style></style>
