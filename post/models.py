from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=12)
    content = models.TextField(blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    modify_at = models.DateTimeField(auto_now=True)
    #comment_set : 나와 연결된 모든 댓글


    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return f'{self.title}'

class Comment(models.Model):
    body = models.CharField(max_length=5)
    create_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')

        #post 1 : comment n
        #models.CASCADE: 연결되어 있는 데이터 삭제 시, 순차적으로 나도 삭제
        #post1.comments : 그 기사와 연결되어 있는 모든 댓글 접근 방법(기본값: comment_set)
        #models.OneToOneField(): 1:1
        #models.ManyToManyField(): n:n

    class Meta:
        ordering = ('-create_at',)

    def __str__(self):
        return f'{self.body} | {self.create_at.strftime("%Y-%m-%d %H:%M:%s")}'
