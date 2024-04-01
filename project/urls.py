from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from shop.views import CategoryViewset, ProductViewset, ArticleViewset, AdminCategoryViewset, AdminArticleViewSet
from shop.views import AdminUserViewset


router = routers.SimpleRouter()
# router.register('category', CategoryViewset, basename='category')
# router.register('product', ProductViewset, basename='product')
# router.register('article', ArticleViewset, basename='article')
router.register('admin/user', AdminUserViewset, basename='admin-user')
# router.register('admin/article', AdminArticleViewSet, basename='admin-article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
