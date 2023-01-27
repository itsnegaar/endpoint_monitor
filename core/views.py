from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status


from .models import UrlItem
from .serializers import UrlItemSerializer


class ListCreateUrlsView(generics.ListCreateAPIView):
    """
    Get url/
    Post url/
    """
    queryset = UrlItem.objects.all()
    serializer_class = UrlItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = UrlItemSerializer(data=request.data)
        if UrlItem.objects.filter(user=request.user).count() >= 20:
            return Response({'Error': 'Maximum URL count reached for user.'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            url = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        urls = UrlItem.objects.filter(user=request.user)
        serializer = UrlItemSerializer(urls, many=True)
        return Response(serializer.data)