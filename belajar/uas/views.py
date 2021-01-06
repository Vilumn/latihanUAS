from django.shortcuts import render, redirect
from uas import models, forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def testing(request):
    folder = models.Folder.objects.all()
    if request.method == "POST":
        keyword = request.POST.get('keyword', '')
        result = models.Folder.objects.filter(nama_binatang__icontains= keyword)
        if keyword != '':
            context = {
                'folder': result,
            }
            return render(request, 'binatang1.html', context)
        print(keyword)
    

    context = {
        'folder': folder,

    }
    return render(request, 'binatang1.html', context)

def folder1(request, pk):

    context = {

    }
    return render(request, 'binatang2.html', context)

class FolderCreate(CreateView):
    template_name = "folderadd.html"
    form_class = forms.TambahBinatang

    def get_success_url(self):
        return reverse_lazy('binatang1')

class FolderUpdate(UpdateView):
    template_name = "folderadd.html"
    form_class = forms.TambahBinatang
    model = models.Folder

    def get_success_url(self):
        return reverse_lazy('binatang1')

class FolderDelete(DeleteView):
    template_name = "folderdelete.html"
    form_class = forms.TambahBinatang
    model = models.Folder

    def get_success_url(self):
        return reverse_lazy('binatang1')
    