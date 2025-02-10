from django.conf.urls import url
from adminn import views

urlpatterns=[
   url('post_admin',views.adminn),
   url('post_view_admin',views.view_adminn),
]