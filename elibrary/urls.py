from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='library-home'),
    path('it_sems/', views.it_sems, name='library-it-sems'),
    path('cse_sems/', views.cse_sems, name='library-cse-sems'),
    path('ece_sems/', views.ece_sems, name='library-ece-sems'),
    path('eee_sems/', views.eee_sems, name='library-eee-sems'), 
    path('it_sem1/', views.it_sem1, name='library-it-sem1'), 
    path('it_sem2/', views.it_sem2, name='library-it-sem2'), 
    path('it_sem3/', views.it_sem3, name='library-it-sem3'), 
    path('it_sem4/', views.it_sem4, name='library-it-sem4'), 
    path('it_sem5/', views.it_sem5, name='library-it-sem5'), 
    path('it_sem6/', views.it_sem6, name='library-it-sem6'), 
    path('it_sem7/', views.it_sem7, name='library-it-sem7'), 
    path('cse_sem1/', views.cse_sem1, name='library-cse-sem1'), 
    path('cse_sem2/', views.cse_sem2, name='library-cse-sem2'), 
    path('cse_sem3/', views.cse_sem3, name='library-cse-sem3'), 
    path('cse_sem4/', views.cse_sem4, name='library-cse-sem4'), 
    path('cse_sem5/', views.cse_sem5, name='library-cse-sem5'), 
    path('cse_sem6/', views.cse_sem6, name='library-cse-sem6'), 
    path('cse_sem7/', views.cse_sem7, name='library-cse-sem7'), 
    path('ece_sem1/', views.ece_sem1, name='library-ece-sem1'), 
    path('ece_sem2/', views.ece_sem2, name='library-ece-sem2'), 
    path('ece_sem3/', views.ece_sem3, name='library-ece-sem3'), 
    path('ece_sem4/', views.ece_sem4, name='library-ece-sem4'), 
    path('ece_sem5/', views.ece_sem5, name='library-ece-sem5'), 
    path('ece_sem6/', views.ece_sem6, name='library-ece-sem6'), 
    path('ece_sem7/', views.ece_sem7, name='library-ece-sem7'), 
    path('it_sem3_DMA/',views.it_sem3_DMA, name='library-it-sem3-DMA'), 
    path('subjectview_sem3/', views.subjectview_sem3 , name='subjectview_sem3'),
    path('subjectview_sem1/', views.subjectview_sem1 , name='subjectview_sem1'),
    path('subjectview_sem2/', views.subjectview_sem2 , name='subjectview_sem2'),
    path('subjectview_sem4/', views.subjectview_sem4 , name='subjectview_sem4'),
    path('subjectview_sem5/', views.subjectview_sem5 , name='subjectview_sem5'),
    path('subjectview_sem6/', views.subjectview_sem6 , name='subjectview_sem6'),
    path('subjectview_sem7/', views.subjectview_sem7 , name='subjectview_sem7'),
    path('subjectview_sem8/', views.subjectview_sem8 , name='subjectview_sem8'),
    path('stackoverflow-home/',views.stack_home,name='stackoverflow-home'),
    path('detail/<int:id>',views.detail,name='stackoverflow-detail_page'),
    path('save-comment',views.save_comment,name='save-comment'),
    path('save-upvote',views.save_upvote,name='save-upvote'),
    path('save-downvote',views.save_downvote,name='save-downvote'),
    path('ask-question',views.ask_form,name='ask-question'),
    path('tag/<str:tag>',views.tag,name='tag'),
    path('profile/',views.profile,name='profile'),
    path('tags/',views.tags,name='tags'),
#    path('user/<str:username>', UserQuestionsListView.as_view(), name='user-qstns'),
    
  
]
