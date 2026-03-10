
from django.shortcuts import render,redirect
from django.http import HttpResponse
from employee.forms import Addemployee
from employee.models import Employee
from django.views import View
from django.db.models import Q
# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'view.html')
class Addemployee(View):
    def get(self,request):
        form_instance = Addemployee()
        context = {'form': form_instance}
        return render(request, 'addemploy.html', context)

    def post(self, request):
        print(request.POST)
        print(request.FILES)
        form_instance = Addemployee(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
            return render(request, 'addemploy.html')
class Viewemployee(View):
    def get(self,request):
         b=Employee.objects.all()
         context={'books':b}
         return render(request,'viewbook.html',context)
class Searchemployee(View):
    def get(self,request):
         query=request.GET['q']
         print(query)

         b=Employee.objects.filter(Q(emp__id__icontains=query) |
                              Q(emp_name__icontains=query) |
                              Q(email__icontains=query) |
                              Q(phone_number__icontains=query) |
                              Q(designation__icontains=query)  |
                                 Q(salary__icontains=query) )
         context={'books':b}
         return render(request,'search.html',context)






