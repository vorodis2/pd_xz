"""


Ж1 Новое



"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from group1 import views as group1_views
from group2 import views as group2_views

router = routers.DefaultRouter()
router.register(r'group1', group1_views.Group1ViewSet)
router.register(r'group2', group2_views.Group2ViewSet)

# router = routers.DefaultRouter()
# router.register(r'^group1$', group1_views.Group1ViewSet.as_view({"megaMethod": "megaFunc"}))
# router.register(r'^group1/asdasdsa/', custom_function)
# router.register(r'group2', group2_views.Group2ViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
