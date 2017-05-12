from django.db import models
from django.utils import timezone


class Post(models.Model): # Delcare Django
    author = models.ForeignKey('auth.User') # 다른 모델에 대한 링크
    title = models.CharField(max_length=200) # 글자 수 제한 텍스트 (ex) 제목.
    text = models.TextField() # 글자 수 제한 없음
    created_date = models.DateTimeField(
        default=timezone.now) # 날짜와 시간
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title