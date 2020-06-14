<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row >
          <v-col :cols="12">
            <h1 class="display-2">Домашняя страница</h1>
          </v-col>
          <v-col :cols="12" :sm="8" :md="3">
            <v-sheet class="pa-3">
              <div
                class="profile__photo mb-4"
                style="background-image: url('https://pbs.twimg.com/media/DeBT14ZV0AATTcE.jpg')"
              ></div>
              <h3 class="text-center">
                {{ user.last_name }} {{ user.first_name }} {{ user.patronymic }}
              </h3>
            </v-sheet>
          </v-col>
          <v-col :cols="12" :sm="8" :md="9">
            <v-sheet class="pa-5" height="100%">
              <h3 class="mb-3">Информация о пользователе:</h3>
              <v-simple-table>
                <template>
                  <tbody>
                    <tr>
                      <td>Уровень доступа:</td>
                      <td>{{ role.name }}</td>
                    </tr>
                    <tr>
                      <td>Должность сотрудника:</td>
                      <td>{{ user.employe_position }}</td>
                    </tr>
                    <tr>
                      <td>Номер телефона:</td>
                      <td>{{ user.phone }}</td>
                    </tr>
                    <tr>
                      <td>Электронная почта:</td>
                      <td>{{ user.email }}</td>
                    </tr>
                  </tbody>
                </template>
              </v-simple-table>
            </v-sheet>
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
    data() {
      return {
        role: null
      }
    },
    middleware: auth,
    props: {
      source: String
    },
    computed: {
      ...mapGetters('auth', ['user']),
      ...mapGetters('interface', ['getRole'])
    },
    mounted() {
      this.role = this.getRole(this.user.role)
    }
  }
</script>
