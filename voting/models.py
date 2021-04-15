from django.db import models


class Poll(models.Model):

    Name = models.CharField(max_length=200)

    no_of_votes = models.IntegerField(default=0)

    vote = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

    def __int__(self):
        return self.no_of_votes

