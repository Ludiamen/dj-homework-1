from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры

    status = filters.CharFilter()
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at', 'updated_at']
