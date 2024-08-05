import django_filters
from .models import DesignerWork, Category


class DesignerWorkFilter(django_filters.FilterSet):
    designe_title = django_filters.CharFilter(lookup_expr='icontains', label='Название работы')
    user__username = django_filters.CharFilter(lookup_expr='icontains', label='Имя дизайнера')
    hashtag = django_filters.CharFilter(lookup_expr='icontains', label='Хэштеги')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Категория')
    publicated_date = django_filters.DateFromToRangeFilter(field_name='publicated_date', label='Дата публикации')

    class Meta:
        model = DesignerWork
        fields = ['designe_title', 'user__username', 'hashtag', 'category', 'publicated_date']
