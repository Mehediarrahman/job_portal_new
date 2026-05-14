from django.urls import path
from .views import *
urlpatterns = [
    path('register/',registerPage,name='register'),
    path('',loginPage,name='login'),
    path('dashboard/',dashboardPage,name='dashboard'),
    path('recruiter/',recruiterProfilePage,name='recruiter'),
    path('jobSeeker/',jobSeekerProfilePage,name='jobSeeker'),
    path('jobPost/',jobPostPage,name='jobPost'),
    path('addSkill/',skillPage,name='addSkill'),
    path('logout/',logoutPage,name='logout'),
    path('applyJob/<int:id>/',applyJobPage,name='applyJob'),
    path('shortListPage/<int:id>/',shortListPage,name='shortListPage'), 
    path('rejectPage/<int:id>/',rejectPage,name='rejectPage'), 
    path('applicantList/',applicantList,name='applicantList'),
    path('myApplicantions/',myApplicantions,name='myApplicantions'),
    path('skillMatchingPage/',skillMatchingPage,name='skillMatchingPage'),

]
