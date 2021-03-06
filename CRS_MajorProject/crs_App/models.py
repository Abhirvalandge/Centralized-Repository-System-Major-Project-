from django.db import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.urls import reverse
from django.utils import timezone


class EducationModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('education_details',args=[
    #                                       self.id,
    #                                       self.publish.year,
    #                                       self.publish.month,
    #                                       self.publish.day,
    #                                       self.slug_field])

class HealthModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('health_details',args=[self.id,self.publish.year,
    #                                       self.publish.month,
    #                                       self.publish.day,
    #                                       self.slug_field])

class AgricultureModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('agriculture_details',args=[self.id,self.publish.year,
    #                                       self.publish.month,
    #                                       self.publish.day,
    #                                       self.slug_field])

class ElectricityModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('electricity_details',args=[self.id,self.publish.year,
    #                                       self.publish.month,
    #                                       self.publish.day,
     #                                      self.slug_field])

class BusinessModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
    #    return reverse('business_details',args=[self.id,self.publish.year,
    #                                       self.publish.month,
    #                                       self.publish.day,
    #                                       self.slug_field])

class YouthModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title

    #def get_absolute_url(self):
     #   return reverse('youth_details',args=[self.id,self.publish.year,
     #                                      self.publish.month,
     #                                      self.publish.day,
     #                                      self.slug_field])


class GovernmentJobsModel(models.Model):
    STATUS_CHOICES = (('draft','Draft'),('published','Published'))
    title = models.CharField(max_length=256)
    slug_field = models.SlugField(max_length=256,unique_for_date='publish')
    body = models.TextField()
    link = models.URLField(max_length=100)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')


    class Meta:
        ordering=('-publish',)

    def __str__(self):
        return self.title


