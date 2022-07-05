from django.contrib import admin
from django.urls import path
from blog import views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = 'home'),
    path('new/',views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('detail/<int:blog_id>',views.detail, name= 'detail'),
    path('makecomment/<int:blog_id>',views.makecomment, name= 'makecomment'),
    path('login/', accounts_views.login ,name='login'),
    path('logout/', accounts_views.logout ,name='logout')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
