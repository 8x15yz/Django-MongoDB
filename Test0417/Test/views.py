from django.http import HttpResponse
from .models import collections


def create_student_info(request):
    content = {
        "code":"1116",
        "name":"MK",
        "grade":"sophomore"
    }
    collections.insert_one(content)
    return HttpResponse("create successfully!")