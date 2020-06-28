from django import forms

styles=(("1","1"),("2","2"),("3","3"),("4","4"),
	("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),
	("10","10"))
colors=(("1","Bk"),("2","Bl"),("3","Rd"),("4","Gr"))

class inputform(forms.Form):
	pdf = forms.FileField()
	style = forms.ChoiceField(choices=styles)
	color = forms.ChoiceField(choices=colors)
	slider = forms.IntegerField(widget=forms.NumberInput(attrs={'type':'range', 'step': '0.1', 'min': '1', 'max': '2', 'value': '1.5'}))
	setting = forms.BooleanField()