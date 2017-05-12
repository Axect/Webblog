from __future__ import unicode_literals # python2

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Bookmark(models.Model): # Django model
    title = models.CharField(max_length=100, blank=True, null=True) # 글자 수가 제한된 텍스트를 정의할 때 사용.
    url = models.URLField('url', unique=True)
    
    def __str__(self):
        return self.title