from django.db import models
from django.utils import timezone
# Create your models here.
# 게시글(Post)엔 제목(postname), 내용(contents)이 존재합니다
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname

class Photo(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

class Comment(models.Model):
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    comment_user = models.CharField(max_length=20, default='anonymous')
    comment = models.TextField()
    password = models.CharField(max_length=20)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    like = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.comment_user