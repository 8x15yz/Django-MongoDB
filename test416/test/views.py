from django.shortcuts import render
from django.http import HttpResponse
from .models import diary_collections

def index(request):
    return HttpResponse("<h1>App is running</h1>")

def add_diary(request):
    records = {
        "diaryTitle": "123",
        "userName": "kate"
    }
    diary_collections.insert_one(records)
    return HttpResponse("New diary is added")

def get_all_diary(request):
    diaries = diary_collections.find_one()  # 일기 데이터 가져오기
    context = {"diaries": diaries}  # 템플릿에 전달할 컨텍스트
    return HttpResponse(str(context))