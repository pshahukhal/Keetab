# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.db.models import Sum,Avg,Min,Max,DecimalField

# Create your models here.
# User model to maintain the user details
class User(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    age = models.IntegerField()
    number = models.IntegerField()
    city = models.CharField(max_length= 80)
    admin = models.BooleanField(default=False)
    balance = models.FloatField(default=0.0)

    def __str__(self):
        return (self.first_name + ' ' +  self.last_name)

    # Use of the properties to display the user behavior
    @property
    def total_price(self):
        purchasedbooks = self.boughtbooks.all()
        sum = purchasedbooks.aggregate(Sum('book__price'))
        return sum['book__price__sum']
    def average_price(self):
        purchasedbooks = self.boughtbooks.all()
        avg = purchasedbooks.aggregate(Avg('book__price'))
        return avg['book__price__avg']
    def minimum_price(self):
        purchasedbooks = self.boughtbooks.all()
        min = purchasedbooks.aggregate(Min('book__price'))
        return min['book__price__min']
    def maximum_price(self):
        purchasedbooks = self.boughtbooks.all()
        max = purchasedbooks.aggregate(Max('book__price'))
        return max['book__price__max']

#  Model to display the list of books available
class Book(models.Model):
    author = models.CharField(max_length=160)
    title = models.CharField(max_length=80)
    language = models.CharField(max_length=80)
    price = models.FloatField()

    def __str__(self):
        return (self.title)

#  model to display the purchases of books made by users
class BookPurchase(models.Model):
    user = models.ForeignKey('keetab_app.User',on_delete=models.CASCADE,related_name="boughtbooks")
    book = models.ForeignKey('keetab_app.Book',on_delete=models.CASCADE,related_name="boughtbooks")
    purchased_date = models.DateField(default=timezone.now())

    def __str__(self):
        return self.user.first_name + ' - ' + self.book.title

    class Meta:
        ordering = ['-purchased_date',]
