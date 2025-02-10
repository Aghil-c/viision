from django.shortcuts import render
from course.models import Course

# Create your views here.
def course(request):
    if request.method=='POST':
        obj=Course()
        obj.course=request.POST.get('course')
        obj.course_duration=request.POST.get('duration')
        obj.admin_id=1
        obj.save()



    return render(request,'course/course.html')
def viewcourse(request):
    obj=Course.objects.all()
    context={
        'cc':obj
    }

    return render(request,'course/view_course.html',context)