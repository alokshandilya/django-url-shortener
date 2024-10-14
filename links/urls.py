from django.urls import path

from .views import add_link, index, root_link

urlpatterns = [
    path("", index, name="index"),
    path("<slug:link_slug>/", root_link, name="root-link"),
    path("link/create", add_link, name="create-link"),
]
