from django.db import models
from django.contrib.auth.models import User


class Skills(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ProspectProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=520)
    cv_file = models.FileField()
    skills = models.ManyToManyField(Skills, through="ProspectSkillset")





class ProspectSkillset(models.Model):
    user = models.ForeignKey(ProspectProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    level_choices = (
        ("*", 1),
        ("**", 2),
        ("***", 3),
        ("****", 4),
        ("*****", 5)
    )
    level = models.IntegerField(choices=level_choices)
    experience = models.IntegerField()
