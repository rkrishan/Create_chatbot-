from django.db import models

# Create your models here.
class ChatBotQuestion(models.Model):
    """
    This class have question and answer for each request 
    """
    question_text =  models.CharField(max_length=50)
    answer_text   =  models.CharField(max_length=50)

    # def __str__(self):
    #     return self.answer_text
