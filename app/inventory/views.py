from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Item
from .forms import ItemForm

# Item Views
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item-list')

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'
    success_url = reverse_lazy('item-list')

class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_confirm_delete.html'
    success_url = reverse_lazy('item-list')