from django.conf.urls import url
from course import views

urlpatterns = [
    url('post_course/',views.course),
    url('post_viewcourse/',views.viewcourse),


]