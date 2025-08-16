from django.http import HttpResponse


def health(request):
    """Health check endpoint that returns HTTP 200 OK"""
    return HttpResponse("OK", status=200)
