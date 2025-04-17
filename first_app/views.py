from django.shortcuts import render
from django.http import HttpResponse
import os
# from .tasks import test_task
# from decouple import config
# Create your views here.

def index(request):
    # test_task.delay()

    # Accessing an environment variable
    debug_mode = os.environ.get('DEBUG', 'Not Set')

    return HttpResponse(f'HHM.....Hello World! This is CN Django Test.By - Harsh Kanani aa.....web hooks test harsh kanani webhook testing 123 - harsh43 {debug_mode}\n')