from django.db import models

# Create your models here.

class empresas(models.Model):

    name = models.CharField(max_length=100)
    status = models.IntegerField()

    def __str__(self):
        return self.name

class vagas(models.Model):

    name = models.CharField(max_length=250)
    depart = models.CharField(max_length=30)
    link = models.CharField(max_length=150)
    data = models.DateField()
    id_empresa = models.ForeignKey(empresas, on_delete=models.CASCADE)
