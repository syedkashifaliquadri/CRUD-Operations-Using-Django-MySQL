from django.db import models

# Create your models here.


class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    class Meta:
        db_table = 'employee'       # app k database mai 'employee' naam se table aye is li 'Meta class' use ki.
