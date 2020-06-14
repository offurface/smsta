<template>
  <v-app id="inspire">
    <v-content>
      <v-container v-if="!loading">
        <v-row align="center" justify="center">
          <v-col>
            <preloader></preloader>
          </v-col>
        </v-row>
      </v-container>
      <v-container v-else fluid>
        <v-row>
          <v-col>
            <h1>Список групп</h1>
          </v-col>
        </v-row>
        <v-row align="center" justify="center">
          <v-col cols="12" md="8">
            <v-text-field
              v-model="searchString"
              prepend-inner-icon="mdi-magnify"
              label="Поиск"
              hide-details="auto"
              solo
            ></v-text-field>
            <v-checkbox
              v-model="searchAll"
              label="Искать по всем группам"
              hide-details="auto"
            ></v-checkbox>
          </v-col>
          <v-col cols="12" md="8">
            <v-list
              dense
              v-if="searchGroups(searchString, searchAll).length !== 0"
            >
              <v-list-item
                v-for="group in searchGroups(searchString, searchAll)"
                :key="group.pk"
                link
                :to="{ name: 'groups-detail', params: { pkGroup: group.pk } }"
              >
                <v-list-item-content>
                  <v-list-item-title>
                    {{ group.name }}, {{ group.department.short_name }},
                    {{ group.start_date }}, {{ group.course }}
                  </v-list-item-title>
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
    data() {
      return {
        loading: false,
        searchString: '',
        searchAll: false
      }
    },
    props: {
      source: String
    },
    methods: {},
    computed: {
      ...mapGetters('groups', ['groups', 'searchGroups'])
    },
    created() {
      this.$store
        .dispatch('groups/loadGroups')
        .then(() => (this.loading = true))
    }
  }
</script>
