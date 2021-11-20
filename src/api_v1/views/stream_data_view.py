from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from decimal import Decimal
from analytics.models import Metrics, StreamData
from ..serializers import StreamDataSerializer


class StreamDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = StreamDataSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                'detail': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        auth_token = request.META.get('HTTP_AUTHORIZATION')
        metrics_code = kwargs.get('metrics_code')
        try:
            user = Token.objects.get(
                key=auth_token.replace('Token ', '')
            ).user
        except Token.DoesNotExist:
            return Response({
                'detail': '不正なトークンです。'
            }, status=status.HTTP_401_UNAUTHORIZED)
        try:
            metrics = Metrics.objects.get(
                user=user,
                code=metrics_code,
            )
        except Metrics.DoesNotExist:
            return Response({
                'detail': 'メトリクスが存在しません。'
            }, status=status.HTTP_404_NOT_FOUND)
        StreamData.objects.create(
            datetime=serializer.data.get('datetime'),
            value=serializer.data.get('value'),
            metrics=metrics,
        )
        return Response(serializer.data, status=status.HTTP_201_CREATED)

stream_data_view = StreamDataView.as_view()
