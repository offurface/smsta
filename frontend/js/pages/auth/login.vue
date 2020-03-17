<template>
  <div class="login row min-vh-100 align-items-center justify-content-center">
    <form
      class="col-12 col-md-8 col-lg-6 text-center"
      @submit.prevent="handleSubmit"
    >
      <img class="login__logo my-4" src="/static/images/logo.png" />
      <div class="form-group">
        <label class="login__label" for="inputLogin">
          {{ $t('user_name') }}
        </label>
        <input
          id="inputLogin"
          class="login__input form-control"
          type="text"
          v-model.trim="username"
          :placeholder="$t('user_name')"
        />
      </div>
      <div class="form-group">
        <label class="login__label" for="inputPass">
          {{ $t('password') }}
        </label>
        <input
          id="inputPass"
          class="login__input form-control"
          type="password"
          v-model.trim="password"
          :placeholder="$t('password')"
        />
      </div>
      <button class="login__btn btn btn-primary px-5" type="submit">
        {{ $t('login') }}
      </button>
    </form>
  </div>
</template>

<script>
  export default {
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
        const { dispatch } = this.$store
        if (username && password) {
          dispatch('auth/login', { username, password })
            .then(response => {
              const next = this.$route.query.next || '/'
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
