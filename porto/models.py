from django.db import models
# bahasa
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
# Create your models here.
class Portofolio(models.Model):
    title = models.CharField(max_length=255) # judul project
    description = models.TextField()  # deskripsi project
    image = models.ImageField(upload_to='project/images/') # preview dari program
    tags = models.ManyToManyField(Tag, related_name='Portofolio', blank=True)  # bahasa yang digunkan
    demo = models.TextField() #link hosting
    link = models.TextField() #link github

    def __str__(self):
        return self.title
    
class Job(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    
class Profil(models.Model):
    nama = models.CharField(max_length=255) # judul project
    # tags = models.ManyToManyField(Tag, related_name='job', blank=True)  # bahasa yang digunkan
    description = models.TextField()  # deskripsi project
    image = models.ImageField(upload_to='project/profil/') # preview dari program
    # tags = models.ManyToManyField(Tag, related_name='bahasa', blank=True)  # bahasa yang digunkan
    # demo = models.TextField() #link hosting
    # link = models.TextField() #link github

    def __str__(self):
        return self.title
# klo bisa integrasikan dengan font awesome jadi bisa langsung pilih
# class Skill(models.Model):
#     icon = models.ImageField(upload_to='icon/images/') # preview dari program
#     name = models.TextField()  # nama skill
#     description = models.TextField()  # deskripsi skill

#     def __str__(self):
#         return self.name
    
# class Footer(models.Model):
#     icon = models.ImageField(upload_to='icon/images/') # preview dari program
#     name = models.TextField()  # nama skill
#     title = models.CharField(max_length=255) # judul project
#     description = models.TextField()  # deskripsi project
    
#     def __str__(self):
#         return self.name