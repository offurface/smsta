<template>
  <v-col xs="11" sm="7" md="6" lg="5">
    <v-card class="pa-6">
      <v-form @submit.prevent="handleSubmit">
        <v-card-text>
          <v-text-field
            id="inputLogin"
            type="text"
            v-model.trim="username"
            :label="$t('user_name')"
            prepend-icon="mdi-account"
          />

          <v-text-field
            id="inputPass"
            type="password"
            v-model.trim="password"
            :label="$t('password')"
            prepend-icon="mdi-lock"
          />
        </v-card-text>
        <v-card-actions class>
          <v-btn
            class="blcok"
            @click.stop="handleSubmit()"
            outlined
            x-large
            dark
            block
          >{{ $t('login') }}</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-col>
</template>

<script>
export default {
  layout: 'empty',
  metaInfo() {
    const { appName } = window.config

    return {
      title: appName,
      titleTemplate: null
    }
  },
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    handleSubmit(e) {
      const { username, password } = this
      console.log({ username, password })
      const { dispatch } = this.$store
      if (username && password) {
        dispatch('auth/login', { username, password })
          .then(response => {
            const next = this.$route.query.next || '/home'
            this.$router.push(next)
          })
          .catch(error => {
            console.log('ssd', error)
          })
      }
    }
  }
}
</script>
