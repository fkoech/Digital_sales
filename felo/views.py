# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import FeloItem

# Create your views here.
def feloView(request):
    all_felo_item = FeloItem.objects.all()
    return render(request, 'index.html', {'all_items': all_felo_item})

def addFelo(request):
    new_item = FeloItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/felo/')

def deleteFelo(request, felo_id):
    item_to_delete = FeloItem.objects.get(id=felo_id)
    item_to_delete.delete()
    return HttpResponseRedirect('/felo/')
   
