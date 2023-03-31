from django.urls import path
from . import views

urlpatterns = [
    path('chat-box/', views.ChatBox.as_view({'get':'chat_page'}), name='chat_page'),
    path('login/', views.LogIn.as_view({'post':'log_in', 'get':'log_in_form'}), name='log_in'),
    path('logout/', views.LogOut.as_view({'get':'log_out'}), name='log_out'),
]