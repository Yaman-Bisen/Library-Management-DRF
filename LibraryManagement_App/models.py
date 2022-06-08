from django.db import models

# Create your models here.

class CommonFields(models.Model):
    email = models.EmailField(primary_key=True, max_length=100)
    password = models.CharField(max_length=100)

    class Meta:
        abstract = True

class AdminLogin(CommonFields):
    pass

class StudentLogin(CommonFields):
    pass

class BookDetails(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    price = models.FloatField()
    qunatity = models.IntegerField()
    date_added = models.DateField()