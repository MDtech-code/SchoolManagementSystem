from django.urls import path,include
from app.inventory.views.items import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView
from app.inventory.views.ItemsInStock import ItemsInStockListView,ItemsInStockDetailView, ItemsInStockCreateView, ItemsInStockUpdateView, ItemsInStockDeleteView
from app.inventory.views.Vendor import VendorListView, VendorDetailView, VendorCreateView, VendorUpdateView, VendorDeleteView
from app.inventory.views.purchaseRecord import PurchaseRecordListView, PurchaseRecordDetailView, PurchaseRecordCreateView, PurchaseRecordUpdateView, PurchaseRecordDeleteView
from app.inventory.views.ReturnToVendor import ReturnToVendorListView, ReturnToVendorDetailView, ReturnToVendorCreateView, ReturnToVendorUpdateView, ReturnToVendorDeleteView
from app.inventory.views.issuance import IssuanceListView, IssuanceDetailView, IssuanceCreateView, IssuanceUpdateView, IssuanceDeleteView
from app.inventory.views.ReturnFromDepartment import ReturnFromDepartmentListView, ReturnFromDepartmentDetailView, ReturnFromDepartmentCreateView, ReturnFromDepartmentUpdateView, ReturnFromDepartmentDeleteView

urlpatterns = [
    
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('items/create/', ItemCreateView.as_view(), name='item-create'),
    path('items/<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),

    # ItemsInStock URLs
    path('items-in-stock/', ItemsInStockListView.as_view(), name='items-in-stock-list'),
    path('items-in-stock/<int:pk>/', ItemsInStockDetailView.as_view(), name='items-in-stock-detail'),
    path('items-in-stock/create/', ItemsInStockCreateView.as_view(), name='items-in-stock-create'),
    path('items-in-stock/<int:pk>/update/', ItemsInStockUpdateView.as_view(), name='items-in-stock-update'),
    path('items-in-stock/<int:pk>/delete/', ItemsInStockDeleteView.as_view(), name='items-in-stock-delete'),

    # Vendor URLs
    path('vendors/', VendorListView.as_view(), name='vendor-list'),
    path('vendors/<int:pk>/', VendorDetailView.as_view(), name='vendor-detail'),
    path('vendors/create/', VendorCreateView.as_view(), name='vendor-create'),
    path('vendors/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor-update'),
    path('vendors/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor-delete'),

    # PurchaseRecord URLs
    path('purchase-records/', PurchaseRecordListView.as_view(), name='purchase-record-list'),
    path('purchase-records/<int:pk>/', PurchaseRecordDetailView.as_view(), name='purchase-record-detail'),
    path('purchase-records/create/', PurchaseRecordCreateView.as_view(), name='purchase-record-create'),
    path('purchase-records/<int:pk>/update/', PurchaseRecordUpdateView.as_view(), name='purchase-record-update'),
    path('purchase-records/<int:pk>/delete/', PurchaseRecordDeleteView.as_view(), name='purchase-record-delete'),

    # ReturnToVendor URLs
    path('returns-to-vendor/', ReturnToVendorListView.as_view(), name='return-to-vendor-list'),
    path('returns-to-vendor/<int:pk>/', ReturnToVendorDetailView.as_view(), name='return-to-vendor-detail'),
    path('returns-to-vendor/create/', ReturnToVendorCreateView.as_view(), name='return-to-vendor-create'),
    path('returns-to-vendor/<int:pk>/update/', ReturnToVendorUpdateView.as_view(), name='return-to-vendor-update'),
    path('returns-to-vendor/<int:pk>/delete/', ReturnToVendorDeleteView.as_view(), name='return-to-vendor-delete'),

    # Issuance URLs
    path('issuances/', IssuanceListView.as_view(), name='issuance-list'),
    path('issuances/<int:pk>/', IssuanceDetailView.as_view(), name='issuance-detail'),
    path('issuances/create/', IssuanceCreateView.as_view(), name='issuance-create'),
    path('issuances/<int:pk>/update/', IssuanceUpdateView.as_view(), name='issuance-update'),
    path('issuances/<int:pk>/delete/', IssuanceDeleteView.as_view(), name='issuance-delete'),

    # ReturnFromDepartment URLs
    path('returns-from-department/', ReturnFromDepartmentListView.as_view(), name='return-from-department-list'),
    path('returns-from-department/<int:pk>/', ReturnFromDepartmentDetailView.as_view(), name='return-from-department-detail'),
    path('returns-from-department/create/', ReturnFromDepartmentCreateView.as_view(), name='return-from-department-create'),
    path('returns-from-department/<int:pk>/update/', ReturnFromDepartmentUpdateView.as_view(), name='return-from-department-update'),
    path('returns-from-department/<int:pk>/delete/', ReturnFromDepartmentDeleteView.as_view(), name='return-from-department-delete'),

]
