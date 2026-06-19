from django.shortcuts import render
from django.http import HttpResponse
# from .tasks import test_task
# from decouple import config
# Create your views here.

def index(request):
    # test_task.delay() okf

    return HttpResponse(f'HHM.....Hello World! This is CN Django Test.By - Harsh Kanani aa.....web hooks test harsh kanani webhook testing 123 - harsh43')


def trigger_oom(request):
    """T3: Allocate memory until the container is OOM-killed (exit 137)."""
    chunks = []
    while True:
        chunks.append(b'\x00' * (50 * 1024 * 1024))  # 50MB per chunk


def trigger_segfault(request):
    """T8: Dereference null pointer — container dies with exit 139 (SIGSEGV)."""
    import ctypes
    ctypes.string_at(0)


def trigger_db_crash(request):
    """T4: Force a DB connection to a dead host — app crashes with connection refused."""
    import psycopg2
    psycopg2.connect(
        host='10.255.255.1',  # non-routable IP — guaranteed timeout/refused
        port=5432,
        dbname='fake',
        user='fake',
        password='fake',
        connect_timeout=3,
    )


def trigger_hang(request):
    """T14: Hang forever — healthcheck will fail and report unhealthy."""
    import time
    time.sleep(999999)
    return HttpResponse('unreachable')
