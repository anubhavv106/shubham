from django.shortcuts import render
from .models import Book, BookProvider, BookAccomplishment, Awards, ProjectType, Project, Publication, Certification, Webinar, Article, Copyright, Patent, BookReviewed, TeachingExperience, ProfessionalMembership, PaperReviewed, CurriculumDevelopment, Orientation, Judge, InternationalIV, OtherMembershipType, OtherMembership, ResearchGrant ,Slideshow,Intro

# Create your views here.
def index(request):
    books = Book.objects.all()
    awards = Awards.objects.all()  
    booksprovider = BookProvider.objects.all()  
    project_types = ProjectType.objects.all()  
    projects = Project.objects.all()  
    publications = Publication.objects.all()
    slideshow = Slideshow.objects.all()

    data = {
        "books": Book.objects.all(), 
        "booksprovider": BookProvider.objects.all(), 
        "awards": Awards.objects.all(), 
        "project_types": ProjectType.objects.all(), 
        "projects": Project.objects.all(), 
        "publications": Publication.objects.all(),
        "certifications": Certification.objects.all(),
        "webinars": Webinar.objects.all(),
        "articles": Article.objects.all(),
        "copyrights": Copyright.objects.all(),
        "patents": Patent.objects.all(),
        "booksreviewed": BookReviewed.objects.all(),
        "teachingexperiences": TeachingExperience.objects.all(),
        "professionalmemberships": ProfessionalMembership.objects.all(),
        "papersreviewed": PaperReviewed.objects.all(),
        "curriculumsdevelopments": CurriculumDevelopment.objects.all(),
        "orientations": Orientation.objects.all(),
        "judges": Judge.objects.all(),
        "internationalivs": InternationalIV.objects.all(),
        "othermembershiptypes": OtherMembershipType.objects.all(),
        "othermemberships": OtherMembership.objects.all(),
        "grants": ResearchGrant.objects.all(),
        "slideshows": Slideshow.objects.all(),
        "intro": Intro.objects.all(),
        # "av":Av.objects.all()
    }

    return render(request, 'index.html', data)

def book(request, book_id):
    book = Book.objects.get(pk=book_id)
    booksprovider = BookProvider.objects.filter(book=book) 
    accomplishments = BookAccomplishment.objects.filter(book=book) 
    return render(request, 'book-info.html',{"book":book,"providers":booksprovider, "accomplishments":accomplishments,"slideshow":Slideshow}) 