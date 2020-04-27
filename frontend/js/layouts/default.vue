<template>
  <v-app id="inspire">
    <!-- Navbar start -->
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mx-2" @click="logout()" fab dark small color="pink">
        <v-icon dark>mdi-account-cancel</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- Navbar end -->

    <!-- Sidebar start -->
    <v-navigation-drawer
      :clipped="true"
      v-model="drawer"
      absolute
      temporary
      app
    >
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
      </v-list>
    </v-navigation-drawer>
    <!-- Sidebar end -->

    <!-- Content start -->
    <v-content transition="slide-x-transition">
      <child></child>
    </v-content>
    <!-- Content end -->

    <!-- Footer start -->
    <v-footer app>
      <span></span>
    </v-footer>
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
      ...mapGetters('interface', ['sidebar'])
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
