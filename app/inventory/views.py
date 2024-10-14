from django.shortcuts import render
from django.views import View

# Create your views here.
def InventoryView(View):
    def get(self, request):
        return render('inventory.html')
