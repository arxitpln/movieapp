<script setup>
import { RouterLink, RouterView } from 'vue-router'
import './assets/App.css'
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="@/assets/icons/logo.svg"/>
    <nav>
      <RouterLink to="/">Home</RouterLink>
    </nav>
  </header>

  <RouterView />
</template>