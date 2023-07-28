from .models import loggers2


class middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        loggers2.objects.create(
            username=request.user,
            method=request.method,
            url_path=request.get_full_path(),
            auth=request.user.is_authenticated,
        )
        response = self.get_response(request)
        return response
