<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col>
            <h1>Profile {{ user['username'] }}</h1>
            <p>{{ user }}</p>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
  import auth from '@/middleware/auth'
  import { mapGetters } from 'vuex'
  export default {
    middleware: auth,
    props: {
      source: String
    },
    computed: {
      ...mapGetters('auth', ['user'])
    }
  }
</script>
