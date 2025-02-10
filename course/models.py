from django.db import models
from adminn.models import Admin

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_duration = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    admin=models.ForeignKey(Admin,on_delete=models.CASCADE)
    #admin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'course'

