<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid>
        <v-row align="center" justify="center">
          <v-col>
            <h1>Test</h1>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veniam, asperiores error commodi placeat neque fugit perferendis consectetur repudiandae earum alias magni labore quas sint laborum blanditiis distinctio culpa odit. Doloremque?Lorem ipsum dolor sit, amet consectetur adipisicing elit. Illo, harum deleniti ab quod ipsam numquam obcaecati, illum optio adipisci neque aliquid deserunt, aperiam rerum atque repellendus repellat quam esse? Error?
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import auth from '@/middleware/auth'
export default {
  middleware: auth,
  props: {
    source: String
  },
  created() {}
}
</script>
