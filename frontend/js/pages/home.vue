<template>
  <example color="#01bf9e" :show-links="true">
    Welcome to SPA application
  </example>
</template>

<script>
  export default {
    metaInfo() {
      const { appName } = window.config

      return {
        title: appName,
        titleTemplate: null
      }
    }
  }
</script>
