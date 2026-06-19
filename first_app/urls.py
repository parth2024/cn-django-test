from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name='index'),

    # --- Crash triggers (reactive healing tests) ---
    path('oom/', views.trigger_oom, name='trigger_oom'),                        # T3
    path('db-crash/', views.trigger_db_crash, name='trigger_db_crash'),          # T4
    path('missing-env/', views.trigger_missing_env, name='trigger_missing_env'), # T6
    path('disk-full/', views.trigger_disk_full, name='trigger_disk_full'),       # T7
    path('segfault/', views.trigger_segfault, name='trigger_segfault'),          # T8
    path('rapid-crash/', views.trigger_rapid_crash, name='trigger_rapid_crash'), # T9
    path('hang/', views.trigger_hang, name='trigger_hang'),                      # T14
    path('import-error/', views.trigger_import_error, name='trigger_import_error'), # T16
    path('startup-crash/', views.trigger_startup_crash, name='trigger_startup_crash'), # T17

    # --- Proactive monitoring triggers ---
    path('memory-pressure/', views.trigger_memory_pressure, name='trigger_memory_pressure'),
    path('cpu-spike/', views.trigger_cpu_spike, name='trigger_cpu_spike'),
    path('disk-pressure/', views.trigger_disk_pressure, name='trigger_disk_pressure'),
    path('port-conflict/', views.trigger_port_conflict, name='trigger_port_conflict'),
]