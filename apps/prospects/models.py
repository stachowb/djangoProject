from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Skills(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ProspectProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=520)
    cv_file = models.FileField(blank=True)
    skills = models.ManyToManyField(Skills, through="ProspectSkillset")
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.get_full_name())
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.user.get_full_name()

    def get_absolute_url(self):
        return f'/{self.slug}/'


class ProspectSkillset(models.Model):
    user = models.ForeignKey(ProspectProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    level_choices = (
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****")
    )
    level = models.IntegerField(choices=level_choices, default=0)

    experience_choices = (
        (0, "less than a year"),
        (1, "1 year"),
        (2, "2 years"),
        (3, "3 years"),
        (4, "4 years"),
        (5, "5 years"),
        (6, "more than 5 years")
    )
    experience = models.IntegerField(choices=experience_choices, default=0)

    def __str__(self):
        return self.user.__str__()
