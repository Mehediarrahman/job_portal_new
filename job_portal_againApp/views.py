from django.shortcuts import redirect,render
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required


def registerPage(request):

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully")
            return redirect('login')

    form = CreateUserForm()
    context = {
        'form':form,
        'btn':"Register",
        'form_title':"Create New Account",
    }
    return render(request,"auth/baseForm.html",context)

def loginPage(request):

    if request.method == "POST":
        form = AuthForm(request,request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            messages.success(request,"Logged in Successfully")
            return redirect("dashboard")

    form = AuthForm()
    context = {
        'form':form,
        'btn':"Login",
        'form_title':"Login Here",
    }
    return render(request,"auth/baseForm.html",context)
def logoutPage(request):
    logout(request)
    return redirect("login")
@login_required
def dashboardPage(request):

    job_data = JobPostModel.objects.all()


    context = {
        'job_data':job_data
    }

    return render(request,'pages/dashboard.html',context)

@login_required
def recruiterProfilePage(request):
    try:
        recruiter = RecruiterProfileModel.objects.get(user=request.user)
    except RecruiterProfileModel.DoesNotExist:
        recruiter = RecruiterProfileModel.objects.create(user=request.user)

    if request.method == "POST":
        form = RecruiterProfileForm(request.POST,request.FILES, instance=recruiter)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect("dashboard")

    form = RecruiterProfileForm(instance=recruiter)
    context = {
        'form':form,
        'btn':"Update",
        'form_title':"Update Recruiter Profile",
    }
    return render(request,'pages/baseForm.html',context)

@login_required
def jobSeekerProfilePage(request):
    try:
        jobSeeker = JobSeekerProfileModel.objects.get(user=request.user)
    except JobSeekerProfileModel.DoesNotExist:
        jobSeeker = JobSeekerProfileModel.objects.create(user=request.user)

    if request.method == "POST":
        form = JobSeekerProfileForm(request.POST,request.FILES, instance=jobSeeker)
        if form.is_valid():
            form.save()
            messages.success(request,"Profile Updated Successfully")
            return redirect("dashboard")

    form = JobSeekerProfileForm(instance=jobSeeker)
    context = {
        'form':form,
        'btn':"Update",
        'form_title':"Update Seeker Profile",
    }
    return render(request,'pages/baseForm.html',context)


@login_required
def jobPostPage(request):
    try:
        recruiter = RecruiterProfileModel.objects.get(user=request.user)
    except RecruiterProfileModel.DoesNotExist:
        recruiter = RecruiterProfileModel.objects.create(user=request.user)

    if request.user.user_type == "Recruiter":
        if request.method =="POST":
            form = JobPostForm(request.POST,request.FILES)
            if form.is_valid():
                data = form.save(commit=False)
                data.user = recruiter
                data.save()
                form.save_m2m() #Important for manyTomanyField
                messages.success(request,'Job Posted')
                return redirect("dashboard")
    form = JobPostForm()
    context={
        'form':form,
        'form_title':"Post A Job",
        'btn':"Post"
    }
    return render(request,"pages/baseForm.html",context)

@login_required
def skillPage(request):
    
   
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():         
            form.save()            
            messages.success(request,'Skill Added')
            return redirect("dashboard")

    form = SkillForm()
    context={
        'form':form,
        'form_title':"Add A Skill",
        'btn':"Add"
    }
    return render(request,"pages/baseForm.html",context)

@login_required
def applyJobPage(request,id):
    job = JobPostModel.objects.get(id=id)
    try:
        applicant = JobSeekerProfileModel.objects.get(user=request.user)
    except JobSeekerProfileModel.DoesNotExist:
        messages.error(request,"Update your profile First")
        return redirect('jobSeeker')

    if request.user.user_type == "Job_Seeker":
        if applicant and job:
            ApplyModel.objects.create(
            applicant = applicant,
            job = job,
            status = 'Pending'
        )
        messages.success(request,"Successfully Applied")
        

    return redirect("dashboard")


@login_required
def applicantList(request):
    try:
        recruiter = RecruiterProfileModel.objects.get(user = request.user)
    except RecruiterProfileModel.DoesNotExist:
        recruiter = RecruiterProfileModel.objects.create(user = request.user)
    if recruiter:
        Apply = ApplyModel.objects.filter(job__user = recruiter)

    context = {
        'Apply':Apply
    }
    return render(request,'pages/list.html',context)

@login_required
def myApplicantions(request):
    try:
        seeker = JobSeekerProfileModel.objects.get(user = request.user)
    except JobSeekerProfileModel.DoesNotExist:
        messages.warning(request,"update Your Profile")
        return redirect('jobSeeker')
    if seeker:
        myApplications = ApplyModel.objects.filter(applicant = seeker)

    context = {
        'myApplications':myApplications
    }
    return render(request,'pages/my_list.html',context)

@login_required
def shortListPage(request,id):

    apply_id = ApplyModel.objects.get(id=id)
    apply_id.status = "ShortListed"
    apply_id.save()

    return redirect('applicantList')

@login_required
def rejectPage(request,id):

    apply_id = ApplyModel.objects.get(id=id)
    apply_id.status = "Rejected"
    apply_id.save()

    return redirect('applicantList')


# skill Match
@login_required
def skillMatchingPage(request):

    try:
        user = JobSeekerProfileModel.objects.get(user = request.user)
    except JobSeekerProfileModel.DoesNotExist:
        return redirect('jobSeeker')   
    if user:
        user_skill =  user.skill_set.all()

        jobs = JobPostModel.objects.filter(skill_set__in = user_skill).distinct()
    
    context={
        'jobs':jobs
    }
    


    
    return render(request,'pages/Skill_dashbaord.html',context)