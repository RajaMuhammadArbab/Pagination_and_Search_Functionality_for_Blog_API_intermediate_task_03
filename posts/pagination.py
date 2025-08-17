from math import ceil
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class DefaultPaginator(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "limit"    
    max_page_size = 100

    def get_paginated_response(self, data):
        total_posts = self.page.paginator.count
        page_size = self.get_page_size(self.request) or self.page.paginator.per_page
        total_pages = ceil(total_posts / page_size) if page_size else 1
        current_page = self.page.number
        return Response({
            "meta": {
                "total_posts": total_posts,
                "total_pages": total_pages,
                "current_page": current_page,
                "page_size": page_size,
            },
            "results": data
        })
