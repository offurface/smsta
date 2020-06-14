<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid v-if="!loading">
        <v-row>
          <v-col>
            <preloader></preloader>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid v-else>
        <v-row justify="center">
          <v-col cols="8" sm="8">
            <v-card>
              <v-card-text>
                <h2 class="display-1">{{ group.name }}</h2>
                <v-simple-table>
                  <template>
                    <tbody>
                      <tr>
                        <td>Кафедра:</td>
                        <td>
                          {{ group.department.full_name }} ({{
                            group.department.short_name
                          }})
                        </td>
                      </tr>
                      <tr>
                        <td>Тьютор:</td>
                        <td>Иванов Иван Иванович</td>
                      </tr>
                      <tr>
                        <td>Количество студентов:</td>
                        <td>{{ group.students.length }}</td>
                      </tr>
                    </tbody>
                  </template>
                </v-simple-table>
                <v-card-actions>
                  <v-btn @click="getGroupListDocument()">
                    Выгрузка документов
                  </v-btn>
                </v-card-actions>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col cols="8" sm="8">
            <v-card>
              <v-card-text>
                <h3 class>Список студентов:</h3>
                <v-list dense>
                  <v-list-item
                    v-for="student in group.students"
                    :key="student.pk"
                    link
                    :to="{
                      name: 'students-detail',
                      params: {
                        pkStudent: student.pk
                      }
                    }"
                  >
                    <v-list-item-icon>
                      <v-icon v-if="student.gender != 1">mdi-face</v-icon>
                      <v-icon v-else>mdi-face-woman</v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title
                        >{{ student.surname }} {{ student.name }}
                        {{ student.patronymic }}</v-list-item-title
                      >
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
        const pk = this.$route.params.pkGroup
        this.$store.dispatch('documents/groupCard', { pk })
      },
      getGroupListDocument() {
        this.$store.dispatch('documents/groupListDocument')
      }
    },
    computed: {
      ...mapGetters('groups', ['group'])
    },
    mounted() {
      const pk = this.$route.params.pkGroup
      this.$store
        .dispatch('groups/loadGroup', { pk })
        .then(() => (this.loading = true))
    }
  }
</script>
