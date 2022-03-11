from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, update_rate):
        self.rating = update_rate
        self.save()

    # def __str__(self):
    #     return ' '.join([
    #         self.user,
    #         self.rating,
    #     ])


class Category(models.Model):
    name_category = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    news = 'N'
    article = 'A'

    type = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    type_post = models.CharField(max_length=1, choices=type, default=article)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    time_write = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, blank=False)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        preview_text = 124 if len(self.text) > 124 else len(self.text)
        return self.text[:preview_text]+'...'


class Postcategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    author_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_write = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
