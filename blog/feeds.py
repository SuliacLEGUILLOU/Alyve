from django.contrib.syndication.views import Feed
from django.urls import reverse

from blog.models import Article, Comment

class LatestArticlesFeed(Feed):
    title = "Le blog d'Alysson"
    description = "Derniers articles"
    link = "feeds/"

    def items(self):
        return Article.objects.order_by('-publication_date')[:10]
    
    def item_title(self, item):
        return item.title
    
    def item_description(self, item):
        return item.content[:400]
    
    def item_link(self, item):
        return reverse('blog:article', args=[item.slug])

class UnvalidedCommentsFeed(Feed):
    title = "Commentaires du blog"
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