from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView,CreateView, UpdateView, DeleteView
from app.inventory.models import ItemsInStock
from app.inventory.forms import ItemsInStockForm

# ItemsInStock Views

class ItemsInStockListView(ListView):
    model = ItemsInStock
    template_name = 'inventory/item_in_stock/items_in_stock_list.html'
    context_object_name = 'items_in_stock'

    def get_queryset(self):
        return ItemsInStock.objects.select_related('item').all()

class ItemsInStockDetailView(DetailView):
    model = ItemsInStock
    template_name = 'inventory/item_in_stock/items_in_stock_detail.html'
    context_object_name = 'items_in_stock'

class ItemsInStockCreateView(CreateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'inventory/item_in_stock/items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

   
class ItemsInStockUpdateView(UpdateView):
    model = ItemsInStock
    form_class = ItemsInStockForm
    template_name = 'inventory/item_in_stock/items_in_stock_form.html'
    success_url = reverse_lazy('items-in-stock-list')

class ItemsInStockDeleteView(DeleteView):
    model = ItemsInStock
    template_name = 'inventory/item_in_stock/items_in_stock_confirm_delete.html'
    success_url = reverse_lazy('items-in-stock-list')
