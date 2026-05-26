from django.contrib import admin
from .models import Perfil, HistorialGuia, IntentoLogin, ScrapingLog, HistorialNotificacion, AuditoriaUsuario

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username', 'user__email')

@admin.register(HistorialGuia)
class HistorialGuiaAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'estado', 'fecha', 'hora', 'sucursal', 'fecha_consulta', 'usuario')
    list_filter = ('estado', 'sucursal', 'fecha_consulta')
    search_fields = ('numero_guia', 'usuario__username')

@admin.register(IntentoLogin)
class IntentoLoginAdmin(admin.ModelAdmin):
    list_display = ('username', 'intentos_fallidos', 'bloqueado_hasta', 'ultimo_intento')
    search_fields = ('username', 'usuario__username')

@admin.register(ScrapingLog)
class ScrapingLogAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'tipo_error', 'fecha')
    search_fields = ('numero_guia', 'mensaje')
    list_filter = ('tipo_error', 'fecha')

@admin.register(HistorialNotificacion)
class HistorialNotificacionAdmin(admin.ModelAdmin):
    list_display = ('numero_guia', 'canal', 'destinatario', 'fecha', 'enviado')
    search_fields = ('numero_guia', 'destinatario', 'mensaje')
    list_filter = ('canal', 'enviado', 'fecha')

@admin.register(AuditoriaUsuario)
class AuditoriaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'username', 'criterio', 'accion', 'resultado', 'numero_guia', 'ip')
    search_fields = ('username', 'criterio', 'accion', 'detalle', 'numero_guia')
    list_filter = ('criterio', 'resultado', 'fecha')
    readonly_fields = ('fecha',)
