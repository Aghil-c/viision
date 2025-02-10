from django.shortcuts import render
from notification.models import Notification
import datetime

# Create your views here.
def notification(request):
    if request.method=='POST':
        obj=Notification()
        obj.admin_id=1
        obj.notification=request.POST.get('notification')
        obj.notification_date=datetime.datetime.today()
        obj.notification_time=datetime.datetime.now()
        obj.save()
    return render(request,'notification/notification.html')

def viewnotification(request):
    obj=Notification.objects.all()
    context={
        'n': obj

    }


    return render(request,'notification/viewnotification.html',context)