from django.views.generic.list import ListView

from .forms import ExpenseSearchForm
from .models import Expense, Category
from .reports import summary_per_category,total_amount_spent,summary_per_year_month



class ExpenseListView(ListView):
    model = Expense
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = object_list if object_list is not None else self.object_list

        form = ExpenseSearchForm(self.request.GET)
        
        if form.is_valid():
            name = form.cleaned_data.get('name', '').strip()
            start_date = form.cleaned_data.get('start_date')
            end_date = form.cleaned_data.get('end_date')
            categories = form.cleaned_data.get('categories')

            if name:
                queryset = queryset.filter(name__icontains=name)

            if categories:
                queryset = queryset.filter(category__in=categories)

            if start_date and end_date:
                queryset = queryset.filter(
                    date__gte=start_date,
                    date__lte=end_date)

            if start_date:
                queryset = queryset.filter(date__gte=start_date)
            if end_date:
                queryset = queryset.filter(date__lte=end_date)
            

        return super().get_context_data(
            form=form,
            object_list=queryset,
            summary_per_category=summary_per_category(queryset),
            total_amount_spent=total_amount_spent(queryset),
            summary_per_year_month=summary_per_year_month(queryset),
            **kwargs)

class CategoryListView(ListView):
    model = Category
    paginate_by = 5