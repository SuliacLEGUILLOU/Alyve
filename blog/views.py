from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Comment, Category, Blog, Page, Question, Link, Social

from random import randint 

class IndexView(generic.ListView):
    model = Article
    template_name = 'index.html'
    pagined_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        articles = Article.objects.filter(published=True).order_by('-publication_date')
        paginator = Paginator(articles, self.pagined_by)

        page = self.request.GET.get('page')

        try:
            articles_page = paginator.page(page)
        except PageNotAnInteger:
            articles_page = paginator.page(1)
        except EmptyPage:
            articles_page = paginator.page(paginator.num_pages)

        context['articles'] = articles_page
        context['blog'] = Blog.objects.get(pk=1)
        context['pages'] = Page.objects.filter(displayed=True)
        context['categories'] = Category.objects.all()
        context['links'] = Link.objects.order_by('sort')
        context['social'] = Social.objects.order_by('sort')
        return context

class CategoryView(generic.ListView):
    
    template_name = 'category.html'
    
    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Article.objects.filter(published=True, category=self.category).order_by('-publication_date')

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=1)
        context['pages'] = Page.objects.filter(displayed=True)
        context['categories'] = Category.objects.all()
        context['links'] = Link.objects.order_by('sort')
        context['social'] = Social.objects.order_by('sort')
        context['category'] = self.category
        context['articles'] = self.get_queryset()
        del context['article_list']
        return context

class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'
    
    def get_context_data(self, **kwargs):
        context = super(ArticleView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=1)
        context['pages'] = Page.objects.filter(displayed=True)
        context['comments'] = Comment.objects.filter(article=self.object.id, valided=True).order_by('-pk')
        context['categories'] = Category.objects.all()
        context['links'] = Link.objects.order_by('sort')
        context['social'] = Social.objects.order_by('sort')

        # get a random question for comment something
        question_count = Question.objects.count()
        index = randint(0, question_count-1)
        if index is not None:
            context['question'] = Question.objects.all()[index]
        
        return context

class PageView(generic.DetailView):
    model = Page
    template_name = 'page.html'
    
    def get_context_data(self, **kwargs):
        context = super(PageView, self).get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(pk=1)
        context['pages'] = Page.objects.filter(displayed=True)
        context['categories'] = Category.objects.all()
        context['links'] = Link.objects.order_by('sort')
        context['social'] = Social.objects.order_by('sort')
        return context

def add_comment(request, slug):
    if request.method == 'POST':
        username = request.POST.get('comment_username', None)
        website = request.POST.get('comment_website', None)
        content = request.POST.get('comment_comment', None)
        answer = request.POST.get('comment_answer', None)
        question_id = int(request.POST.get('comment_question', None))

        if username and content and answer and question_id:
            question = Question.objects.get(pk=question_id)
            if answer == question.answer:
                article = Article.objects.get(slug=slug)
                comment = Comment(username=username, content=content, publication_date=timezone.now(), article=article)
                comment.save()

            return redirect(reverse('blog:article', args=[slug]))

    return redirect('article', slug=slug)