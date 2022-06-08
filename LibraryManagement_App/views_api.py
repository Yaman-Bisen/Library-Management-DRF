from .models import BookDetails
from .serializers import BookDetailsSerializer
from rest_framework import viewsets

class BookDetailsViewSet(viewsets.ModelViewSet):
    queryset = BookDetails.objects.all()
    serializer_class = BookDetailsSerializer