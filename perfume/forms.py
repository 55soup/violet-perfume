from django import forms

from perfume.models import Memory


class MemoryCreationForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'description', 'image']

    def save(self, commit=True):
        new_memory = Memory.objects.create(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('description'),
            image = self.cleaned_data.get('image'),
        )
        return new_memory


