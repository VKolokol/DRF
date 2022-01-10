from rest_framework.viewsets import ReadOnlyModelViewSet

from users.serializers import UserSerializer
from users.models import Users


class UserView(ReadOnlyModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'pk'

