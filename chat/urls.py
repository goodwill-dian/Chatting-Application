from django.urls import path
from . import views

urlpatterns = [
    path('chat-box/', views.ChatBox.as_view({'get':'chat_page'}), name='chat_page'),
    path('login/', views.LogIn.as_view({'post':'log_in', 'get':'log_in_form'}), name='log_in'),
    path('chat-box/logout/', views.LogOut.as_view({'get':'log_out'}), name='log_out'),
    
    path('get-data/', views.get_data, name='user_name'),
    path('get-old-chat/', views.get_old_chat, name='old_chat')
]