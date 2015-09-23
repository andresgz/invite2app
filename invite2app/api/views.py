from invite2app.users.models import User
from rest_framework import viewsets
from invite2app.api.serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from invite2app.lib.facebook_auth import FacebookAuth, NotValidFacebookAccount
from rest_framework import status

from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FriendsUsingApp(APIView):
    """
    View to list all users using Application.
    * User has to be authenticated.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        try:
            if not request.user.is_authenticated():
                raise NotValidFacebookAccount("User needs to be authenticated")
            graph = FacebookAuth(request.user.id).get_graph()
            users = graph.get_connections(
                id='me', connection_name='friends', fields='name')
            data = users.get('data')
        except NotValidFacebookAccount:
            data = []

        return Response(data)

    def post(self, request):
        friends_ids = request.data.get('friends_ids')
        message = request.data.get('message', u'')
        graph = FacebookAuth(request.user.id).get_graph()

        message_text = u' - '.join([message, settings.INVITE_MESSAGE])
        try:
            graph.put_object(
                parent_object='me', connection_name='feed',
                message=str(message_text),
                tags=friends_ids)
        except Exception, e:
            return Response({'message': e.message},
                            status=status.HTTP_400_BAD_REQUEST)

        return Response({}, status=status.HTTP_201_CREATED)


class FacebookFriends(APIView):
    """
    Lists friends of the current user.
    * User has to be authenticated.
    """

    def get(self, request, format=None):
        """
        Return a list of all users.
        """

        after = request.GET.get('after', None)
        try:
            if not request.user.is_authenticated():
                raise NotValidFacebookAccount("User needs to be authenticated")
            graph = FacebookAuth(request.user.id).get_graph()
            users = graph.get_connections(
                id='me', connection_name='taggable_friends',
                fields='name,picture', limit='30', after=after)
            data = users
        except NotValidFacebookAccount:
            data = []

        return Response(data)
