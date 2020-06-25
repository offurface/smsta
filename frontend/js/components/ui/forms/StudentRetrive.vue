<template>
  <v-card class="overflow-hidden" color="lighten-3">
    <v-toolbar flat>
      <v-icon class="mr-2">mdi-account</v-icon>
      <v-toolbar-title class="font-weight-light">
        Информация о студенте
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn color="yellow" fab small @click="isEditing = !isEditing">
        <v-icon v-if="isEditing">mdi-close</v-icon>
        <v-icon v-else>mdi-pencil</v-icon>
      </v-btn>
    </v-toolbar>
    <v-card-text>
      <v-form ref="form">
        <v-tabs v-model="tab" class="mb-4">
          <v-tab>
            Основное
          </v-tab>
          <v-tab>
            Социальный статус
          </v-tab>
          <v-tab>
            Родители
          </v-tab>
        </v-tabs>
        <v-tabs-items v-model="tab">
          <v-tab-item>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.surname"
              :counter="50"
              name="surname"
              label="Фамилия"
              required
            ></v-text-field>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.name"
              :counter="50"
              name="name"
              label="Имя"
              required
            ></v-text-field>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.patronymic"
              :counter="50"
              name="patronymic"
              label="Отчество"
              required
            ></v-text-field>
            <v-select
              :disabled="!isEditing"
              v-model="student.gender"
              :items="gender"
              item-value="id"
              item-text="name"
              label="Пол"
            ></v-select>
            <v-select
              :disabled="!isEditing"
              v-model="student.payment_training"
              :items="paymentTraining"
              item-value="id"
              item-text="name"
              label="Способ финасирования"
            ></v-select>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.birth_place"
              :counter="255"
              name="birth_place"
              label="Место рождения"
              required
            ></v-text-field>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.address"
              :counter="255"
              name="address"
              label="Адрес по прописке"
              required
            ></v-text-field>
            <v-text-field
              :disabled="!isEditing"
              v-model="student.address_fact"
              :counter="255"
              name="address_fact"
              label="Адрес фактический"
              required
            ></v-text-field>
            <v-select
              :disabled="!isEditing"
              v-model="student.disability_group"
              :items="disabilityGroup"
              item-value="id"
              item-text="name"
              label="Форма инвалидности"
            ></v-select>
            <v-select
              :disabled="!isEditing"
              v-model="student.active_group"
              :items="activeGroup"
              item-value="id"
              item-text="name"
              label="Актив группы"
            ></v-select>
          </v-tab-item>
          <v-tab-item>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_orphan"
              label="Студенты-сироты и студенты, оставшихся без попечения родителей"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_military"
              label="Студенты-ветераны и инвалиды боевых действий"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_radioactive"
              label="Студенты из районов, подвергшихся радиоактивному заражению"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_parents_retired"
              label="Студенты, у которых оба родителя пенсионеры"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_many_kids_family"
              label="Студенты из многодетных семей"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_from_broken_home"
              label="Студенты из неполных семей"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_poor"
              label="Относится к категории малообеспеченных"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_chronic_disease"
              label="Студенты, страдающих хроническими заболеваниями"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_wed"
              label="Студенты, состоящие в браке"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_status_student_family"
              label="Имеют статус 'студенческая семья"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_have_kids"
              label="Студенты, имеющие детей"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_unwed_mother"
              label="В том числе матери-одиночки"
            ></v-checkbox>
            <v-checkbox
              color="green"
              :disabled="!isEditing"
              v-model="student.is_south_east_ukraine"
              label="Студенты, прибывшие на обучение из Юго-востока Украины"
            ></v-checkbox>
          </v-tab-item>
          <v-tab-item> </v-tab-item>
        </v-tabs-items>
      </v-form>
    </v-card-text>
    <v-divider></v-divider>
    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn :disabled="!isEditing" color="success" @click="save()">
        Обновить
      </v-btn>
    </v-card-actions>
    <v-snackbar
      v-model="snackbar"
      :timeout="2000"
      :bottom="true"
      :left="true"
      color="green"
      class="text-center"
    >
      Информация о студенте обновлена
    </v-snackbar>
  </v-card>
</template>

<script>
  import { mapGetters } from 'vuex'

  export default {
    name: 'student-retrive',
    data() {
      return {
        tab: null,
        isEditing: null,
        snackbar: false
      }
    },
    props: { student: null },
    methods: {
      save() {
        const pk = this.$route.params.pkStudent
        const student = this.student
        this.$store
          .dispatch('students/putStudent', { pk, student })
          .then(() => {
            this.snackbar = true
            this.isEditing = false
          })
      }
    },
    computed: {
      ...mapGetters('enums', [
        'disabilityGroup',
        'gender',
        'paymentTraining',
        'activeGroup'
      ])
    },
    mounted() {
      Promise.all([
        this.$store.dispatch('enums/loadDisabilityGroup'),
        this.$store.dispatch('enums/loadGender'),
        this.$store.dispatch('enums/loadPaymentTraining'),
        this.$store.dispatch('enums/loadActiveGroup')
      ]).finally(() => {
        this.loading = true
      })
    }
  }
</script>
