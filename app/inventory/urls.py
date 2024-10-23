from django.urls import path
from . import views
from django.urls import path
from . import views
from .views import (
    ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView,
    ItemsInStockListView, ItemsInStockDetailView, ItemsInStockCreateView, ItemsInStockUpdateView, ItemsInStockDeleteView,
    VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView, VendorDeleteView,
    PurchaseRecordCreateView, ReturnToVendorCreateView, IssuanceCreateView
)

urlpatterns = [
    path('inventory/', views.InventoryView.as_view(), name='inventory'),
    
    # Item URLs
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),

    # ItemsInStock URLs
    path('stock/', ItemsInStockListView.as_view(), name='items-in-stock-list'),
    path('stock/<int:pk>/', ItemsInStockDetailView.as_view(), name='items-in-stock-detail'),
    path('stock/create/', ItemsInStockCreateView.as_view(), name='items-in-stock-create'),
    path('stock/<int:pk>/update/', ItemsInStockUpdateView.as_view(), name='items-in-stock-update'),
    path('stock/<int:pk>/delete/', ItemsInStockDeleteView.as_view(), name='items-in-stock-delete'),

    # Vendor URLs
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/create/', VendorCreateView.as_view(), name='vendor-create'),
    path('vendors/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendors/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),

    # PurchaseRecord URLs
    path('purchase-records/create/', PurchaseRecordCreateView.as_view(), name='purchase-record-create'),

    # ReturnToVendor URLs
    path('return-to-vendor/create/', ReturnToVendorCreateView.as_view(), name='return-to-vendor-create'),

    # Issuance URLs
    path('issuance/create/', IssuanceCreateView.as_view(), name='issuance-create'),
]
