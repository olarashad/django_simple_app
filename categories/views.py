from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category
from .forms import CategoryForm

class CategoryListView(ListView):
    model = Category
    template_name = "categories/list.html"
    context_object_name = "categories"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories/detail.html"
    context_object_name = "category"



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/form.html"

    def form_valid(self, form):
        category = form.save(commit=False)  
        category.save()
        form.save_m2m()  
        return redirect(category.get_absolute_url())

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories/form.html"

    def form_valid(self, form):
        category = form.save()
        form.save_m2m()  
        return redirect(category.get_absolute_url())

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories/confirm_delete.html"
    success_url = reverse_lazy('category_list')
