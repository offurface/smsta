<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
<<<<<<< HEAD
          <v-col>
            <v-btn @click="logger()">log</v-btn>
          </v-col>
=======
          <v-col> </v-col>
>>>>>>> 67a21e0101656c73c91ce74090c78357c1a279d4
          <v-col v-for="group in groups" :key="group.id">{{
            group.name
          }}</v-col>
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
<<<<<<< HEAD
    methods: {
      logger() {
        console.log(this.groups)
      }
    },
=======
    methods: {},
>>>>>>> 67a21e0101656c73c91ce74090c78357c1a279d4
    computed: {
      ...mapGetters('groups', ['groups'])
    },
    created() {
      this.$store.dispatch('groups/loadGroups')
<<<<<<< HEAD
      console.log('created')
=======
>>>>>>> 67a21e0101656c73c91ce74090c78357c1a279d4
    }
  }
</script>
