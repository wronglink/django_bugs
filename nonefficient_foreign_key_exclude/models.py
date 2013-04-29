from django.db import models

class A(models.Model):
    pass

class B(models.Model):
    name = models.CharField(max_length=15)
    a = models.ForeignKey(A)
