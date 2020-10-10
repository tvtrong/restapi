from django.contrib.auth.models import User
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
# Using APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Using mixins
from rest_framework import mixins
# Using generics
from rest_framework import generics
from rest_framework import permissions

from .permissions import IsOwnerOrReadOnly

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import renderers
from rest_framework.response import Response

from rest_framework import viewsets

from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Using ViewSets ----------------------------------------


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # URL path: ^ users/{pk}/change-password/$
    # URL name: 'user-change_password'
    @action(methods=['post'], detail=True, permission_classes=[IsAdminOrIsSelf], url_path='change-password', url_name='change_password')
    def set_password(self, request, pk=None):

        # Using generics ----------------------------------------
        # class UserList(generics.ListAPIView):
        #    queryset = User.objects.all()
        #    serializer_class = UserSerializer

        # class UserDetail(generics.RetrieveAPIView):
        #    queryset = User.objects.all()
        #    serializer_class = UserSerializer

        # class SnippetHighlight(generics.GenericAPIView):
        #    queryset = Snippet.objects.all()
        #    renderer_classes = [renderers.StaticHTMLRenderer]

        #    def get(self, request, *args, **kwargs):
        #        snippet = self.get_object()
        #        return Response(snippet.highlighted)

        # @api_view(['GET'])
        # def api_root(request, format=None):
        #    return Response({
        #        'users': reverse('user-list', request=request, format=format),
        #        'snippets': reverse('snippet-list', request=request, format=format)
        #    })

        # class SnippetList(generics.ListCreateAPIView):
        #    queryset = Snippet.objects.all()
        #    serializer_class = SnippetSerializer
        #    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        #    def perform_create(self, serializer):
        #        serializer.save(owner=self.request.user)

        # class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
        #    queryset = Snippet.objects.all()
        #    serializer_class = SnippetSerializer
        #    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
        #                          IsOwnerOrReadOnly]

        # Using mixins ------------------------------------------
        # class SnippetList(mixins.ListModelMixin,
        #                  mixins.CreateModelMixin,
        #                  generics.GenericAPIView):
        #    queryset = Snippet.objects.all()
        #    serializer_class = SnippetSerializer

        #    def get(self, request, *args, **kwargs):
        #        return self.list(request, *args, **kwargs)

        #    def post(self, request, *args, **kwargs):
        #        return self.create(request, *args, **kwargs)

        # Using APIView -----------------------------------------

        # class UserCountView(APIView):
        #    """
        #    A view that returns the count of active users in JSON.
        #    """
        #    renderer_classes = [JSONRenderer]

        #    def get(self, request, format=None):
        #        user_count = User.objects.filter(active=True).count()
        #        content = {'user_count': user_count}
        #        return Response(content)

        # class ExampleView(APIView):
        #    """
        #    A view that can accept POST requests with JSON content.
        #    """
        #    parser_classes = [JSONParser]

        #    def post(self, request, format=None):
        #        return Response({'received data': request.data})

        # class SnippetList(APIView):
        #    """
        #    List all snippets, or create a new snippet.
        #    """

        #    def get(self, request, format=None):
        #        snippets = Snippet.objects.all()
        #        serializer = SnippetSerializer(snippets, many=True)
        #        return Response(serializer.data)

        #    def post(self, request, format=None):
        #        serializer = SnippetSerializer(data=request.data)
        #        if serializer.is_valid():
        #            serializer.save()
        #            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Using mixins ------------------------------------------
        # class SnippetDetail(mixins.RetrieveModelMixin,
        #                    mixins.UpdateModelMixin,
        #                    mixins.DestroyModelMixin,
        #                    generics.GenericAPIView):
        #    queryset = Snippet.objects.all()
        #    serializer_class = SnippetSerializer

        #    def get(self, request, *args, **kwargs):
        #        return self.retrieve(request, *args, **kwargs)

        #    def put(self, request, *args, **kwargs):
        #        return self.update(request, *args, **kwargs)

        #    def delete(self, request, *args, **kwargs):
        #        return self.destroy(request, *args, **kwargs)

        # Using APIView -----------------------------------------
        # class SnippetDetail(APIView):
        #    """
        #    Retrieve, update or delete a snippet instance.
        #    """

        #    def get_object(self, pk):
        #        try:
        #            return Snippet.objects.get(pk=pk)
        #        except Snippet.DoesNotExist:
        #            raise Http404

        #    def get(self, request, pk, format=None):
        #        snippet = self.get_object(pk)
        #        serializer = SnippetSerializer(snippet)
        #        return Response(serializer.data)

        #    def put(self, request, pk, format=None):
        #        snippet = self.get_object(pk)
        #        serializer = SnippetSerializer(snippet, data=request.data)
        #        if serializer.is_valid():
        #            serializer.save()
        #            return Response(serializer.data)
        #        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #    def delete(self, request, pk, format=None):
        #        snippet = self.get_object(pk)
        #        snippet.delete()
        #        return Response(status=status.HTTP_204_NO_CONTENT)
