from django import forms


class AddScore(forms.Form):
    duration = forms.DurationField(label="Durée")
    height = forms.IntegerField(label="Hauteur")
    length = forms.IntegerField(label="Largeur")
    mines = forms.IntegerField(label="Mines")
