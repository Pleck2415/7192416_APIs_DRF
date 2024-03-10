from rest_framework.viewsets import ModelViewSet
 
from shop.models import Category
from shop.models import Product
from shop.serializers import CategorySerializer
from shop.serializers import ProductSerializer

class CategoryViewset(ModelViewSet):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
    
class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()