from django.conf.urls import url
from .views import ListJuntas
#ShowBook, ListAllBooks

urlpatterns = [
	url(r'^juntas/$', ListJuntas.as_view()),
]