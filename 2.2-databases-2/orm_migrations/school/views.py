from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    student_query = Student.objects.prefetch_related('teachers').order_by('group', 'name').all()
    context = {'object_list': student_query}

    return render(request, template, context)
