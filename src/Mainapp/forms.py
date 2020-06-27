from django import forms

styles=(("Choose style","Choose style"),("Style 1","Style 1"),("Style 2","Style 2"),("Style 3","Style 3"),("Style 4","Style 4"),
	("Style 5","Style 5"),("Style 6","Style 6"),("Style 7","Style 7"),("Style 8","Style 8"),("Style 9","Style 9"),
	("Style 10","Style 10"))
colors=(("Choose color","Choose color"),("Black","Black"),("Blue","Blue"),("Red","Red"),("Green","Green"))

class inputform(forms.Form):
	pdf = forms.FileField()
	style = forms.ChoiceField(choices=styles)
	color = forms.ChoiceField(choices=colors)
	slider = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '0.1', 'min': '1', 'max': '2', 'value': '1.5'}))
	setting = forms.BooleanField()