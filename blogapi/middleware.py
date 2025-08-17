from django.http import JsonResponse
from urllib.parse import parse_qs
import re

class QueryValidationMiddleware:
    """
    Validates common query params:
      - page: positive int (>=1)
      - limit: positive int (1..100)
      - ordering: safe comma-separated fields (letters, underscore, hyphen)
      - start_date/end_date: YYYY-MM-DD format if present
      - author: length cap (<=1000) to avoid abuse
      - search: length cap (<=1000)
    Returns 400 JSON on invalid input before hitting the view.
    """

    DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
    ORDER_RE = re.compile(r"^[-a-zA-Z0-9_,.]+$") 

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        q = request.META.get("QUERY_STRING", "")
        params = parse_qs(q, keep_blank_values=True)

        def bad(msg):
            return JsonResponse({"detail": msg}, status=400)

       
        if "page" in params:
            try:
                page = int(params["page"][0] or "1")
                if page < 1:
                    return bad("`page` must be >= 1.")
            except ValueError:
                return bad("`page` must be an integer.")

      
        if "limit" in params:
            try:
                limit = int(params["limit"][0] or "10")
                if limit < 1 or limit > 100:
                    return bad("`limit` must be between 1 and 100.")
            except ValueError:
                return bad("`limit` must be an integer.")

        
        for key in ("start_date", "end_date"):
            if key in params and params[key][0]:
                if not self.DATE_RE.match(params[key][0]):
                    return bad(f"`{key}` must be YYYY-MM-DD.")

     
        if "ordering" in params and params["ordering"][0]:
            if not self.ORDER_RE.match(params["ordering"][0]):
                return bad("`ordering` contains invalid characters.")

       
        for key in ("author", "search"):
            if key in params:
                if len(params[key][0]) > 1000:
                    return bad(f"`{key}` too long.")

        return self.get_response(request)
