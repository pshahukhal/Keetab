from django.conf.urls import url,include
from keetab_app import views

# app url patterns

urlpatterns = [
    url(r'^about/$',views.AboutView.as_view(),name="about"),
    url(r'^$',views.UserListView.as_view(),name="user_list"),
    url(r'^user/(?P<pk>\d+)$',views.UserDetailView.as_view(),name="user_detail"),
    url(r'^books/$',views.BookListView.as_view(),name="book_list"),
    url(r'^datatable/user/$', views.UserListJsonView.as_view(), name='user_list_json'),
    url(r'^datatable/book/$', views.BookListJsonView.as_view(), name='book_list_json'),
]
