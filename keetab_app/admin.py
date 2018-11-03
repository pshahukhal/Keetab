# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from keetab_app.models import User,Book,BookPurchase

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookPurchase)
