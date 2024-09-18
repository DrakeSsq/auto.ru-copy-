import django_filters
from .models import *



class Legkovoe_Avto_Filter(django_filters.FilterSet):
    year = django_filters.NumberFilter(field_name='year', lookup_expr='exact')
    marka = django_filters.CharFilter(field_name='marka__title', lookup_expr='icontains')
    price = django_filters.RangeFilter()
    city = django_filters.ModelChoiceFilter(queryset=City.objects.all(), empty_label='Выберите город')

    class Meta:
        model = Legkovoe_Avto
        fields = ['year', 'marka', 'price', 'city']