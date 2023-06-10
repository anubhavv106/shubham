from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    authors = models.CharField(max_length=200, null=True)
    isbn = models.CharField(max_length=200, null=True)
    pages = models.CharField(max_length=200, null=True)
    extra_message = models.CharField(max_length=200, null=True)
    introduction = models.TextField(null = True)
    picture_main = models.ImageField(upload_to='static/images/books/')
    picture_extra = models.ImageField(upload_to='static/images/books/', null=True)
    date_of_publish = models.CharField(max_length=200, null=True)
    

    def __str__(self):
        return self.title

class BookAccomplishment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    point = models.TextField(null=True)

class BookProvider(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.CharField(max_length=200, null=True)
    link = models.URLField(max_length=200, null=True)

class Awards(models.Model):
    name = models.CharField(max_length=255,null=True)
    picture = models.ImageField(upload_to='static/images/awards')
    description = models.TextField(null=True)
    linkSite = models.URLField(max_length=255, null=True)
    site=models.CharField(max_length=255, null=True)
    category=models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    
class ProjectType(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    project_type = models.ForeignKey(ProjectType, on_delete=models.CASCADE, help_text="This is an html rendered field, you can add anchor and paragraph tags here. This will be rendered to the frontend")
    data = models.TextField(null=True)

    def __str__(self):
        return str(self.data)


class Publication(models.Model):
    data = models.TextField(null=True, help_text="This is an html rendered field, you can add anchor and paragraph tags here. This will be rendered to the frontend")

    def __str__(self):
        return str(self.data)

class Webinar(models.Model):
    title = models.CharField(max_length=255,null=True)
    youtube_embed_code = models.CharField(max_length=255,null=True, help_text="Please enter the youtube embed code, it will look like \"2fIo1WH5bcg\", please do not enter all the embed code.")
    date = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.title)

class Article(models.Model):
    title = models.CharField(max_length=255,null=True)
    date = models.CharField(max_length=255,null=True)
    link = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.title)

class Copyright(models.Model):
    data = models.TextField(null=True)
    link = models.CharField(max_length=255,null=True, blank=True)
    def __str__(self):
        return str(self.data)

class Certification(models.Model):
    name = models.CharField(max_length=255,null=True)
    picture = models.ImageField(upload_to='static/images/certifications')
    date = models.CharField(max_length=255,null=True)
    expiration_date = models.CharField(max_length=255,null=True)
    certification_no = models.CharField(max_length=255,null=True)

    def __str__(self):
        return str(self.name)

class Patent(models.Model):
    title = models.TextField(null=True)

    def __str__(self):
        return str(self.title)
    


# Models for interaction section

class TeachingExperience(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class BookReviewed(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class ProfessionalMembership(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class OtherMembershipType(models.Model):
    title = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title

class OtherMembership(models.Model):
    membership_type = models.ForeignKey(OtherMembershipType, on_delete=models.CASCADE)
    data = models.TextField(null=True, help_text="This is an html rendered field, you can add anchor and paragraph tags here. This will be rendered to the frontend")

    def __str__(self):
        return str(self.data)

class PaperReviewed(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class CurriculumDevelopment(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

ASSISTANCE_CHOICES = (
    ("Resource Person", "Resource Person"),
    ("Organized", "Organized"),
    ("Attended", "Attended"),
)

class Orientation(models.Model):
    type_of_work = models.CharField(
        max_length = 255,
        choices = ASSISTANCE_CHOICES,
        default = 'Organized'
    )
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class Judge(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)

class InternationalIV(models.Model):
    data = models.TextField(null=True, help_text="This will be rendered as html in the frontend")

    def __str__(self):
        return str(self.data)
 
class Slideshow(models.Model):
    title = models.CharField(max_length=255,null=True)
    img = models.ImageField(upload_to='static/uploads')
    img1 = models.ImageField(upload_to='static/uploads')
    img2 = models.ImageField(upload_to='static/uploads')
    img3 = models.ImageField(upload_to='static/uploads')
    img4 = models.ImageField(upload_to='static/uploads')
    img5 = models.ImageField(upload_to='static/uploads')
    
    # def __str__(self):
    #     return self.title


# Research Grants
class ResearchGrant(models.Model):
    date = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255,null=True)
    amount = models.CharField(max_length=255,null=True)
    grant_from = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)


class Intro(models.Model):
     = models.CharField(max_length=255,null=True)
    title1 = models.CharField(max_length=255,null=True)
    title1_1 = models.CharField(max_length=255,null=True)
    title1_2 = models.CharField(max_length=255,null=True)
    title1_3 = models.CharField(max_length=255,null=True)
    title1_4 = models.CharField(max_length=255,null=True)
    title1_5= models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    more= models.CharField(max_length=255,null=True)
    more_link = models.URLField(max_length=100,null=True)

    
    




