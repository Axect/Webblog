from django.conf.urls import url
from . import views

# 127.0.0.1:8000으로 들어오면 views.post_list를 보여줌.
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]