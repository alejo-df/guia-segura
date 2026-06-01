from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Página principal
    path('', views.home, name='users-home'),

    # Registro
    path('register/', views.VistaRegistro.as_view(), name='users-register'),

    # Perfil
    path('profile/', views.profile, name='users-profile'),

    # Lista de usuarios
    path('users-list/', views.VistaListaUsuarios.as_view(), name='users-list'),

    # Consulta de guía
    path('track-guide/', views.VistaConsultarGuia, name='track-guide'),

    # Login / Logout
    path('login/', views.VistaAccesoPersonalizada.as_view(template_name='users/login.html', authentication_form=views.FormularioAcceso), name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),

    # --- PANEL USUARIOS ---
    path('panel/usuarios/', views.panel_usuarios, name='panel_usuarios'),
    path('panel/usuarios/<int:user_id>/', views.detalle_usuario, name='detalle_usuario'),
    path('panel/usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('panel/usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('panel/usuarios/eliminar/<int:user_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    path('panel/usuarios/cambiar-rol/<int:user_id>/<str:rol>/', views.cambiar_rol_usuario, name='cambiar_rol_usuario'),
    path('panel/usuarios/inactivos/', views.usuarios_inactivos, name='usuarios_inactivos'),
    path('panel/usuarios/activar/<int:user_id>/', views.activar_usuario, name='activar_usuario'),

    # --- PANEL GUÍAS ---
    path('panel/guias/', views.panel_guias, name='panel_guias'),
    path('panel/guias/<int:consulta_id>/', views.detalle_consulta, name='detalle_consulta'),
    path('panel/guias/<int:consulta_id>/crear-evento/', views.crear_evento, name='crear_evento'),
    path('panel/guias/<int:consulta_id>/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('panel/guias/<int:consulta_id>/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('panel/guias/<int:consulta_id>/inactivos/', views.detalle_consulta_inactivos, name='detalle_consulta_inactivos'),
    path('panel/guias/<int:consulta_id>/restaurar/<int:evento_id>/', views.restaurar_evento, name='restaurar_evento'),
    path('panel/guias/exportar/excel/', views.exportar_guias_excel, name='exportar_guias'),
    path('panel/guias/exportar/pdf/', views.exportar_guias_pdf, name='exportar_guias_pdf'),
    path('panel/guias/reporte/', views.exportar_guias_excel, name='reporte_guias'),

    # --- SPRINT 4: LOGS Y SEGURIDAD ---
    path('panel/logs/scraping/', views.panel_logs_scraping, name='panel_logs_scraping'),
    path('panel/logs/notificaciones/', views.panel_notificaciones, name='panel_notificaciones'),
    path('panel/logs/intentos/', views.panel_intentos_login, name='panel_intentos_login'),
    path('panel/logs/auditoria/', views.panel_auditoria_usuarios, name='panel_auditoria_usuarios'),
    path('panel/guias/<int:consulta_id>/ajax-eventos/', views.ajax_eventos_guia, name='ajax_eventos_guia'),
    path('panel/logs/intentos/desbloquear/<int:intento_id>/', views.desbloquear_cuenta, name='desbloquear_cuenta'),
    # --- USUARIO NORMAL ---
    path('mis-guias/excel/', views.mis_guias_excel, name='mis_guias_excel'),
    path('mis-guias/pdf/', views.mis_guias_pdf, name='mis_guias_pdf'),
    path('mis-notificaciones/', views.mis_notificaciones, name='mis_notificaciones'),
]