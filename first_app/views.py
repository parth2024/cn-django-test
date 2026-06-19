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
