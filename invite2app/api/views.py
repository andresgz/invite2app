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
        print request.data
        graph = FacebookAuth(request.user.id).get_graph()
        print request.user.id
        try:
            graph.put_object(
                parent_object='me', connection_name='feed',
                message=settings.INVITE_MESSAGE,
                tags=friends_ids)
        except Exception, e:
            Exception(e)
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

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
        try:
            if not request.user.is_authenticated():
                raise NotValidFacebookAccount("User needs to be authenticated")
            graph = FacebookAuth(request.user.id).get_graph()
            users = graph.get_connections(
                id='me', connection_name='taggable_friends',
                fields='name,picture', after='QWFJUHpiQmszYlN4OE50aWh2RkVmaXRpTWFQcXVFVmpQWEYxSVoyY3dJNURNWTd5YzdHX3hkLUJjbG5BUzRJX3I0cl9SR05IT1EzcjhKQ2ZATWHMzck5Od0FTZA21yXy1GVjdiWjMtZA1VmQ1BzSkEZD')
            data = users
        except NotValidFacebookAccount:
            data = []

        return Response(data)
