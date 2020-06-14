from io import BytesIO
from datetime import datetime
from django.views import View
from django.utils import dateformat
from django.http import HttpResponse
from docxtpl import DocxTemplate
from config.settings import TEMPLATES_DIR
from apps.api.system import models


class Document(View):
    """ Обработка запросов связанная с docx документами """

    def get(self, request, *args, **kwargs):
        """ Обработка GET запроса """
        doc = DocxTemplate(TEMPLATES_DIR + "/docx/group-card.docx")
        pk = kwargs["pk"]
        isnstanceAcademicGroup = models.AcademicGroup.objects.get(pk=pk)
        querysetStudents = models.Student.objects.filter(academic_group=pk)
        context = {
            "name": isnstanceAcademicGroup.name,
            "all_count": querysetStudents.count(),
            "date": dateformat.format(datetime.now(), ("d E Y")),
            "man": querysetStudents.filter(
                gender=models.enums.Gender.MALE.value
            ).count(),
            "woman": querysetStudents.filter(
                gender=models.enums.Gender.FEMALE.value
            ).count(),
            "budgetary": querysetStudents.filter(
                payment_training=models.enums.PaymentTraining.BUDGETARY.value
            ).count(),
            "commercial": querysetStudents.filter(
                payment_training=models.enums.PaymentTraining.COMMERCIAL.value
            ).count(),
            "is_orphan": querysetStudents.filter(is_orphan=True).count(),
            "disability_group": querysetStudents.filter(
                disability_group__isnull=False
            ).count(),
            "disability_group_one": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.FIRST.value
            ).count(),
            "disability_group_second": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.SECOND.value
            ).count(),
            "disability_group_third": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.THIRD.value
            ).count(),
            "is_military": querysetStudents.filter(is_military=True).count(),
            "is_radioactive": querysetStudents.filter(
                is_radioactive=True
            ).count(),
            "is_parents_retired": querysetStudents.filter(
                is_parents_retired=True
            ).count(),
            "is_parents_disabilities": querysetStudents.filter(
                is_parents_disabilities=True
            ).count(),
            "is_many_kids_family": querysetStudents.filter(
                is_many_kids_family=True
            ).count(),
            "is_many_kids_family_and_poor": querysetStudents.filter(
                is_many_kids_family=True, is_poor=True
            ).count(),
            "is_from_broken_home": querysetStudents.filter(
                is_from_broken_home=True
            ).count(),
            "is_from_broken_home_and_poor": querysetStudents.filter(
                is_from_broken_home=True, is_poor=True
            ).count(),
            "is_chronic_disease": querysetStudents.filter(
                is_chronic_disease=True
            ).count(),
            "is_wed": querysetStudents.filter(is_wed=True).count(),
            "is_wed_and_status_student_family": querysetStudents.filter(
                is_wed=True, is_status_student_family=True
            ).count(),
            "is_have_kids": querysetStudents.filter(is_have_kids=True).count(),
            "is_have_kids_and_unwed_mother": querysetStudents.filter(
                is_have_kids=True, is_unwed_mother=True
            ).count(),
            "is_south_east_ukraine": querysetStudents.filter(
                is_south_east_ukraine=True
            ).count(),
        }
        doc.render(context)
        byte_file = BytesIO()
        doc.save(byte_file)
        response = HttpResponse(
            byte_file.getvalue(), content_type="application/msword"
        )
        response[
            "Content-Disposition"
        ] = 'attachment; filename="group-card.docx"'
        return response


class DocumentTutorJournal(View):
    """ Дневник куратора """

    def get(self, request, *args, **kwargs):
        """ Обработка GET запроса """
        doc = DocxTemplate(TEMPLATES_DIR + "/docx/group-card.docx")
        pk = kwargs["pk"]
        isnstanceAcademicGroup = models.AcademicGroup.objects.get(pk=pk)
        querysetStudents = models.Student.objects.filter(academic_group=pk)
        context = {
            "name": isnstanceAcademicGroup.name,
            "all_count": querysetStudents.count(),
            "date": dateformat.format(datetime.now(), ("d E Y")),
            "man": querysetStudents.filter(
                gender=models.enums.Gender.MALE.value
            ).count(),
            "woman": querysetStudents.filter(
                gender=models.enums.Gender.FEMALE.value
            ).count(),
            "budgetary": querysetStudents.filter(
                payment_training=models.enums.PaymentTraining.BUDGETARY.value
            ).count(),
            "commercial": querysetStudents.filter(
                payment_training=models.enums.PaymentTraining.COMMERCIAL.value
            ).count(),
            "is_orphan": querysetStudents.filter(is_orphan=True).count(),
            "disability_group": querysetStudents.filter(
                disability_group__isnull=False
            ).count(),
            "disability_group_one": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.FIRST.value
            ).count(),
            "disability_group_second": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.SECOND.value
            ).count(),
            "disability_group_third": querysetStudents.filter(
                disability_group=models.enums.DisabilityGroup.THIRD.value
            ).count(),
            "is_military": querysetStudents.filter(is_military=True).count(),
            "is_radioactive": querysetStudents.filter(
                is_radioactive=True
            ).count(),
            "is_parents_retired": querysetStudents.filter(
                is_parents_retired=True
            ).count(),
            "is_parents_disabilities": querysetStudents.filter(
                is_parents_disabilities=True
            ).count(),
            "is_many_kids_family": querysetStudents.filter(
                is_many_kids_family=True
            ).count(),
            "is_many_kids_family_and_poor": querysetStudents.filter(
                is_many_kids_family=True, is_poor=True
            ).count(),
            "is_from_broken_home": querysetStudents.filter(
                is_from_broken_home=True
            ).count(),
            "is_from_broken_home_and_poor": querysetStudents.filter(
                is_from_broken_home=True, is_poor=True
            ).count(),
            "is_chronic_disease": querysetStudents.filter(
                is_chronic_disease=True
            ).count(),
            "is_wed": querysetStudents.filter(is_wed=True).count(),
            "is_wed_and_status_student_family": querysetStudents.filter(
                is_wed=True, is_status_student_family=True
            ).count(),
            "is_have_kids": querysetStudents.filter(is_have_kids=True).count(),
            "is_have_kids_and_unwed_mother": querysetStudents.filter(
                is_have_kids=True, is_unwed_mother=True
            ).count(),
            "is_south_east_ukraine": querysetStudents.filter(
                is_south_east_ukraine=True
            ).count(),
        }
        doc.render(context)
        byte_file = BytesIO()
        doc.save(byte_file)
        response = HttpResponse(
            byte_file.getvalue(), content_type="application/msword"
        )
        response[
            "Content-Disposition"
        ] = 'attachment; filename="group-card.docx"'
        return response


class GroupListDocument(View):
    """ Обработка запросов связанная с docx документами """

    def get(self, request, *args, **kwargs):
        """ Обработка GET запроса """
        doc = DocxTemplate(TEMPLATES_DIR + "/docx/group-list.docx")
        groups = models.AcademicGroup.objects.all()
        print(groups)
        context = {
            "date": dateformat.format(datetime.now(), ("d E Y")),
            "groups": groups,
        }
        doc.render(context)
        byte_file = BytesIO()
        doc.save(byte_file)
        response = HttpResponse(
            byte_file.getvalue(), content_type="application/msword"
        )
        response[
            "Content-Disposition"
        ] = 'attachment; filename="group-card.docx"'
        return response
