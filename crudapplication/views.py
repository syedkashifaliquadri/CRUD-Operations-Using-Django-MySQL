from django.shortcuts import render,redirect
from crudapplication.forms import EmployeeForm
from crudapplication.models import Employee

# Create your views here.


def emp(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html',{'form':form})


def show(request):
    employees = Employee.objects.all()
    return render(request,'employee_list.html',{'employees':employees})


def edit(request,id=0):
    if request.method == "GET":                     # Ye info lekr ayga
        if id==0:                                   # Yaha ye new bande ko form dakhayega 0 means new user
            form = EmployeeForm()
        else:                                       # yaha jo app link mai id dogy user us ki info dakhyga
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request,"employee_form.html", {'form':form})
    else:
        if id==0:                                   # Yaha ye new bande ko form dakhayega 0 means new user
            form = EmployeeForm(request.POST)
        else:                                       # yaha jo app link mai id dogy user us ki info dakhyga or changes karre k bad DB mai b POST karega
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid():                         # Form agar sahi fill kara hoga phr DB mai save kar dega
            form.save()
        return redirect('/show')


# def update(request,id):
#     employee = Employee.objects.get(id=id)
#     form = EmployeeForm(request.POST,instance=employee)
#     if form.is_valid():
#         form.save()
#         return redirect('/show')
#     else:
#         return redirect('/edit')


def delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/show')