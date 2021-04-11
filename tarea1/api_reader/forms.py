from django import forms


characters_choices = []

class CharacterForm(forms.Form):
    character_number = forms.CharField(label="Ingrese nombre del personaje ", max_length=100, required=False)

