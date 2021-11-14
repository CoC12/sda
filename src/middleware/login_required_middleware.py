from django.conf import settings
from django.contrib.auth.views import redirect_to_login
from django.urls import resolve


class LoginRequiredMMiddleware():

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        if request.user.is_authenticated:
            return None
        if resolve(request.path).view_name in settings.LOGIN_REQUIRED_IGNORE_VIEWS:
            return None
        return redirect_to_login(
            next=request.path,
        )
