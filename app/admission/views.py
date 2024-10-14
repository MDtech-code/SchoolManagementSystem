from django.shortcuts import render
from django.views import View
class AdmissionView(View):
    def get(self,request):
        return render(request,'admission.html')
    
# Create your views here.
