from django.db import models

# Create your models here.
class Add_question(models.Model):
    question=models.TextField()
class Answer(models.Model):
    answer=models.TextField()
    ques_id=models.IntegerField(default=0)
    user_name=models.CharField(max_length=100,default=0)
    like=models.IntegerField(default=0)



