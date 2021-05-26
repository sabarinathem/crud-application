from django.shortcuts import render,redirect
from employee.form import EmployeeForm,CreateUserForm
from employee.models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='employee:login')
def index(request):
    
    form=EmployeeForm()
    return render(request,'employee/index.html',{'form':form})
@login_required(login_url='employee:login')
def emp(request):

    if request.method=='POST':
        form=EmployeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/show')
            # try:
            #     form.save()
                # return redirect("/show")
                
            # except:
            #     pass
            eid=form.cleaned_data['eid']
            ename = form.cleaned_data['ename']
            eemail = form.cleaned_data['eemail']
            econtact = form.cleaned_data['econtact']

            context = {
                    'eid':eid,
                    'ename': ename,
                    'eemail': eemail,
                    'econtact': econtact
            }
            

            return render(request,'employee/show.html',context)
    # else:
    #     form=EmployeeForm()
    # return render(request,'employee/index.html',{'form':form})
@login_required(login_url='employee:login')
def show(request):
    employees=Employee.objects.all()
    
    return render(request,'employee/show.html',{'employees':employees})
@login_required(login_url='employee:login')
def edit(request,id):
    employee=Employee.objects.get(pk=id)
    return render(request,'employee/edit.html',{'employee':employee})
@login_required(login_url='employee:login')
def update(request,id):
    employee=Employee.objects.get(pk=id)
    form=EmployeeForm(request.POST,instance=employee)

    if form.is_valid():
        form.save()

        return redirect('/show')
    return render(request,'employee/edit.html',{'employee':employee})

    
@login_required(login_url='employee:login')           
def delete(request,id):

    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
def registerPage(request):
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('employee:login')
    form=CreateUserForm()
    context={'form':form}
    return render(request,'employee/register.html',context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('employee:index')
    else:
        
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('employee:index')
            else:
                messages.info(request,'Username OR Password is Incorrect')
                context={}
                return render(request,'employee/login.html',context)
        context={}
        return render(request,'employee/login.html')
def logoutPage(request):
    logout(request)
    return redirect('employee:login')