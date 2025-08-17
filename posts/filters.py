import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
   
    author = django_filters.CharFilter(field_name="author", lookup_expr="iexact")
    
    start_date = django_filters.DateFilter(field_name="created_at", lookup_expr="date__gte")
    end_date = django_filters.DateFilter(field_name="created_at", lookup_expr="date__lte")

    class Meta:
        model = Post
        fields = ["author", "start_date", "end_date"]
    