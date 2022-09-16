from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice


class NoticeDetailView(DetailView):
    model = Notice #DB에서 pk에 해당하는 notice 가져와서
                    #notice 라는 변수로 notice_detail.html파일로 전달