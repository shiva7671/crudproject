from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib import admin
from django.urls import path
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home_view),
    path("employees/",views.table_view),
    path("insert/",views.insert_view),
    path("update/<int:id>",views.update_view),
    path("delete/<int:id>",views.delete_view),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
]
