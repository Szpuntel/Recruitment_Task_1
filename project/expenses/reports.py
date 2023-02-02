from collections import OrderedDict

from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.db.models.functions import TruncMonth


def summary_per_category(queryset):
    return OrderedDict(sorted(
        queryset
        .annotate(category_name=Coalesce('category__name', Value('-')))
        .order_by()
        .values('category_name')
        .annotate(s=Sum('amount'))
        .values_list('category_name', 's')
    ))


def total_amount_spent(queryset):
    return queryset.aggregate(s=Sum('amount'))['s']

def summary_per_year_month(queryset):
    return queryset.annotate(year_month=TruncMonth('date')
    ).values(
        'year_month'
    ).annotate(
        total=Sum('amount')
    ).order_by(
        'year_month'
    )

