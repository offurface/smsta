<template>
  <div class="batman">
    <div class="row min-vh-100 py-4 align-items-center">
      <div class="col-12 text-center">
        <div class="batman__animate">
          <img class="batman__logo" src="/static/images/batman.png" alt="logo" />
          <img
            class="batman__wheel batman__wheel--back"
            src="/static/images/back_wheel.png"
            alt="back wheel"
          />
          <img
            class="batman__wheel batman__wheel--front"
            src="/static/images/front_wheel.png"
            alt="front wheel"
          />
        </div>
        <div :style="{ color: color }">
          <h3>
            <div class="d-inline-block pb-2" :style="{ 'border-bottom': `1px solid ${color}` }">
              <i class="ic ic-batman"></i>
              <slot></slot>
            </div>
          </h3>
          <div v-if="showLinks" class="batman__links m-auto">
            <div v-for="category in getCategory" :key="category.name">
              <h6 class="mt-3">
                <b>{{ category.name }}:</b>
              </h6>
              <div class="d-flex flex-wrap justify-content-center">
                <item
                  v-for="item in category.items"
                  :key="item.name"
                  :icon="item.icon"
                  :name="item.name"
                  :url="item.url"
                  :no-reload="item.noReload"
                />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Link from './Link'

export default {
  components: {
    item: Link
  },
  props: {
    color: {
      type: String,
      default: 'white'
    },
    showLinks: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    getCategory: function() {
      return this.$store.getters['links/items']
    }
  }
}
</script>

<style lang="sass" scoped>
@keyframes flame-animation
  100%
    border-top-width: 1.9em
    border-left-width: .5em
    border-left-width: .5em

  @keyframes spin
    0%
      transform: rotate(0deg)
    100%
      transform: rotate(360deg)
  .ic
    vertical-align: bottom
    font-size: 1.5rem
  .batman
    &__links
      max-width: 750px
    &__logo
      width: 290px
    &__wheel
      position: absolute
      bottom: -0.4rem
      animation: spin 0.4s linear infinite
      &--back
        left: 3.45rem
        width: 51px
      &--front
        right: 2.43rem
        width: 46px
    &__animate
      display: inline-block
      position: relative
      margin-bottom: 10px
      &:before
        border-left: .65rem solid transparent
        border-right: .65rem solid transparent
        border-top: 1.75rem solid $batman-fire-color
        content: ""
        display: inline-block
        height: .5rem
        left: 6%
        position: absolute
        bottom: 0.1rem
        transform: rotate(90deg)
        z-index: 6
        animation: flame-animation 0.2s linear infinite
</style>
