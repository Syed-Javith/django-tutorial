from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=20)
    stu_id = models.IntegerField(default=278)

class Department(models.Model):
    dept_name = models.CharField(max_length=200)


class Student(models.Model):
    email = models.EmailField()
    stu_reg = models.IntegerField()
    dept_id = models.ForeignKey(Department,on_delete=models.PROTECT,default=None)