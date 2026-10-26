from django.db import connection
from django.db.utils import OperationalError
from django.http import HttpResponse


def evaluador_sis(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")

        return HttpResponse("OK")

    except OperationalError:
        return HttpResponse("ERROR", status=503)