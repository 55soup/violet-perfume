from django.core.validators import MinValueValidator
from django.db import models
from django.shortcuts import resolve_url


# Create your models here.
class Memory(models.Model):
    name = models.CharField(max_length=20, default='')
    description = models.CharField(max_length=100, default='')
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='memory_images/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # 모델 하나를 구하는 절대 주소
        return resolve_url('product:detail', pk=self.id)


class Comments(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default='') #닉네임
    comment = models.CharField(max_length=200, default='') #댓글내용
    created = models.DateTimeField(auto_now_add=True) #생성날짜
    updated = models.DateTimeField(auto_now=True) #수정시 날짜 변경
    heart = models.IntegerField(validators=[MinValueValidator(0)]) #하트 갯수

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.comment

class Reply(models.Model):
    pass