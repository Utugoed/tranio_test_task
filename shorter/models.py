from django.db import models

from shorter.helpers import generate_code

# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=6, unique=True)
    usage_counter = models.IntegerField(default=0)

    class Meta:
        ordering = ['pk']

    @classmethod
    def create_code(cls, url: str):
        code = generate_code()
        existing_url = cls.objects.all().filter(code=code)
        while existing_url:
            code = generate_code()
        
        new_url = cls(
            url=url,
            code=code
        )
        new_url.save()
        return new_url

    def to_dict(self):
        return {
            "pk": self.pk,
            "url": self.url,
            "code": self.code,
            "usage_counter": self.usage_counter
        }

    def update_counter(self):
        self.usage_counter += 1
        self.save()