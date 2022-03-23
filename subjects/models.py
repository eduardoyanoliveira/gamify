from django.db import models
from util.db import base
import re

# Create your models here.
class Subject(base.BaseNameField):
    
    class Meta:
        db_table = 'tbl_subject'


class Content(base.BaseNameField):
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    url =  models.URLField(max_length=300)

    def save(self, *args, **kwargs):
        # regex pattern for url
        pattern = re.compile(r'((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)')

        # Checks if the URL is valid
        if(not re.match(pattern, self.url)):
           raise ValueError('Url field recived a not valid url')
       
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'tbl_content'


class Keyword(models.Model):
    content_id = models.ForeignKey(Content, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.keyword