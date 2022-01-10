from django.urls import path, include
from rest_framework.routers import SimpleRouter

from users.views import UserView


app_name = 'users'

router = SimpleRouter()
router.register(r'', UserView)

urlpatterns = [
    path('', include(router.urls))
]
