from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse


def home(request):
    form = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/index.html', {'form': form, 'stu': stud})

def Save(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            print(name)
            user = User(name=name,email=email,password = password)
            user.save()
            stud = User.objects.values()
            print(stud)
            student_data= list(stud)
            print(student_data)
            return JsonResponse({'status':'save','student_data':student_data})
        else:
            return JsonResponse({'status':0})

# Delete data
def Delete(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})