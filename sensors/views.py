from rest_framework import mixins, status, viewsets
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import action
from rest_framework.response import Response

from .auth import SensorTokenPermission
from .models import Sensor
from .serializers import SensorDataSerializer, SensorSerializer


class SensorView(viewsets.ReadOnlyModelViewSet):
    # when logged in the browser, all the listing of sensors
    authentication_classes = [SessionAuthentication]
    serializer_class = SensorSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Sensor.objects.filter(owner=self.request.user)
        return Sensor.objects.none()

    @action(detail=True, methods=["get"], permission_classes=[SensorTokenPermission])
    def config(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
            # only allow config retrieve for tokens
            self.check_object_permissions(request, sensor)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(sensor.meta)

    @action(detail=True, methods=["post"], permission_classes=[SensorTokenPermission])
    def upload(self, request, pk):
        try:
            sensor = Sensor.objects.get(pk=pk)
            # only allow data upload with tokens
            self.check_object_permissions(request, sensor)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = SensorDataSerializer(
            data={"sensor": sensor.id, "data": request.data}
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "data saved"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
