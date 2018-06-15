from django.db import models


class Partnership_Company(models.Model):
    title = models.CharField(max_length=255, verbose_name=('company_title'), blank=True)
    logo = models.ImageField(upload_to='companies-logo')
    site_adress =  models.CharField(max_length=255, verbose_name=('site_adress'), blank=True)


class Team_member(models.Model):
    name = models.CharField(max_length=255, verbose_name=('team_member'), blank=True)
    description = models.TextField(verbose_name=('description'))
    logo = models.ImageField(upload_to='team-members')


class Feedback(models.Model):
    name = models.CharField(max_length=255, verbose_name=('name'), blank=True)
    body_text = models.TextField(verbose_name=('description'))
    created_at = models.DateTimeField(auto_now_add=True)
