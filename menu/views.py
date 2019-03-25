from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from datetime import datetime as dt
from django.utils import timezone
from operator import attrgetter
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from .models import Menu, Item
from .forms import MenuForm


def menu_list(request):
    menus = Menu.objects.all().prefetch_related('items')
    return render(request, 'menu/list_all_current_menus.html', {'menus': menus})


def menu_detail(request, pk):
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    item = Item.objects.get(pk=pk)
    return render(request, 'menu/detail_item.html', {'item': item})


def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('menu_detail', pk=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'menu/menu_new.html', {'form': form})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    form = MenuForm(instance=menu)
    if request.method == "POST":
        if form.is_valid:
            form = MenuForm(request.POST)
            menu = form.save()
            return redirect('menu_detail', pk=menu.pk)
    return render(request, 'menu/change_menu.html', {
        'menu': menu,
        'form': form,
    })
