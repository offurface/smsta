<template>
  <v-app id="inspire">
    <!-- Navbar start -->
    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />
      <v-toolbar-title>Application</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn class="mx-2" @click="logout()" fab dark small color="pink">
        <v-icon dark>mdi-account-cancel</v-icon>
      </v-btn>
    </v-app-bar>
    <!-- Navbar end -->

    <!-- Sidebar start -->
    <v-navigation-drawer v-model="drawer" app>
      <v-list dense>
        <v-list-item link to="/profile">
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Profile</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/home">
          <v-list-item-action>
            <v-icon>mdi-view-dashboard</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link to="/test">
          <v-list-item-action>
            <v-icon>mdi-settings</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Test</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <!-- Sidebar end -->

    <!-- Content start -->
    <v-content transition="scroll-x-transition">
      <child></child>
    </v-content>
    <!-- Content end -->

    <!-- Footer start -->
    <v-footer app>
      <span>&copy; 2019</span>
    </v-footer>
    <!-- Footer end -->
  </v-app>
</template>

<script>
export default {
  name: 'MainLayout',
  data() {
    return {
      drawer: null
    }
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
