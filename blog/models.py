import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from django.db.models.signals import pre_save
from django.dispatch import receiver

from slugify import slugify

SOCIAL_CHOICES = (
    ('LINKED_IN', 'Linked In'),
    ('INSTAGRAM', 'Instagram'),
    ('RSS_FLUX', 'Flux RSS'),
    ('FACEBOOK', 'Facebook'),
    ('GITHUB', 'Github'),
    ('BITBUCKET', 'Bitbucket'),
    ('GOOGLE_PLUS', 'Google+'),
    ('YOUTUBE', 'Youtube'),
    ('MASTODON', 'Mastodon'),
    ('DIASPORA', 'Diaspora'),
    ('PEERTUBE', 'Peertube'),
    ('PATREON', 'Patreon'),
    ('DISCORD', 'Discord')
)

class Blog(models.Model):
    name = models.CharField('Nom', max_length=255)
    description = models.CharField('Description', max_length=500, blank=True, null=True)
    cover = models.ImageField('Image de couverture', upload_to='blog/', blank=True, null=True)
    sidebar_title = models.CharField('Barre latérale', max_length=30, blank=True, null=True)
    sidebar_picture = models.ImageField('Avatar', upload_to='blog/', blank=True, null=True)
    sidebar_description = models.TextField('Description dans la sidebar', max_length=250, blank=True, null=True)

class Media(models.Model):
    file = models.FileField(upload_to='media/')
    title = models.CharField('Nom', max_length=100, blank=True, null=True)

class Page(models.Model):
    name = models.CharField('Nom', max_length=100)
    slug = models.SlugField('Lien d\'accès', max_length=100, unique=True)
    content = models.TextField('Contenu')
    displayed = models.BooleanField('Affiché dans le menu', default=True)
    cover = models.ImageField('Image de couverture', upload_to='pages/', blank=True, null=True)

class Comment(models.Model):
    username = models.CharField('Nom d\'utilisateur', max_length=25)
    publication_date = models.DateTimeField('Date de publication')
    valided = models.BooleanField('Validé', default=False)
    content = models.TextField('Contenu')
    
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Commentaire')
        verbose_name_plural = _('Commentaires')

class Article(models.Model):
    title = models.CharField('Titre', max_length=200)
    slug = models.SlugField('Lien d\'accès', max_length=100, unique=True)
    content = models.TextField('Contenu')
    publication_date = models.DateTimeField('Date de publication')
    update_date = models.DateTimeField('Date de mise à jour', blank=True, null=True)
    published = models.BooleanField('Publié', default=False)
    cover = models.ImageField('Image de couverture', upload_to='covers/', blank=True, null=True)
    hide_image = models.NullBooleanField('Cacher les images', default=False)
    disclaimer = models.TextField('Disclaimer', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def comments_count(self):
        return Comment.objects.filter(article=self.id).count()

    def unvalided_comments(self):
        return Comment.objects.filter(article=self.id, valided=False)
    
    def unvalided_comments_count(self):
        return Comment.objects.filter(article=self.id, valided=False).count()

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField('Nom', max_length=60)
    slug = models.SlugField('Lien d\'accès', max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Catégorie')
        verbose_name_plural = _('Catégories')

class Question(models.Model):
    question = models.CharField('Question', max_length=100)
    answer = models.CharField('Réponse', max_length=2)

class Link(models.Model):
    sort = models.IntegerField('Ordre', default="5")
    link = models.URLField('Lien')
    shortcut = models.CharField('Titre', max_length=60)
    
    def __str__(self):
        return self.shortcut

    class Meta:
        verbose_name = _('Lien')
        verbose_name_plural = _('Liens')

class Social(models.Model):
    sort = models.IntegerField('Ordre', default="5")
    link = models.URLField('Lien')
    network = models.CharField('Réseau', choices=SOCIAL_CHOICES, max_length=16, blank=True, null=True)
    shortcut = models.CharField('Titre', max_length=60)
    sidebar = models.BooleanField('Affiché dans la sidebar', default=False)

    def __str__(self):
        return self.shortcut


@receiver(pre_save, sender=Page)
def cb_page_slug(sender, instance, **kwargs):
    if instance.id is None:
        instance.slug = slugify(instance.name)

@receiver(pre_save, sender=Article)
def cb_article_slug(sender, instance, **kwargs):
    if instance.id is None:
        instance.slug = slugify(instance.title)

@receiver(pre_save, sender=Category)
def cb_category_slug(sender, instance, **kwargs):
    if instance.id is None:
        instance.slug = slugify(instance.name)