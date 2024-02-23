
from django.contrib import admin
from django.urls import path
from realestateapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),
    path('agent-single.html/', views.agent, name = 'agent-single'),
    path('agents-grid.html/', views.agents, name = 'agents-grid'),
    path('blog-grid.html/', views.blogg, name = 'blog-grid'),
    path('blog-single.html/', views.blogs, name = 'blog-single'),
    path('contact.html/', views.contact, name = 'contact'),
    path('about.html/', views.about, name = 'about'),
    path('property-grid.html/', views.propertyg, name = 'property-grid'),
    path('property-single.html/', views.propertys, name = 'property-single'),

]
