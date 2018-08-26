from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Blog

from blog.models import Article, Comment

class LatestArticlesFeed(Feed):
    blog = Blog.objects.get(pk=1)
    title = "Derniers articles sur " + blog.name
    description = "Derniers articles"
    link = "feeds/"

    def items(self):
        allArticles = Article.objects.order_by('-publication_date')
        artticles = []
        for article in allArticles:
            if article.published:
                artticles.append(article)
            if len(artticles) == 10:
                break
        return artticles

    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content[:400]
    
    def item_link(self, item):
        return reverse('blog:article', args=[item.slug])

class UnvalidedCommentsFeed(Feed):
    title = "Commentaires du blog (non validés)"
    description = "Derniers commentaires non validés"
    link = "feeds/"

    def items(self):
        return Comment.objects.filter(valided=False).order_by('-publication_date')
    
    def item_title(self, item):
        return item.username
    
    def item_description(self, item):
        return item.content
    
    def item_link(self, item):
        return reverse('blog:index')

class ValidedCommentsFeed(Feed):
    title = "Commentaires du blog"
    description = 'Flux des commentaires'
    link = 'feeds/'

    def items(self):
        return Comment.objects.order_by('-publication_date')[:50]
    
    def item_title(self, item):
        return item.username
    
    def item_description(self, item):
        return item.content
    
    def item_link(self, item):
        return reverse('blog:article', args=[item.article.slug])
