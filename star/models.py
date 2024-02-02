from django.db import models
from django.utils import timezone

class Blog_post(models.Model):
    title = models.CharField(max_length=300)
    date_created = models.DateTimeField()
    image = models.CharField(max_length=200, null=True)
    intro = models.TextField()
    boldi = models.TextField(blank=True, null=True)
    paraf = models.TextField()
    paraf1 = models.TextField(blank=True, null=True)
    paraf2 = models.TextField(blank=True, null=True)
    paraf3 = models.TextField(blank=True, null=True)
    boldi2 = models.TextField(blank=True, null=True)
    paraf4 = models.TextField(blank=True, null=True)
    paraf5 = models.TextField(blank=True, null=True)
    paraf6 = models.TextField(blank=True, null=True)
    paraf7 = models.TextField(blank=True, null=True)
    boldi3 = models.TextField(blank=True, null=True)
    paraf8 = models.TextField(blank=True, null=True)
    paraf9 = models.TextField(blank=True, null=True)
    paraf10 = models.TextField(blank=True, null=True)
    paraf11 = models.TextField(blank=True, null=True)
    boldi4 = models.TextField(blank=True, null=True)
    paraf12 = models.TextField(blank=True, null=True)
    paraf13 = models.TextField(blank=True, null=True)
    paraf14 = models.TextField(blank=True, null=True)
    paraf15 = models.TextField(blank=True, null=True)
    image2 = models.CharField(max_length=200, blank=True, null=True)
    bolds = models.TextField(blank=True, null=True)
    paras = models.TextField(blank=True, null=True)
    paras1 = models.TextField(blank=True, null=True)
    paras2 = models.TextField(blank=True, null=True)
    paras3 = models.TextField(blank=True, null=True)
    bolds2 = models.TextField(blank=True, null=True)
    paras4 = models.TextField(blank=True, null=True)
    paras5 = models.TextField(blank=True, null=True)
    paras6 = models.TextField(blank=True, null=True)
    paras7 = models.TextField(blank=True, null=True)
    bolds3 = models.TextField(blank=True, null=True)
    paras8 = models.TextField(blank=True, null=True)
    paras9 = models.TextField(blank=True, null=True)
    paras10 = models.TextField(blank=True, null=True)
    paras11 = models.TextField(blank=True, null=True)
    bolds4 = models.TextField(blank=True, null=True)
    paras12 = models.TextField(blank=True, null=True)
    paras13 = models.TextField(blank=True, null=True)
    paras14 = models.TextField(blank=True, null=True)
    paras15 = models.TextField(blank=True, null=True)
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['-date_created']