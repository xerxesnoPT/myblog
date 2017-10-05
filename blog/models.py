from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    created_time = models.DateField()
    modified_time = models.DateField()
    # 文章摘要,使用'blank'属性设置为True表示允许空值
    excerpt = models.CharField(max_length=200, blank=True)
    # 设置外键,多对一关系确立关系分类,作者. 标签为多对多关系
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})


    class Meta:
        ordering = ['-created_time', 'title']




