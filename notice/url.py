from django.urls import path

from notice.views import NoticeListView

app_name = 'notice'

urlpatterns = [
    path('', NoticeListView.as_view(), name='list'),
]