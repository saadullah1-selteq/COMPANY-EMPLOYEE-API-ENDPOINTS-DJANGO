from django.db import models


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    about_me = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('NON-IT', 'NON-IT'),
                                                     ('mobile phone', 'mobile phone')))
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)


def __str__(self):
    return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=11)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=(('Manager', 'Manager'), ('Software Developer', 'Developer')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
