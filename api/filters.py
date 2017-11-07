from django_filters import rest_framework as filters

from api.models import Place


class PlaceFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Place
        fields = ['name', 'type']