from django.contrib import admin
<<<<<<< HEAD
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('company/', include('Company.urls'))
=======
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('Company.urls'))
>>>>>>> b9152bfd9817422afa7e5eeb815016a73a63bbb6
]
