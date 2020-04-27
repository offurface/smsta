<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col>
            <v-btn @click="logger()">log</v-btn>
          </v-col>
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
    methods: {
      logger() {
        console.log(this.groups)
      }
    },
    computed: {
      ...mapGetters('groups', ['groups'])
    },
    created() {
      this.$store.dispatch('groups/loadGroups')
      console.log('created')
    }
  }
</script>
