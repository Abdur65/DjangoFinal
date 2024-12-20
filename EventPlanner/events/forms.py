from django import forms
from events.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date_time', 'location', 'capacity']
        
        def clean_price(self):
            capacity = self.cleaned_data.get('capacity')
            
            if capacity < 0:
                raise forms.ValidationError("The capacity must be a positive number")
            
            return capacity