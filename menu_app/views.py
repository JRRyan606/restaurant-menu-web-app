# menu_app/views.py
from django.shortcuts import render
from .models import MenuItem


# menu_app/views.py
def menu_list(request):
    menu_items = MenuItem.objects.filter(available=True)
    return render(request, 'menu_app/menu_list.html', {'menu_items': menu_items})

