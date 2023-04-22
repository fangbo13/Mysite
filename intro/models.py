from django.db import models

# Create your models here.
class HomeContent(models.Model):
    heading = models.CharField(max_length=200)
    home_background = models.ImageField(upload_to='home_background/')
    home_photo = models.ImageField(upload_to='home_photo/')
    Eng_content = models.CharField(max_length=200)
    Ire_content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

class AboutContent(models.Model):
    about_title = models.CharField(max_length=200)
    about_background = models.ImageField(upload_to='about_background/')
    text_up = models.CharField(max_length=200)
    text_down = models.CharField(max_length=200)
    about_photo = models.ImageField(upload_to='about_photo/')
    created_at = models.DateTimeField(auto_now_add=True)

class Download(models.Model):
    download = models.FileField(upload_to='download/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.download.name

    
class Education(models.Model):
    degree_title = models.CharField(max_length=100)
    school_name = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=100)
    award = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.degree_title} - {self.school_name}"


class Skill(models.Model):
    skill_icon = models.CharField(max_length=255)
    skill_name = models.CharField(max_length=255)
    skill_level = models.PositiveIntegerField()

    def __str__(self):
        return self.skill_name
    
class Description(models.Model):
    desc_title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.desc_title

class Certification(models.Model):
    certification = models.CharField(max_length=255)

    def __str__(self):
        return self.certification

class Project(models.Model):
    project_title = models.CharField(max_length=255)
    project_description = models.TextField()
    completion_date = models.DateField()
    custom_description = models.TextField() 
    project_images= models.ImageField(upload_to='project_images')
    project_url = models.CharField(max_length=255)
    
    def __str__(self):
        return self.project_title

