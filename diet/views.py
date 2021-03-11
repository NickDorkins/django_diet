from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Diet
from django.urls import reverse_lazy

class SDietListView(ListView):
    template = 'diet-list.html'
    model = Diet

class DietDetailView(DetailView):
    template = 'diet-detail.html'
    model = Diet

class DietCreateView(CreateView):
    template = 'diet-create.html'
    model = Diet
    fields = ['title', 'purchaser', 'description']
    

class DietUpdateView(UpdateView):
    template = 'diet-update.html'
    model = Diet
    fields = ['title', 'purchaser', 'description']    

class DietDeleteView(DeleteView):
    template = 'diet-delete.html'
    model = Diet
    success_url = reverse_lazy('diet_list')
