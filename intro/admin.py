
from django.contrib import admin
from .models import HomeContent,AboutContent,Download,Education,Skill,Description,Certification,Project,ContactInfo

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ['heading', 'home_background', 'home_photo', 'Eng_content','created_at']
    list_display_links = list_display

@admin.register(AboutContent)
class AboutContentAdmin(admin.ModelAdmin):
    list_display = ['about_title', 'about_background', 'text_up', 'text_down','about_photo','created_at']
    list_display_links = list_display

@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ['download','created_at']
    list_display_links = list_display

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree_title','school_name','graduation_date','award']
    list_display_links = list_display

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_icon','skill_name','skill_level']
    list_display_links = list_display

@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['desc_title','description']
    list_display_links = list_display

@admin.register(Certification)
class DescriptionAdmin(admin.ModelAdmin):
    list_display = ['certification']
    list_display_links = list_display

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title','project_description','completion_date','project_images','project_url']
    list_display_links = list_display

@admin.register(ContactInfo)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['email','phone1','phone2']
    list_display_links = list_display