from django.db import models

class Project(models.Model):
    """
    Django model representing a front-end project.

    Fields:
        - name: Unique name of the project.
        - html: HTML source code.
        - css: CSS source code.
        - js: JavaScript source code.

    The __str__ method returns the project's name.
    """
    name = models.CharField(max_length=100, unique=True)
    html = models.TextField(blank=True)
    css = models.TextField(blank=True)
    js = models.TextField(blank=True)

    def __str__(self):
        return self.name
