from turtle import update
from django.db import models
from user_profile.models import User
from django.utils.text import slugify
from .slug import genarate_unique_slug
from ckeditor.fields import RichTextField


#category
class Category(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug  = models.SlugField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)

#tags
class Tag(models.Model):
    title = models.CharField(max_length=150)
    slug  = models.SlugField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)


#blogs    
class Blog(models.Model):
    user = models.ForeignKey(User, related_name='user_blogs', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category_blogs', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tag_blogs', blank=True)
    likes = models.ManyToManyField(User, related_name='user_likes', blank=True) 
    title = models.CharField(max_length=250)
    slug = models.SlugField(null=True,blank=True)
    banner = models.ImageField(upload_to='blog_banners')
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.pk) +"."+ self.title
    
    '''def save(self, *arg, **kwargs):
        self.slug = slugify(self.title)
        super().save(*arg, **kwargs)'''

    def save(self, *arg, **kwargs):
        updating = self.pk is not None 
        if updating:
            self.slug = genarate_unique_slug(self, self.title, update = True)
            super().save(*arg, **kwargs) 

        else:
            self.slug = genarate_unique_slug(self, self.title)
            super().save(*arg, **kwargs)


#comment
class Comment(models.Model):
    user = models.ForeignKey(User,related_name='user_comment',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='blog_comment',on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return  str(self.pk) +"."+self.text


#reply
class Reply(models.Model):
    user = models.ForeignKey(User,related_name='user_reply',on_delete=models.CASCADE)
    comment = models.ForeignKey(Blog, related_name='comment_reply',on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text
