import json

from django.db import models


class ImageTestTable(models.Model):
    img_url = models.CharField(max_length=512, default='')
    img = models.ImageField(null=True, blank=True)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)
