<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row>
          <v-col>
            <h1>Список групп:</h1>
          </v-col>
        </v-row>
        <v-row align="center" justify="center">
          <v-col>
            <v-list dense>
              <v-list-item
                v-for="group in groups"
                :key="group.pk"
                link
                :to="{ name: 'groups-detail', params: { pk: group.pk } }"
              >
                <v-list-item-content>
                  <v-list-item-title>{{ group.name }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
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
    methods: {},
    computed: {
      ...mapGetters('groups', ['groups'])
    },
    created() {
      this.$store.dispatch('groups/loadGroups')
    }
  }
</script>
