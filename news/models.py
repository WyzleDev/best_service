from django.db import models

from django.utils.translation import gettext_lazy as _


class Post(models.Model):
    image = models.ImageField(upload_to="media/")
    header = models.CharField(_("Заголовок"), max_length=128, null=False, blank=False)
    body = models.TextField(_("Тело поста"), null=False, blank=False)

    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = 'Посты'


