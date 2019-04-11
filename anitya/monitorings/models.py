from django.db import models
import uuid

class IndexView(models.Model):
    pass

class InstanceStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    virtual_id = models.CharField(max_length=36, default='')
    status = models.CharField(max_length=50, default='UNKNOWN')

    def __str__(self):
        return self.id
