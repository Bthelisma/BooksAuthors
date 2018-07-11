# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def index(request):
    context = {"books": Book.objects.all()}
    return render (request, "book_authors/index.html", context)
