from django.shortcuts import render
from django.views import View
# Create your views here.
class Emp(View):
    def get(self, request):
        return render(request, 'employee/employee.html')
