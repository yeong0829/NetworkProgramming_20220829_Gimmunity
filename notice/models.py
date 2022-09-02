from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True) # 내용 없어도 됨
    create_at = models.DateTimeField(auto_now_add=True) #데이터 생성 시 날짜 시간 기록
    modify_at = models.DateTimeField(auto_now=True) #데이터 수정 시 날짜 시간 기록

    class Meta: #순서 지정
        ordering = ('-modify_at', '-create_at', 'title')#역순일 때 - 붙힘(내림차순)

    def __str__(self):
        return f'{self.title} | {self.content}'