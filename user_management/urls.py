from django.contrib import admin

from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views
# ⬅️ IMPORTACIONES ACTUALIZADAS
from users.views import VistaAccesoPersonalizada, VistaRestablecerContrasena, VistaCambiarContrasena, cerrar_sesion 

# ⬅️ IMPORTACIÓN ACTUALIZADA
from users.forms import FormularioAcceso 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),

    # ⬅️ USO DE VISTA Y FORMULARIO ACTUALIZADOS
    path('login/', VistaAccesoPersonalizada.as_view(redirect_authenticated_user=True, template_name='users/login.html',
                                           authentication_form=FormularioAcceso), name='login'),

    path('logout/', cerrar_sesion, name='logout'),

    # ⬅️ USO DE VISTA ACTUALIZADA
    path('password-reset/', VistaRestablecerContrasena.as_view(), name='password_reset'),

    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),

    # ⬅️ USO DE VISTA ACTUALIZADA
    path('password-change/', VistaCambiarContrasena.as_view(), name='password_change'),

    re_path(r'^oauth/', include('social_django.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)