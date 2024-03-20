from django.db import models


class Crusade(models.Model):
    nomi = models.CharField(max_length=250)
    sababi = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.nomi

    class Meta:
        ordering = ['id']
        verbose_name = 'Crusade'
        verbose_name_plural = 'crusade'
        db_table = 'crusade'
