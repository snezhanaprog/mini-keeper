from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from account.urls import *
from django.contrib.auth.models import User
from account.views import *


def start(request):
    return render(request, 'app/start.html')


def directory_list(request):
    directories = []
    user = User.objects.get(id=request.user.id)
    if user:
        directories = Directory.objects.filter(parent__isnull=True, user=user)
    return render(request, "app/directory_list.html", {'directories': directories})


def directory_detail(request, pk):
    directory = Directory.objects.get(pk=pk)
    subdirectories = directory.subdirectories.all()
    records = directory.records.all()
    context ={
        'directory': directory,
        'subdirectories': subdirectories,
        'records': records
    }
    return render(request, 'app/directory_detail.html', context)


def add_directory(request, parent_id=None):
    if request.method == 'POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            directory = form.save(commit=False)
            directory.user = request.user
            directory.author = request.user
            directory.save()
            return redirect('directory_list')
    else:
        form = DirectoryForm(initial={'parent': parent_id})
    return render(request, 'app/add_directory.html', {'form': form})


def add_record(request, directory_id):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        form.user = request.user
        if form.is_valid():
            record = form.save(commit=False)
            record.author = request.user
            record.user = request.user
            record.save()
            return redirect('directory_detail', pk=directory_id)
    else:
        form = RecordForm(initial={'directory': directory_id})
    return render(request, 'app/add_record.html', {'form': form})


def change_directory(request, parent_id=None, directory_id=None):
    directory = Directory.objects.get(pk=directory_id)
    if request.method == 'POST':
        form = DirectoryForm(request.POST, request.FILES)
        if form.is_valid():
            directory.name = form.cleaned_data['name']
            directory.parent = form.cleaned_data['parent']
            directory.image = form.cleaned_data['image']
            directory.save()
            if directory.parent is None:
                return redirect('directory_list')
            return redirect('directory_detail', directory.parent.id)
    else:
        form = DirectoryForm(initial={'parent': parent_id, 'image': directory.image, 'name': directory.name})
    return render(request, 'app/change_directory.html', {'form': form})


def del_directory(request, directory_id):
    if request.method == 'POST':
        directory = Directory.objects.get(pk=directory_id)
        if directory is not None:
            parent = directory.parent
            directory.delete()
            if parent is None:
                return redirect('directory_list')
            return redirect('directory_detail', parent.id)


def change_record(request, directory_id, record_id):
    directory = Directory.objects.get(pk=directory_id)
    record = directory.records.get(pk=record_id)
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            record.title = form.cleaned_data['title']
            record.directory = form.cleaned_data['directory']
            record.description = form.cleaned_data['description']
            record.content = form.cleaned_data['content']
            record.save()
            return redirect('directory_detail', record.directory.id)
    else:
        form = DirectoryForm(initial={'title': record.title, 'content': record.content, 'description': record.description, 'directory ': directory_id})
    return render(request, 'app/change_record.html', {'form': form})


def del_record(request, directory_id, record_id):
    if request.method == 'POST':
        directory = Directory.objects.get(pk=directory_id)
        record = directory.records.get(pk=record_id)
        if record is not None:
            record.delete()
            return redirect('directory_detail', pk=directory_id)


def public_directories(request):
    directories = Directory.objects.filter(type=Directory.PUBLIC).exclude(user=request.user)
    records = Record.objects.filter(type=Directory.PUBLIC).exclude(user=request.user)
    return render(request, 'app/public_directories.html', {'directories': directories, 'records': records})


def add_directory_to_user(request, directory_id):
    directory = get_object_or_404(Directory, id=directory_id)
    if directory.type == Directory.PUBLIC:
        new_directory = Directory(
            name=directory.name,
            parent=None,
            image=directory.image,
            user=request.user,
            author=directory.author,
            type=Directory.PUBLIC
        )
        new_directory.save()
        return redirect('public_directories')
    return redirect('public_directories')


def add_record_to_user(request, record_id):
    record = get_object_or_404(Record, id=record_id)
    if record.type == Directory.PUBLIC:
        new_record = Record(
            title=record.title,
            content=record.content,
            directory=None,
            description=record.description,
            author=record.author,
            user=request.user,
            type=Directory.PUBLIC
        )
        new_record.save()
        return redirect('public_directories')
    return redirect('public_directories')

