from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomuserModel(AbstractUser):

    USER_LIST = [
        ("Job_Seeker","Job_Seeker"),
        ("Recruiter","Recruiter"),
    ]

    display_name = models.CharField(null=True, max_length=50)
    user_type = models.CharField(choices=USER_LIST, max_length=50)


class SkillModel(models.Model):
    name = models.CharField(max_length=50,unique=True)
    
    def __str__(self):
        return self.name or "No Skills"

    
class RecruiterProfileModel(models.Model):
    user = models.OneToOneField(CustomuserModel, on_delete=models.CASCADE)
    name = models.CharField(null=True, max_length=50)
    company = models.CharField(null=True, max_length=50)
    phone = models.CharField(null=True, max_length=50)
    address = models.CharField(null=True, max_length=50)
    image = models.ImageField(upload_to="media/profile", max_length=None,null=True)

    def __str__(self):
        return self.name
    

    
class JobSeekerProfileModel(models.Model):
    user = models.OneToOneField(CustomuserModel, on_delete=models.CASCADE) 
    name = models.CharField(null=True, max_length=50)   
    phone = models.CharField(null=True, max_length=50)
    address = models.CharField(null=True, max_length=50)
    skill_set = models.ManyToManyField(SkillModel,blank=True)
    image = models.ImageField(upload_to="media/profile", max_length=None,null=True)
    resume = models.FileField(upload_to="media/resume", max_length=None,null=True)

    def __str__(self):
        return self.name 
    

class JobPostModel(models.Model):
    CATEGORY=[
        ("Full-Time","Full-Time"),
        ("Part-Time","Part-Time"),
        ("Remote","Remote"),
        ("Hybrid","Hybrid"),
    ]
    user = models.ForeignKey(RecruiterProfileModel, on_delete=models.CASCADE)
    title = models.CharField(null=True, max_length=50)
    opening = models.CharField(null=True, max_length=50)
    description = models.TextField(null=True)
    category = models.CharField(choices=CATEGORY, max_length=50,null=True)
    skill_set = models.ManyToManyField(SkillModel,blank=True)


    def __str__(self):
        return self.title or "Empty"


 
class ApplyModel(models.Model):
    STATUS=[
        ("Pending","Pending"),
        ("ShortListed","ShortListed"),
        ("Rejected","Rejected"),
        ("Hired","Hired"),
    ]
    applicant = models.ForeignKey(JobSeekerProfileModel, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPostModel,on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=50,default='Pending')
