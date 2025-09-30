from django.shortcuts import render, redirect
from testapp.models import EmployeeModel
from testapp.forms import EmployeeModelForm
# Create your views here.
def home_view(request):
    return render(request,"home.html")

def table_view(request):
    emp_data=EmployeeModel.objects.all().order_by("id")
    dict={"employees":emp_data}
    return render(request,"table.html",context=dict)


def insert_view(request):
    if request.method=="POST":
        form= EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form=EmployeeModelForm()
    insert_data={"form":form}
    return render(request,"insert.html",context=insert_data)


def delete_view(request,id):
    employee=EmployeeModel.objects.get(id=id)
    employee.delete()
    return redirect("/employees/")

def update_view(request, id):
    employee = EmployeeModel.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeModelForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            # Redirect to employee list page after update
            return redirect('/employees/')  # replace with your URL name
    else:
        form = EmployeeModelForm(instance=employee)
    context = {"form": form}
    return render(request, "update.html", context)

