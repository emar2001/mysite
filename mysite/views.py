from django.http import HttpResponse

def http_test(request):
    return HttpResponse('http_test')