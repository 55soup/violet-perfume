from django import forms

from perfume.models import Memory, Comments


class MemoryCreationForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = ['name', 'description', 'year', 'image']

    def save(self, commit=True):
        new_memory = Memory.objects.create(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('description'),
            year = self.cleaned_data.get('year'),
            image = self.cleaned_data.get('image'),
        )
        return new_memory



class CommentCreationsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user', 'comment']

    # def save(self, commit=True):
    #     new_comment = Comments.objects.create(
    #         user = self.cleaned_data.get('user'),
    #         content = self.cleaned_data.get('comment'),
    #         image=self.cleaned_data.get('image'),
    #     )
    #     return new_comment

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['comment']