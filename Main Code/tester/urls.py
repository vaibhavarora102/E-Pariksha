
from django.urls import path
from . import views
urlpatterns = [
    path('createMCQ10/', views.MCQ10TestCreateView.as_view(), name='MCQ10-Create'),
    path('createMCQ25/', views.MCQ25TestCreateView.as_view(), name='MCQ25-Create'),
    path('createQnA10/', views.QnA10TestCreateView.as_view(), name='MCQ10-Create'),

    # path('test-created/aes-128bit/1ewaHnLFDesfAnUr3LkQXk+OBjjqXTVy18e+PP66fDx4YD6FDgCTTbG9c2/ym6fW4FkFvIpAcWyKimVNuz/qvzM3EbHZoV4h19MTn2bjnxRTw8Gk7ZWkB8PSQjZtm7ntZ3XCoDH9S2oaQ46AU1yP8w==' , views.Created ,name='created'),
    
    path('', views.home, name='home'),
    path('home/', views.home_paper, name='home-paper'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('MCQ10/', views.giveMCQ10, name='MCQ10'),
    path('MCQ25/', views.giveMCQ25, name='MCQ25'),
    path('QnA10/', views.giveQnA10, name='QnA10'),

    path('test/', views.test, name='test'),


]

