<template>
  <div>
    <example>
      {{ $t('page_not_found') }}
    </example>
  </div>
</template>

<script>
  export default {
    metaInfo() {
      return {
        title: this.$t('page_not_found')
      }
    }
  }
</script>
