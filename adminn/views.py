from django.shortcuts import render
from adminn.models import Admin

# Create your views here.
def adminn(request):
    if request.method=='POST':
        obj=Admin()
        obj.admin_college=request.POST.get('college')
        obj.admin_email=request.POST.get('Email')
        obj.admin_gender=request.POST.get('gender')
        obj.admin_photo=request.POST.get('Photo')
        obj.number=request.POST.get('number')
        obj.admin_password=request.POST.get('Password')
        obj.admin_username=request.POST.get('User')
        obj.save()

    return render(request,'admin/admin.html')
def view_adminn(request):
    obj=Admin.objects.all()
    context={
        'rr':obj
    }
    return render(request,'admin/view_admin.html',context)