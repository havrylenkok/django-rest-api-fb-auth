from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from api.views import ListView, CreateView, DetailView, UsersListView, CurrentUser

urlpatterns = {
    url(r'^places$', ListView.as_view(), name="list"),
    url(r'^places/search$', ListView.as_view(), name="search"),
    url(r'^places/create$', CreateView.as_view(), name="create"),
    url(r'^places/view/(?P<pk>\d+)$', DetailView.as_view(), name="view"),
    url(r'^users$', UsersListView.as_view(), name="users"),
    url(r'^me$', CurrentUser.as_view(), name="me")
}

urlpatterns = format_suffix_patterns(urlpatterns)
