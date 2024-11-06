# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# from app.inventory.models import Item
# from app.inventory.forms import ItemForm


# #Item Views
# class ItemListView(ListView):
#     model = Item
#     template_name = 'inventory/items/item_list.html'
#     context_object_name = 'items'

#     def get_queryset(self):
#         return Item.objects.select_related('category').all
#         # return Item.objects.all()

# class ItemDetailView(DetailView):
#     model = Item
#     template_name = 'inventory/items/item_detail.html'
#     context_object_name = 'item'

#     def get_object(self, queryset=None):
#         return Item.objects.select_related('category').get(pk=self.kwargs['pk'])

# class ItemCreateView(CreateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'inventory/items/item_form.html'
#     success_url = reverse_lazy('item-list')
# class ItemUpdateView(UpdateView):
#     model = Item
#     form_class = ItemForm
#     template_name = 'inventory/items/item_form.html'
#     success_url = reverse_lazy('item-list')

# class ItemDeleteView(DeleteView):
#     model = Item
#     template_name = 'inventory/items/item_confirm_delete.html'
#     success_url = reverse_lazy('item-list')