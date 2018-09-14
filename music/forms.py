from django.forms import TextInput
from django.forms.models import inlineformset_factory
from music.models import Album, Track

TrackFormSet = inlineformset_factory(Album, Track, 
    fields=['album', 'number', 'name'],
    can_delete=False,
    widgets={
        'artist': TextInput(attrs={'class': 'form-control'}),
        'name': TextInput(attrs={'class': 'form-control'}),
        'number': TextInput(attrs={'class': 'form-control'})
    }
)