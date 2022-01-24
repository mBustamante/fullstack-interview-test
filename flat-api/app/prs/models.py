
from django.db import models


class PullRequest(models.Model):

    OPEN_STATUS = 'OPEN'
    MERGED_STATUS = 'MERGED'
    CLOSED_STATUS = 'CLOSED'

    STATUS_CHOICES = [
        (OPEN_STATUS, 'OPEN'),
        (MERGED_STATUS, 'MERGED'),
        (CLOSED_STATUS, 'CLOSED'),
    ]

    source = models.CharField(max_length=64)
    target = models.CharField(max_length=64)
    author_name = models.CharField(max_length=64)
    author_email = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    created = models.DateTimeField(auto_now_add=True, editable=False, blank=True)
    modified = models.DateTimeField(auto_now=True, editable=False, blank=True)

    def merge(self):
        try:
            pass
        except Exception as e:
            print(e)

    def close(self):
        status = PullRequest.CLOSED_STATUS
        status.save()

# comentario prueba 1
