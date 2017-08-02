from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import QuestionCreateView, QuestionDetailsView, ChoiceCreateView, ChoiceDetailsView

urlpatterns = {
    url(r'^questions/$', QuestionCreateView.as_view(), name="create"),
    url(r'^questions/(?P<pk>[0-9]+)/$',
        QuestionDetailsView.as_view(), name="details"),
    url(r'^choices/$', ChoiceCreateView.as_view(), name="create"),
    url(r'^choices/(?P<pk>[0-9]+)/$',
        ChoiceDetailsView.as_view(), name="details"),        
}

urlpatterns = format_suffix_patterns(urlpatterns)