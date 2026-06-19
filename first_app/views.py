from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from .tasks import test_task
# from decouple import config
# Create your views here.

def index(request):
    # test_task.delay() okf

    return HttpResponse(f'HHM.....Hello World! This is CN Django Test.By - Harsh Kanani aa.....web hooks test harsh kanani webhook testing 123 - harsh43')


# ---------------------------------------------------------------------------
# T3: OOM Kill (exit 137)
# ---------------------------------------------------------------------------
def trigger_oom(request):
    """T3: Allocate memory until the container is OOM-killed (exit 137)."""
    chunks = []
    while True:
        chunks.append(b'\x00' * (50 * 1024 * 1024))  # 50MB per chunk


# ---------------------------------------------------------------------------
# T4: Database Unreachable
# ---------------------------------------------------------------------------
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


# ---------------------------------------------------------------------------
# T6: Missing Environment Variable
# ---------------------------------------------------------------------------
def trigger_missing_env(request):
    """T6: Access a required env var that doesn't exist — crashes with KeyError."""
    import os
    value = os.environ['THIS_ENV_VAR_DOES_NOT_EXIST_12345']
    return HttpResponse(value)


# ---------------------------------------------------------------------------
# T7: Disk Full
# ---------------------------------------------------------------------------
def trigger_disk_full(request):
    """T7: Write to disk until 'No space left on device' crashes the process."""
    import os
    path = '/tmp/disk_fill_test'
    os.makedirs(path, exist_ok=True)
    i = 0
    while True:
        with open(f'{path}/chunk_{i}.bin', 'wb') as f:
            f.write(b'\x00' * (100 * 1024 * 1024))  # 100MB per file
        i += 1


# ---------------------------------------------------------------------------
# T8: Segfault (exit 139)
# ---------------------------------------------------------------------------
def trigger_segfault(request):
    """T8: Dereference null pointer — container dies with exit 139 (SIGSEGV)."""
    import ctypes
    ctypes.string_at(0)


# ---------------------------------------------------------------------------
# T9: Circuit Breaker (crash 5x rapidly)
# ---------------------------------------------------------------------------
def trigger_rapid_crash(request):
    """T9: Crash immediately — call this 5+ times to trigger circuit breaker."""
    import sys
    sys.exit(1)


# ---------------------------------------------------------------------------
# T14: Hang (healthcheck fails → unhealthy)
# ---------------------------------------------------------------------------
def trigger_hang(request):
    """T14: Hang forever — healthcheck will fail and report unhealthy."""
    import time
    time.sleep(999999)
    return HttpResponse('unreachable')


# ---------------------------------------------------------------------------
# T16: Image Unavailable (simulate by importing non-existent module)
# ---------------------------------------------------------------------------
def trigger_import_error(request):
    """T16: Import a module that doesn't exist — simulates broken image/dependency."""
    import non_existent_module_that_will_never_exist  # noqa: F401
    return HttpResponse('unreachable')


# ---------------------------------------------------------------------------
# T17: Startup Crash Loop (crash within 5s of boot)
# ---------------------------------------------------------------------------
def trigger_startup_crash(request):
    """T17: Exit immediately to simulate a startup crash loop."""
    import os
    os._exit(1)


# ---------------------------------------------------------------------------
# Proactive: Memory Pressure (allocate ~85% of limit without crashing)
# ---------------------------------------------------------------------------
def trigger_memory_pressure(request):
    """Allocate memory gradually to push container toward memory limit without OOM.
    The health agent should detect high memory usage and send a proactive alert.
    """
    mb = int(request.GET.get('mb', '200'))
    chunks = []
    for _ in range(mb):
        chunks.append(b'\x00' * (1024 * 1024))  # 1MB per chunk
    return JsonResponse({
        'status': 'allocated',
        'mb_held': mb,
        'message': f'Holding {mb}MB in memory. Health agent should detect memory_pressure.',
    })


# ---------------------------------------------------------------------------
# Proactive: CPU Throttling (spin CPU to 100%)
# ---------------------------------------------------------------------------
def trigger_cpu_spike(request):
    """Burn CPU for N seconds to trigger CPU throttling alert.
    The health agent should detect high CPU and send a proactive alert.
    """
    import time
    seconds = int(request.GET.get('seconds', '60'))
    end_time = time.time() + seconds
    while time.time() < end_time:
        _ = sum(i * i for i in range(10000))
    return JsonResponse({
        'status': 'done',
        'cpu_burn_seconds': seconds,
        'message': f'CPU burned for {seconds}s. Health agent should have detected cpu_throttled.',
    })


# ---------------------------------------------------------------------------
# Proactive: Disk Pressure (fill disk to ~85% without crashing)
# ---------------------------------------------------------------------------
def trigger_disk_pressure(request):
    """Write files to push disk toward threshold without filling completely.
    The health agent should detect disk_pressure proactively.
    """
    import os
    mb = int(request.GET.get('mb', '500'))
    path = '/tmp/disk_pressure_test'
    os.makedirs(path, exist_ok=True)
    for i in range(mb // 50):
        with open(f'{path}/chunk_{i}.bin', 'wb') as f:
            f.write(b'\x00' * (50 * 1024 * 1024))  # 50MB per file
    return JsonResponse({
        'status': 'written',
        'mb_written': mb,
        'message': f'Wrote ~{mb}MB to disk. Health agent should detect disk_pressure.',
    })


# ---------------------------------------------------------------------------
# Proactive: Port Conflict
# ---------------------------------------------------------------------------
def trigger_port_conflict(request):
    """T5-alt: Bind to a port that's already in use — causes EADDRINUSE crash."""
    import socket
    port = int(request.GET.get('port', '8000'))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 0)
    s.bind(('0.0.0.0', port))
    s.listen(1)
    # Now try to bind again — will fail
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind(('0.0.0.0', port))
    return HttpResponse('unreachable')
