from xmlrpc.client import Boolean
from django.db import models
from game_config.models import Difficulty
from util.db import interections

# Create your models here.
class Question(interections.BaseInteraction):
    is_public = models.BooleanField(default=False)
    difficulty_id = models.ForeignKey(Difficulty, on_delete=models.PROTECT)
   
    def toggle_public(self) -> None:
        self.is_public = not self.is_public
        
    class Meta:
        db_table = 'tbl_question'    
    


class Answer(interections.BaseInteraction):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'tbl_answer'    