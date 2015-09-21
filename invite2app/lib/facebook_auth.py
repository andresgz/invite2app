# -*- coding: utf-8 -*-
import facebook
from allauth.socialaccount.models import SocialToken
from django.core.exceptions import ObjectDoesNotExist


class FacebookAuth(object):
    """
    Interface bettween Django AllAuth and Facebook SDK
    """
    def __init__(self, user_id):
        super(FacebookAuth, self).__init__()
        # Only integers are allowed
        if not isinstance(user_id, (int, long)):
            raise TypeError("An Integer is expected")
        self.user_id = user_id

    def get_graph(self):
        """
        Returns a Graph object to be used on the Facebook SDK.
        """
        return facebook.GraphAPI(access_token=self.get_access_token())

    def get_access_token(self):
        """
        Get a valid token for the user from AllAuth
        """
        try:
            token = SocialToken.objects.get(
                account__user_id=self.user_id).token
        except ObjectDoesNotExist:
            raise NotValidFacebookAccount("A token has not been found")
        return token


class NotValidFacebookAccount(Exception):
    """
    NotValidAccount Exception.
    """
    pass
