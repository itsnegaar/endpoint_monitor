from django.db import models


class UrlItem(models.Model):
    """ Url database models"""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    user = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    address = models.CharField(max_length=255)
    threshold = models.IntegerField(default=10)
    failed_times = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ Return string representation of our url item """
        return self.address


class RequestItem(models.Model):
    """ Request database models"""
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    url = models.ForeignKey(
        UrlItem,
        on_delete=models.CASCADE
    )
    result = models.IntegerField(default=0)

    def __str__(self):
        """ Return string representation of our request item """
        return self.url.address