<template>
  <div>
    <h1>{{ $t('page_not_found') }}</h1>
  </div>
</template>

<script>
export default {
  layout: 'empty',
  metaInfo() {
    return {
      title: this.$t('page_not_found')
    }
  }
}
</script>
