from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Ola django</body></html>', content_type='text/html')
