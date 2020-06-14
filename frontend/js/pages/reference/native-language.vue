<template>
  <v-app id="inspire">
    <v-content>
      <v-container fluid v-if="!loading">
        <v-row align="center" justify="center">
          <v-col>
            <preloader></preloader>
          </v-col>
        </v-row>
      </v-container>
      <v-container fluid v-else>
        <v-row>
          <v-col>
            <h1>
              Справочник языков
              <v-menu offset-y>
                <template v-slot:activator="{ on }">
                  <v-btn dark v-on="on" fab small>
                    <v-icon dark>mdi-plus</v-icon>
                  </v-btn>
                </template>
                <v-list>
                  <v-list-item @click="dialogPost = true" link>
                    <v-list-item-title>
                      Добавить запись
                    </v-list-item-title>
                  </v-list-item>
                </v-list>
              </v-menu>
            </h1>
          </v-col>
        </v-row>

        <v-row v-if="nativeLanguages.length == 0" justify="center">
          <v-col cols="8" sm="8">
            <v-card class="py-6 px-4 text-center">
              <h2 class="display-1">В справочнике нет записей</h2>
            </v-card>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col>
            <v-list dense>
              <v-list-item
                v-for="(item, index) in nativeLanguages"
                link
                @click="loadPut(item)"
                :key="item.pk"
              >
                <v-list-item-content>
                  <v-list-item-title>
                    {{ ++index }}. {{ item.name }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="8" sm="8">
            <v-dialog v-model="dialogPost">
              <v-card>
                <v-card-title class="headline">
                  Добавить запись "Родной язык"
                </v-card-title>

                <v-card-text>
                  <v-text-field
                    v-model="emptyObject.name"
                    :counter="50"
                    name="name"
                    label="Наименование"
                    required
                  ></v-text-field>
                  {{ emptyObject }}
                </v-card-text>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="green darken-2" @click="objectPost()">
                    Добавить
                  </v-btn>
                  <v-btn color="red darken-2" @click="dialogPost = false">
                    Отмена
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
            <v-dialog v-if="nativeLanguage" v-model="dialogPut">
              <v-card>
                <v-card-title class="headline">
                  Обновить запись "Родной язык"
                </v-card-title>
                <v-card-text>
                  <v-text-field
                    v-model="nativeLanguage.name"
                    :counter="50"
                    name="name"
                    label="Наименование"
                    required
                  ></v-text-field>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="green darken-1" text @click="objectPut()">
                    Обновить
                  </v-btn>
                  <v-btn
                    color="yellow darken-1"
                    text
                    @click="dialogPut = false"
                  >
                    Отмена
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
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
        dialogPost: false,
        dialogPut: false,
        loading: false,
        nativeLanguage: null,
        emptyObject: {
          name: ''
        }
      }
    },
    methods: {
      objectPost() {
        const nativeLanguage = this.emptyObject
        if (nativeLanguage.name.trim() !== '') {
          this.$store
            .dispatch('reference/postNativeLanguage', { nativeLanguage })
            .then(() => {
              this.dialogPost = false
              this.emptyObject.name = ''
            })
        }
      },
      loadPut(nativeLanguage) {
        this.dialogPut = true
        this.nativeLanguage = nativeLanguage
      },
      objectPut() {
        const nativeLanguage = this.nativeLanguage
        const pk = this.nativeLanguage.id
        if (nativeLanguage.name.trim() !== '') {
          this.$store
            .dispatch('reference/putNativeLanguage', { pk, nativeLanguage })
            .then(() => (this.dialogPut = false))
        }
      }
    },
    computed: {
      ...mapGetters('reference', ['nativeLanguages'])
    },
    mounted() {
      this.$store
        .dispatch('reference/loadNativeLanguages')
        .then(() => (this.loading = true))
    }
  }
</script>
