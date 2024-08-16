from django.utils.deprecation import MiddlewareMixin
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser
from django.urls import resolve

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        current_url = resolve(request.path_info).url_name

        if current_url == 'admin:index' or request.path.startswith('/admin/'):
            return  # Skip JWT authentication for admin URLs

        try:
            user_authenticator = JWTAuthentication()
            user, token = user_authenticator.authenticate(request)
            request.user = user if user is not None else AnonymousUser()
        except Exception as e:
            request.user = AnonymousUser()  # Fall back to an anonymous user if authentication fails
