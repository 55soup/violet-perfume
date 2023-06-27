from django.db import models

# Create your models here.
class Memory(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']


    def __str__(self):
        return self.name


class Comments(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20) #닉네임
    comment = models.CharField(max_length=200) #댓글내용
    created = models.DateTimeField(auto_now_add=True) #생성날짜
    updated = models.DateTimeField(auto_now=True) #수정시 날짜 변경
    heart = models.IntegerField() #하트 갯수

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment