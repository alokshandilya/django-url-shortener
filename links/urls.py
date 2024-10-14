from django.urls import path

from .views import index, root_link

urlpatterns = [
    path("", index, name="index"),
    path("<slug:link_slug>/", root_link, name="root_link"),
]
