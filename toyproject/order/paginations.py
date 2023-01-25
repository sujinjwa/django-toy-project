from rest_framework import pagination

class OrderPagination(pagination.PageNumberPagination):
    # page_query_param : page가 아닌 key로 하고 싶다
    page_size = 10