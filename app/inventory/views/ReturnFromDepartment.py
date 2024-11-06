from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from app.inventory.models import ReturnFromDepartment
from app.inventory.forms import ReturnFromDepartmentForm
from django.urls import reverse_lazy

# ReturnFromDepartment View
class ReturnFromDepartmentListView(ListView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department/return_from_department_list.html'
    context_object_name = 'returns_from_department'

    def get_queryset(self):
        return ReturnFromDepartment.objects.select_related('department', 'stock_item__item')

class ReturnFromDepartmentDetailView(DetailView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department/return_from_department_detail.html'
    context_object_name = 'return_from_department'

class ReturnFromDepartmentCreateView(CreateView):
    model = ReturnFromDepartment
    form_class = ReturnFromDepartmentForm
    template_name = 'inventory/return_from_department/return_from_department_form.html'
    success_url = reverse_lazy('return-from-department-list')

class ReturnFromDepartmentUpdateView(UpdateView):
    model = ReturnFromDepartment
    form_class = ReturnFromDepartmentForm
    template_name = 'inventory/return_from_department/return_from_department_form.html'
    success_url = reverse_lazy('return-from-department-list')

class ReturnFromDepartmentDeleteView(DeleteView):
    model = ReturnFromDepartment
    template_name = 'inventory/return_from_department/return_from_department_confirm_delete.html'
    success_url = reverse_lazy('return-from-department-list')