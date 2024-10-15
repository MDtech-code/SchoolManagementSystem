from django.shortcuts import render
from django.views import View

# Create your views here.
def financeView(View):
    def get(self, request):
        return render('finance.html')