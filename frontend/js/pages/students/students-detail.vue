<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid v-if="!loading">
        <v-row align="center" justify="center">
          <v-col>
            <preloader></preloader>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid v-else>
        <!-- <v-row justify="center">
          <v-col cols="8" sm="8">
            <v-card>{{ student }}</v-card>
          </v-col>
        </v-row> -->
        <v-row>
          <v-col>
            <student-retrive :student="student"></student-retrive>
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
    data() {
      return {
        loading: false
      }
    },
    methods: {},
    computed: {
      ...mapGetters('students', ['student'])
    },
    mounted() {
      const pk = this.$route.params.pkStudent
      this.$store
        .dispatch('students/loadStudent', { pk })
        .then(() => (this.loading = true))
    }
  }
</script>
