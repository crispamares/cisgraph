from django.db import models

# Create your models here.


class Poll(models.Model):
    kind = models.CharField(max_length=50, unique_for_date="date")
    poll_name = models.CharField(max_length=200)
    date = models.DateField()
    cis_study_id = models.SmallIntegerField()

    def __str__(self):
        return self.poll_name


class Question(models.Model):
    poll = models.ForeignKey(Poll)
    kind = models.CharField(max_length=50)  # AutoUbicacion, ...
    question_text = models.CharField(max_length=200)
    sample = models.PositiveIntegerField('N')

    def __str__(self):
        return self.kind + " -- " + self.poll.poll_name


class Choice(models.Model):
    """
    Available Choice for any Question
    """
    question = models.ForeignKey(Question)
    answer_int = models.SmallIntegerField()
    answer_text = models.CharField(max_length=200)
    is_nsnc = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text + " -- " + str(self.answer_int)


class Facet(models.Model):
    """
    Represents a Column in multi-answers or a Facet in faceted answers
    """
    question = models.ForeignKey(Question)
    kind = models.CharField(max_length=50)  # COLUMN, VOTO, IDEOLOGIA, ...
    value = models.SmallIntegerField()
    facet_text = models.CharField(max_length=200)
    is_total = models.BooleanField(default=False)
    sample = models.PositiveIntegerField('N')


class Answer(models.Model):
    question = models.ForeignKey(Question)
    choice = models.ForeignKey(Choice)
    percent = models.FloatField()
    facet = models.ForeignKey(Facet, null=True, blank=True)

    def is_multi(self):
        return bool(self.facet)

    def __str__(self):
        return str(self.choice.answer_text) + " -- " + str(self.percent)


# class AvAutoUbicacion(models.Model):
#     question = models.ForeignKey(Question)
#     posicion_ideologica = models.ForeignKey(Choice)  # 1 2 3 4 5 6 7 8 9 10 ns nc
#     percent = models.SmallIntegerField()
