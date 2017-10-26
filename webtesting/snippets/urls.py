from django.conf.urls import url
from snippets.views import SnippetDetail, SnippetList
urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
]