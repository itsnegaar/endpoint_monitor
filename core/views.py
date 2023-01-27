from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status


from .models import UrlItem
from .serializers import UrlItemSerializer

#classbase

#list and create urls
class ListCreateUrlsView(generics.ListCreateAPIView):
    """
    Get url/
    Post url/
    """
    queryset = UrlItem.objects.all()
    serializer_class = UrlItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs): #create new url
        serializer = UrlItemSerializer(data=request.data)
        if UrlItem.objects.filter(user=request.user).count() >= 20:
            return Response({'Error': 'Maximum URL count reached for user.'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            url = serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs): #get all users url
        urls = UrlItem.objects.filter(user=request.user)
        serializer = UrlItemSerializer(urls, many=True)
        return Response(serializer.data)


#access to url with id and delete it
class UrlDetailView(generics.RetrieveDestroyAPIView):
    """
    Get url/<pk>/
    Delete url/<pk>/
    """
    queryset = UrlItem.objects.all()
    serializer_class = UrlItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        url = self.get_object()
        if url.user != request.user:
            return Response({'Error': 'You do not have permission to view this URL.'},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer = UrlItemSerializer(url)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        url = self.get_object()
        if url.user != request.user:
            return Response({'Error': 'You do not have permission to delete this URL.'},
                            status=status.HTTP_400_BAD_REQUEST)
        url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)