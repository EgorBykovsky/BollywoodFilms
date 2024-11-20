<script setup lang="ts">
import { ref } from 'vue';
import axios from 'axios';

const searchQuery = ref('');
const searchQuery2 = ref('');
const results = ref<string[]>([]);
const results_top = ref<string[]>([]);
const results_overview = ref<string[]>([]);
const showTopResults = ref(false);  

const search = async () => {
  if (searchQuery.value.trim()) {
    try {
      const response = await axios.post('http://localhost:8000/top10_genres', {
        title: searchQuery.value, 
      });
      results.value = response.data.top_10_genres;
    } catch (error) {
      console.error("Ошибка при поиске:", error);
    }
  } else {
    results.value = []; 
  }
};

const search2 = async () => {
  if (searchQuery2.value.trim()) {
    try {
      const response = await axios.post('http://localhost:8000/top10_overview', {
        title: searchQuery2.value, 
      });
      results_overview.value = response.data.top_10_overview;
    } catch (error) {
      console.error("Ошибка при поиске:", error);
    }
  } else {
    results_overview.value = []; 
  }
};

const top = async () => {
  try {
    const response = await axios.post('http://localhost:8000/top10');
    results_top.value = response.data.top_10;
    showTopResults.value = true; 
  } catch (error) {
    console.error("Ошибка при получении топ-10:", error);
  }
};

const clearTop = () => {
  showTopResults.value = false;  
};

const clear = () => {
  results.value = [];
  results_overview.value = [];};
</script>

<template>
  <main class="container">
    <div class="column">
      <div class="search-box">
        <button class="btn-search"><i class="fas fa-search"></i></button>
        <input 
          v-model="searchQuery" 
          @keyup.enter="search" 
          @input="clear"
          type="text" 
          class="input-search" 
          placeholder="Film to Search..."
        />
      </div>
      <div v-if="searchQuery.trim() && results.length" class="results">
        <ul>
          <li v-for="(movie, index) in results" :key="index">
            <strong>{{ movie[0] }}</strong>: {{ movie[1] }}
          </li>
        </ul>
      </div>
    </div>

    <div class="column-center">
      <button class="button-top" @click="top">Получить топ 10</button>
      <button v-if="showTopResults" class="button-top hide" @click="clearTop">Скрыть топ 10</button>
      
      <ul v-if="showTopResults && results_top.length">
        <li v-for="(movie, index) in results_top" :key="index">
          {{ movie }}
        </li>
      </ul>
    </div>

    <div class="column">
      <div class="search-box">
        <button class="btn-search"><i class="fas fa-search"></i></button>
        <input 
          v-model="searchQuery2" 
          @keyup.enter="search2" 
          @input="clear"
          type="text" 
          class="input-search" 
          placeholder="Film to Search..."
        />
      </div>
      <div v-if="searchQuery2.trim() && results_overview.length" class="results">
        <ul>
          <li v-for="(movie, index) in results_overview" :key="index">
            <strong>{{ movie[0] }}</strong>: {{ movie[1] }}
          </li>
        </ul>
      </div>
    </div>
  </main>
</template>
