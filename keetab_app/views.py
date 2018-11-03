# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from keetab_app.models import User,Book,BookPurchase
from django.urls import reverse_lazy
from django_datatables_view.base_datatable_view import BaseDatatableView

# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class UserListView(TemplateView):
    template_name = 'user_list.html'

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'


class BookListView(TemplateView):
    template_name = 'book_list.html'

# Views to generate the json for the data Table used

class UserListJsonView(BaseDatatableView):
    model = User
    columns = ['first_name', 'last_name', 'age', 'city', 'number','id',]

class BookListJsonView(BaseDatatableView):
    model = Book
    columns = ['title', 'author', 'language', 'price',]
