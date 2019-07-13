from django import forms
from .models import ComplaintForm, Invoice


class DocumentForm(forms.ModelForm):
    class Meta:
        model = ComplaintForm
        fields = '__all__'


class InvoiceForm(forms.Form):
    FORMAT_CHOICES = (
        ('pdf', 'PDF'),
        ('docx', 'MS Word'),
        ('html', 'HTML'),
    )
    number = forms.CharField(label='Invoice #')
    customer = forms.ModelChoiceField(queryset=Invoice.objects.all())
    subject = forms.CharField()
    amount = forms.DecimalField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
