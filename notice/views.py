from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from notice.models import Notice


class NoticeListView(ListView):
    model = Notice