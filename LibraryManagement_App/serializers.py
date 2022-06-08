from rest_framework import serializers
from .models import BookDetails

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = '__all__'