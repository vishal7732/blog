from django.contrib import admin
from django.urls import path, include
from post.views import index, blog, post, search
from myapp.views import myapp, login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('blog/', blog, name='post_list'),
    path('search/', search, name='search'),
    path('post/<id>/', post, name='post_detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('login', login),
    path('myapp', myapp),
    path('logout', include('myapp.urls')),
    #path('reset_pass', reset_pass),
    path('signup', myapp, name="home"),
    path('login', login, name="login"),
    path('logout', logout, name="logout"),
    path('reset_pass/', auth_views.PasswordResetView.as_view(template_name="reset_pass.html"), name="reset_pass"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),
         name="password_reset_confirm"),
   
    #path('reset_password_complete',
        # auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),
       #  name="password_reset_complete"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)