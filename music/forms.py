from django.forms.models import inlineformset_factory
from music.models import Album, Track

TrackFormSet = inlineformset_factory(Album, Track, 
    fields=['album', 'number', 'name'], 
    exclude=[],
    can_delete=False)