<template>
  <div class="m-2">
    <router-link v-if="noReload" :to="{ name: url }" class="text-light text-nowrap">
      <i :class="icon"></i>
      {{ name }}
    </router-link>
    <a v-else class="text-light text-nowrap" target="_blank" :href="url">
      <i :class="icon"></i>
      {{ name }}
    </a>
  </div>
</template>

<script>
export default {
  name: 'example-link',
  props: ['icon', 'name', 'url', 'noReload']
}
</script>
