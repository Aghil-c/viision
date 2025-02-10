from django.conf.urls import url
from notification import views

urlpatterns = [
    url('post_notification/',views.notification),
    url('post_view_notification/',views.viewnotification),


]