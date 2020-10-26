from django.db import models


class Quote(models.Model):
    quote_author = models.CharField(max_length=75)
    quote_body = models.TextField(max_length=280, null=True)
    context = models.CharField(max_length=75)
    source = models.CharField(max_length=75)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote_author}'
