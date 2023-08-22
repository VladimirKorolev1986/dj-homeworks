from django_filters import rest_framework as filters, DateFromToRangeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    date = DateFromToRangeFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['status', 'creator']
