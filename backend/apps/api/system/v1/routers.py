from django.urls import path
from .views import groups, students, enums, reference

app_name = "system"

urlpatterns = [
    # Группы
    path("groups/", groups.AcademicGroupList.as_view()),
    path("groups/<int:pk>/", groups.AcademicGroupDetail.as_view()),
    # Студенты
    path("students/<int:pk>/", students.StudentDetail.as_view()),
    # Справочники
    path("nationality/", reference.NationalityList.as_view()),
    path("nationality/<int:pk>/", reference.NationalityDetail.as_view()),
    path("native-language/", reference.NativeLanguageList.as_view()),
    path(
        "native-language/<int:pk>/", reference.NativeLanguageDetail.as_view()
    ),
    path("citizenship/", reference.CitizenshipList.as_view()),
    path("citizenship/<int:pk>/", reference.CitizenshipDetail.as_view()),
    path("training-direction/", reference.TrainingDirectionList.as_view()),
    path(
        "training-direction/<int:pk>/",
        reference.TrainingDirectionDetail.as_view(),
    ),
    # Перечесления
    path("form-training/", enums.FormTrainingListView.as_view()),
    path("payment-training/", enums.PaymentTrainingListView.as_view()),
    path("type-training/", enums.TypeTrainingListView.as_view()),
    path("active-group/", enums.ActiveGroupListView.as_view()),
    path("disability-group/", enums.DisabilityGroupListView.as_view()),
    path("gender/", enums.GenderListView.as_view()),
]
