<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row justify="center">
          <v-col>
            <h1>Домашняя страница</h1>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import auth from '@/middleware/auth'
  export default {
    middleware: auth,
    props: {
      source: String
    },
    created() {}
  }
</script>
