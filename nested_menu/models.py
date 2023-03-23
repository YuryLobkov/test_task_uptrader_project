from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    url_type = models.CharField(max_length=20, choices=[('url', 'URL'), ('named_url', 'Named URL')])
    url = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def is_active(self, current_url):
        return current_url == self.url

    def __str__(self):
        return self.name
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.url = self.get_url()

    def get_url(self):
        if self.url_type == 'named_url':
            try:
                return reverse(self.url)
            except NoReverseMatch:
                return ''
        return self.url
