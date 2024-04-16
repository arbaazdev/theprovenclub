from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, MemberViewSet, ReservationViewSet

app_name = "api"

router = routers.DefaultRouter()

router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'reservation', ReservationViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
