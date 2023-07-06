from rest_framework import serializers
from .models import FirstModel, SecondModel, ThirdModel, FourthModel

class FourthLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthModel
        fields = ('text_field_four',)

class ThirdLevelSerializer(serializers.ModelSerializer):
    fourth_model = FourthLevelSerializer()

    class Meta:
        model = ThirdModel
        fields = ('text_field_three', 'fourth_model')

class SecondLevelSerializer(serializers.ModelSerializer):
    third_model = ThirdLevelSerializer()

    class Meta:
        model = SecondModel
        fields = ('text_field_two', 'third_model')

class FirstLevelSerializer(serializers.ModelSerializer):
    second_model = SecondLevelSerializer()

    class Meta:
        model = FirstModel
        fields = ('text_field_one', 'second_model')