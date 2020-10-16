from django.db import models

class Images(models.Model):
    files = models.FileField(upload_to="multi_imgs/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Memos(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    img01 = models.ImageField(blank=True)
    img02 = models.ImageField(blank=True)
    img03 = models.ImageField(blank=True)
    img04 = models.ImageField(blank=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.img01.delete()
        self.img02.delete()
        self.img03.delete()
        self.img04.delete()
        super().delete(*args, **kwargs)