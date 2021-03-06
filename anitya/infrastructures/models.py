from django.db import models
import uuid


class Driver(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='')
    plugin = models.CharField(max_length=50, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Physical(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=200, default='UNKNOWN')
    driver_id = models.CharField(max_length=36, default='')
    ip_address = models.CharField(max_length=15, default='')
    secret_key = models.CharField(max_length=50, default='')
    az = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=1000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Virtual(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, default='')
    physical_id = models.CharField(max_length=36, default='UNKNOWN')
    tags = models.CharField(max_length=200, default='UNKNOWN')
    description = models.CharField(max_length=1000, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name