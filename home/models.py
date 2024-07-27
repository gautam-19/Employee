from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=20)
    id_no = models.IntegerField()
    dept = models.CharField(max_length=120)
    salary = models.IntegerField()
    date = models.DateTimeField()

    #show entity with name
    def __str__(self):
        return self.first_name
    


    