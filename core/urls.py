from django.conf.urls import url

from .views import best_time_to_post

urlpatterns = [
    url(r'^best_time/$', best_time_to_post, name='core_best_time_to_post')
]
