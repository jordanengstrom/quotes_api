from rest_framework.pagination import PageNumberPagination


class ThirtySetPagination(PageNumberPagination):
    page_size = 30
