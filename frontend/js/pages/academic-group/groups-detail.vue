<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row v-if="!loading" align="center" justify="center">
          <v-col>
            <preloader></preloader>
          </v-col>
        </v-row>
        <v-row v-else justify="center">
          <v-col cols="12" sm="8" md="6">
            <v-card>
              <v-card-text>
                <h2 class="display-1">{{ group.name }}</h2>
                <p>{{ group.students.length }}</p>
                <v-card-actions>
                  <v-btn @click="getGroupCard()">Анализ контингента группы</v-btn>
                </v-card-actions>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="12" sm="8" md="6">
            <v-card>
              <v-card-text>
                <h3 class>Список студентов:</h3>
                <v-list dense>
                  <v-list-item v-for="student in group.students" :key="student.pk" link>
                    <v-list-item-icon>
                      <v-icon v-if="student.gender == 1">mdi-face</v-icon>
                      <v-icon v-else>mdi-face-woman</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title>{{ student.surname }} {{ student.name }} {{ student.patronymic }}</v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </v-card-text>
            </v-card>
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
  methods: {
    getGroupCard() {
      const pk = this.$route.params.pk
      this.$store.dispatch('documents/groupCard', { pk })
    }
  },
  computed: {
    ...mapGetters('groups', ['group'])
  },
  mounted() {
    const pk = this.$route.params.pk
    this.$store
      .dispatch('groups/loadGroup', { pk })
      .then(() => (this.loading = true))
  }
}
</script>
