from django.shortcuts import render, redirect
from .models import *
from .forms import *
from account.urls import *
from account.views import *


def start(request):
    return render(request, 'app/start.html')


def directory_list(request):
    directories = Directory.objects.filter(parent__isnull=True, user=request.user)
    return render(request, "app/directory_list.html", {'directories': directories})


def directory_detail(request, pk):
    directory = Directory.objects.get(pk=pk, user=request.user)
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
            form.save()
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