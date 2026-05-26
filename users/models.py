# users/models.py

from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# =====================================================
# PERFIL DE USUARIO
# =====================================================
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField(default='Mi biografía.', max_length=500, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.avatar.path)
            if img.height > 100 or img.width > 100:
                new_img = (100, 100)
                img.thumbnail(new_img)
                img.save(self.avatar.path)
        except FileNotFoundError:
            pass


# =====================================================
# HISTORIAL DE CONSULTAS DE GUÍAS
# =====================================================
class HistorialGuia(models.Model):
    consulta_id = models.IntegerField(default=1)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_guia = models.CharField(max_length=200)
    fecha = models.CharField(max_length=50, null=True, blank=True)
    hora = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=255, null=True, blank=True)
    sucursal = models.CharField(max_length=255, null=True, blank=True)
    fecha_consulta = models.DateTimeField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero_guia} - {self.estado}"


# =====================================================
# SPRINT 4 - SEGURIDAD, LOGS Y NOTIFICACIONES
# =====================================================
class IntentoLogin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150)
    intentos_fallidos = models.IntegerField(default=0)
    bloqueado_hasta = models.DateTimeField(null=True, blank=True)
    ultimo_intento = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} - {self.intentos_fallidos} intentos"


class ScrapingLog(models.Model):
    numero_guia = models.CharField(max_length=200)
    tipo_error = models.CharField(max_length=120, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_guia} - {self.tipo_error}"


class HistorialNotificacion(models.Model):
    numero_guia = models.CharField(max_length=200)
    canal = models.CharField(max_length=50)
    destinatario = models.CharField(max_length=255, blank=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    enviado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.numero_guia} - {self.canal} - {self.fecha}"

# =====================================================
# AUDITORÍA / LOG DE USABILIDAD
# =====================================================
class AuditoriaUsuario(models.Model):
    RESULTADOS = [
        ("exitoso", "Exitoso"),
        ("fallido", "Fallido"),
        ("bloqueado", "Bloqueado"),
        ("error", "Error"),
    ]

    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField(max_length=150, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    criterio = models.CharField(max_length=100)
    accion = models.CharField(max_length=180)
    resultado = models.CharField(max_length=20, choices=RESULTADOS, default="exitoso")
    detalle = models.TextField(blank=True)
    numero_guia = models.CharField(max_length=200, blank=True)
    ip = models.CharField(max_length=100, null=True, blank=True)
    metodo = models.CharField(max_length=10, blank=True)
    ruta = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        nombre = self.username or (self.usuario.username if self.usuario else "Anónimo")
        return f"{self.fecha:%Y-%m-%d %H:%M} - {nombre} - {self.accion}"
