
from django.conf import settings
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
        repo = settings.REPO
        repo.git.checkout(self.target)
        repo.git.merge(self.source)

        self.status = PullRequest.MERGED_STATUS
        self.save()

    def close(self):
        self.status = PullRequest.CLOSED_STATUS
        self.save()


# comment for test-2
