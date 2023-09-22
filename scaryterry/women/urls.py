from django.urls import path

from women import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>', views.show_category, name='category')
]
