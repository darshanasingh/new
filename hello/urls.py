from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^snippets/$', views.SnippetGet.as_view()),
    url(r'^snippetspost/$', views.SnippetPost.as_view()),
    url(r'^userdetails/$', views.UserDetails.as_view()),
    url(r'^getuserdetails/(?P<userid>[0-9]+)/$', views.GetUserdetails.as_view()),
    url(r'^changepass/$', views.changepass.as_view()),
]
