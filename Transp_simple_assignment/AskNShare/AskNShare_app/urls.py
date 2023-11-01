from django.urls import path

from AskNShare_app import views

urlpatterns = [
    path('',views.login_function,name='log'),
    path('login_read',views.login_read_fun),
    path('register',views.register_fun,name='reg'),
    path('reg_read',views.reg_redata),
    path('home',views.home_function,name='home'),
    path('addq',views.add_question,name='aq'),
    path('read_addq',views.add_question_read),
    path('answer',views.answer_fun,name='ans'),
    path('ansread/<int:id>',views.read_answer,name='ar'),
    path('log_out',views.logout_fun,name='log_out'),
    path('view_ans/<int:id>',views.view_ans_fun,name='va'),
    path('create_ans/<int:id>',views.create_ans_fun,name='create_ans'),
    path('like_ans/<int:id>',views.like_an_fun,name='la'),
    path('like_read/<int:id>',views.like_read_fun,name='like_read')
    ]