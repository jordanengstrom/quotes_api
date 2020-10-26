from rest_framework import generics
from rest_framework import permissions
from quote.models import Quote
from quote.api.serializers import QuoteSerializer
from quote.api.pagination import ThirtySetPagination
from quote.api.permissions import IsAdminUserOrReadOnly


# Anonymous users must be able to retrieve the available records
# Create permissions must be granted exclusively to admin users
class QuoteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = ThirtySetPagination


# Update/delete permissions must be granted exclusively to admin users
class QuoteDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [IsAdminUserOrReadOnly]
