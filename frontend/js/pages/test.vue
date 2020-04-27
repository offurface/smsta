<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col> </v-col>
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
    methods: {},
    computed: {
      ...mapGetters('groups', ['groups'])
    },
    created() {
      this.$store.dispatch('groups/loadGroups')
    }
  }
</script>
