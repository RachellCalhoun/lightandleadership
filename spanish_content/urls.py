from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^nuestrahistoria$', views.our_story, name='our_story'),
    url(r'^nuestroequipo$', views.our_team, name='our_team'),
    url(r'^ninos$', views.childrens_program, name='childrensprogram'),
    url(r'^aplicar$', views.apply, name='apply'),
    url(r'^jovenes$', views.teens_program, name='teensprogram'),
    url(r'^mujeres$', views.womens_program, name='womensprogram'),
    url(r'^artesanas$', views.artisan_program, name='artisanprogram'),
    url(r'^etica$', views.ethical_post, name='ethical_page'),
    url(r'^peru$', views.why_peru, name='peru'),
    url(r'^voluntariadoperu$', views.volunteer_peru, name='volunteer_peru'),
    url(r'^finanzas$', views.financials, name='financials'),
    url(r'^donaciones$', views.donations, name='donations'),
    url(r'^chicago$', views.volunteer_chicago, name='volunteer_chicago'),
    url(r'^dona$', views.donate, name='donate'),
]
