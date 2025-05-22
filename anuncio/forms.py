from django import forms
from anuncio.models import Anuncio

class FormularioAnuncio(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = ['veiculo', 'preco_diaria', 'descricao', 'status']
        widgets = {
            'veiculo': forms.Select(attrs={'class': 'form-control'}),
            'preco_diaria': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }