<template>
  <v-col cols="12" sm="6" md="4">
    <v-card @click="$emit('click')">
      <v-card-title>{{ movie.title }}</v-card-title>
      <v-card-text>{{ movie.description }}</v-card-text>
    </v-card>
  </v-col>
</template>

<script setup>
defineProps(['movie']);
</script>
