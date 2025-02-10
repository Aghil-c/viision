from django.db import models
from adminn.models import Admin

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    notification_time = models.TimeField()
    notification_date = models.DateField()
    notification = models.CharField(max_length=300)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    #admin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification'
