from django.db import models


class Profile(models.Model):
    skills = None
    bio = models.TextField(max_length=520)
    photo = models.ImageField()
    cv_file = models.FileField()


class Skills(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class ProspectSkillset(models.Model):
    prospect = None
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    level_choices = (
        ("*", 1),
        ("**", 2),
        ("***", 3),
        ("****", 4),
        ("*****", 5)
    )
    level = models.IntegerField(choices=level_choices)
