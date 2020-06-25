<template>
  <v-app id="inspire">
    <!-- Navbar start -->
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Дневник тьютора</v-toolbar-title>
      <v-spacer></v-spacer>
      <h4 class="body-1 mr-3">
        {{ user.username }}
      </h4>
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn v-on="on" fab small>
            <v-icon>mdi-account</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item link>
            <v-list-item-title>
              Личный кабинет
            </v-list-item-title>
          </v-list-item>
          <v-list-item link>
            <v-list-item-title @click="logout()">
              Выход
            </v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
    <!-- Navbar end -->

    <!-- Sidebar start -->
    <v-navigation-drawer :clipped="true" v-model="drawer" fixed temporary app>
      <v-list v-for="(category, i) in sidebar" :key="i" dense>
        <v-subheader>{{ category.name }}</v-subheader>
        <v-list-item
          v-for="(link, j) in category.items"
          :key="j"
          link
          :to="link.to"
        >
          <v-list-item-action>
            <v-icon>{{ link.icon }}</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>{{ link.name }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link @click="logout()">
          <v-list-item-action>
            <v-icon>mdi-account-cancel</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Выход</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!-- Sidebar end -->

    <!-- Content start -->
    <v-content transition="slide-x-transition">
      <child></child>
    </v-content>
    <!-- Content end -->

    <!-- Footer start -->
    <!-- <v-footer app>
      <span></span>
    </v-footer> -->
    <!-- Footer end -->
  </v-app>
</template>

<script>
  import { mapGetters } from 'vuex'
  export default {
    name: 'MainLayout',
    data() {
      return {
        drawer: null
      }
    },
    computed: {
      ...mapGetters('interface', ['sidebar']),
      ...mapGetters('auth', ['user'])
    },
    methods: {
      logout() {
        const { dispatch } = this.$store
        dispatch('auth/logout')
          .then(response => {
            this.$router.push('/')
          })
          .catch(error => {
            console.log('ssd', error)
          })
      }
    }
  }
</script>
