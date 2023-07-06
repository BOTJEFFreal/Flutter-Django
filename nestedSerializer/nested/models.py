from django.db import models

class FourthModel(models.Model):
    text_field_four = models.CharField(max_length=100)

class ThirdModel(models.Model):
    text_field_three = models.CharField(max_length=100)
    fourth_model = models.ForeignKey(FourthModel, on_delete=models.CASCADE)

class SecondModel(models.Model):
    text_field_two = models.CharField(max_length=100)
    third_model = models.ForeignKey(ThirdModel, on_delete=models.CASCADE)

class FirstModel(models.Model):
    text_field_one = models.CharField(max_length=100)
    second_model = models.ForeignKey(SecondModel, on_delete=models.CASCADE)