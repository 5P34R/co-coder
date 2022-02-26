from django.contrib.auth.models import User
from django.db import models

class Notes(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    date = models.CharField(max_length=255, blank=True)


    def save(self):
        self.date = f"{self.publish.strftime('%B')} {self.publish.strftime('%D').split('/')[1]} 20{self.publish.strftime('%D').split('/')[2]}"
        super(Notes, self).save()

    class Meta:
        ordering = ('-date_created'),


    def __str__(self):
        return f"{self.title}"