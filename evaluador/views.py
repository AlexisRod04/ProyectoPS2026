from django.db import connection
from django.db.utils import OperationalError
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> HOLA </h1>")

def evaluador_sis(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return HttpResponse("OK")

    except OperationalError:
        return HttpResponse("ERROR", status=503)

def login(request):
    return HttpResponse("Login page")