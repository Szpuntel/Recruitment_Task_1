from django import forms
from .models import Expense, Category

class ExpenseSearchForm(forms.ModelForm):

    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple
    )

    start_date = forms.DateField(
        required = False,
        widget=forms.TextInput(
            attrs={'type': 'date'}))
        
    end_date = forms.DateField(
        required = False,
        widget=forms.TextInput(
            attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ('name',)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False

