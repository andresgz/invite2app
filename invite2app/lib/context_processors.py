from django.conf import settings  # import the settings file


def context_settings(request):
    """
    Settings Context processor
    Send variables to the context of all templates.
    * APP_URL: Used in the JS Facebook dialogs
    * FACEBOOK_APP_ID: Facebook App's ID.
    """
    return {
        'SETTINGS': {
            'APP_URL': settings.APP_URL,
            'FACEBOOK_APP_ID': settings.FACEBOOK_APP_ID
            }
    }
