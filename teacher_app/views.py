from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Teacher, Subject
from .forms import TeacherForm,SubjectForm
import csv
import os
from django.conf import settings

def home(request):
    return render(request,'teacher_app/base.html')

def teacher_list(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'teacher_app/teacher_list.html', {'teachers': teachers, 'subjects': subjects})

def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    print(teacher.__dict__)
    return render(request, 'teacher_app/teacher_detail.html', {'teacher': teacher})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teacher_app/add_teacher.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = SubjectForm()
    return render(request, 'teacher_app/add_subject.html', {'form': form})

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    if request.method == 'POST':
        form = TeacherForm(request.POST, request.FILES, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teacher_app/edit_teacher.html', {'form': form, 'teacher': teacher})

def filter_teachers(request):
    print("pppppppppppppp========")
    print(request.method)
    if request.method == 'GET':
        letter = request.GET.get('letter', '')
        subject_id = request.GET.get('subject_id', '')
        teachers = Teacher.objects.all()
        if letter:
            teachers = teachers.filter(last_name__istartswith=letter)
        if subject_id:
            teachers = teachers.filter(subjects_taught=subject_id)
        teachers_data = [{'id': teacher.id, 'first_name': teacher.first_name, 'last_name': teacher.last_name} for teacher in teachers]
        print(teachers_data,"ooooooooooooooo------------")
        return JsonResponse({'teachers': teachers_data})
    return JsonResponse({})

def import_teachers(request):
    if request.method == 'POST' and request.user.is_authenticated:
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            handle_uploaded_csv(csv_file)
    return redirect('teacher_list')

def handle_uploaded_csv(csv_file):
    csv_file_name = csv_file.name
    csv_file_path = os.path.join(settings.MEDIA_ROOT, 'teacher_csv', csv_file_name)

    with open(csv_file_path, 'wb+') as destination:
        for chunk in csv_file.chunks():
            destination.write(chunk)

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            first_name = row['First Name']
            last_name = row['Last Name']
            email = row['Email Address']
            phone_number = row['Phone Number']
            room_number = row['Room Number']
            subject_names = [s.strip() for s in row['Subjects taught'].split(',') if s.strip()]
            subjects_taught = [Subject.objects.get_or_create(name=name)[0] for name in subject_names]
            print("kkkkkk")
            
            # Create or update the teacher
            teacher, created = Teacher.objects.update_or_create(
                email=email,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'phone_number': phone_number,
                    'room_number': room_number,
                }
            )
            teacher.subjects_taught.set(subjects_taught)

from django.shortcuts import render
from .forms import ImportTeachersForm

def upload_csv(request):
    if request.method == 'GET':
        print("iiiiiiiiiiii",request.user.is_authenticated,request.method)
        form = ImportTeachersForm()
        return render(request, 'teacher_app/upload_csv.html', {'form': form})
    if request.method == 'POST' and request.user.is_authenticated:
        print("jjjjjjjjjjjjjjj")
        csv_file = request.FILES.get('csv_file')
        if csv_file:
            handle_uploaded_csv(csv_file)
    return redirect('teacher_list')

# teacher_directory/views.py

from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('teacher_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        print("1111111111----------")
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('teacher_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')
