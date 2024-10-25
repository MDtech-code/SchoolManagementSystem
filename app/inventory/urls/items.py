from django.urls import path
from inventory.views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
urlpatterns = [
       # Item URLs
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),
]
