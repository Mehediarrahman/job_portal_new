from django.urls import path
from .views import *
urlpatterns = [
    path('',registerPage,name='register'),
    path('login/',loginPage,name='login'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('recruiter/',recruiterProfilePage,name='recruiter'),
    path('jobSeeker/',jobSeekerProfilePage,name='jobSeeker'),
    path('jobPost/',jobPostPage,name='jobPost'),
    path('addSkill/',skillPage,name='addSkill'),
    path('logout/',logoutPage,name='logout'),
    path('applyJob/<int:id>/',applyJobPage,name='applyJob'),
    path('changeStatus/<int:id>/',changeStatusPage,name='changeStatus'),
    path('myJobPage/',myJobPage,name='myJobPage'),

]
