from django.urls import path
from . import views
from django.contrib.auth import views as authviews
urlpatterns=[
    path('news',views.shownews,name='shownews'),
    path('login/',authviews.LoginView.as_view(),name='login'),
    path('logout',authviews.LogoutView.as_view(),name='logout'),
    path('billing',views.bill,name='billing'),
    path('',views.about,name='about'),
    path('news/<int:pk>/comment',views.add_comment,name="add_comment"),
    path('changepassword',authviews.PasswordChangeView.as_view(),name='changepassword'),
    path('changepassword/done',authviews.PasswordChangeDoneView.as_view(),name='passchangedone'),
]