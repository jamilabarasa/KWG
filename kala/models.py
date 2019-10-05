from django.db import models
from django.conf import settings
class Member(models.Model):
    CATS = (
        ("REGULAR","REGULAR"),
        ("ELDERLY","ELDERLY"),
        ("STAFF","STAFF"),
    )
    GEN = (
        ("MALE","MALE"),
        ("FEMALE","FEMALE"),
    )
    
    name = models.CharField(max_length=50,unique=True)
    idno = models.CharField(max_length=10)
    gender = models.CharField(max_length=10,choices=GEN,default='MALE')
    contact = models.CharField(max_length=20,unique=True)
    category = models.CharField(max_length=10,choices=CATS,default='REGULAR')
    date_joined = models.DateField()
    def __str__(self):
        return self.name


class New(models.Model):
    subject = models.CharField(max_length = 70)
    body = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.subject

class Comment(models.Model):
    post = models.ForeignKey(New,on_delete=models.CASCADE,related_name='comment')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ('created',)

    def __str__(self):
        return '#{} - {}'.format(self.id,self.post)

class Burial(models.Model):
    PLACES = (
        ("NAIROBI","NAIROBI"),
        ("KITUI","KITUI"),
        ("MOMBASA","MOMBASA"),
        ("OTHER","OTHER"),
    )
    who = models.ForeignKey(Member,on_delete=models.CASCADE)
    place = models.CharField(max_length=15,choices=PLACES,default="KITUI")
    date = models.DateField(auto_now_add=True)
    burial_date = models.DateField(blank=True)
    
    class Meta:
        ordering = ('-date',)
    
    def __str__(self):
        return self.who

