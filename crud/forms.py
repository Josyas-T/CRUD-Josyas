from django import forms
from .models import Cliente
from validate_docbr import CPF, CNPJ

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

    def clean_documento(self):
        doc = self.cleaned_data['documento']
        doc = ''.join(filter(str.isdigit, doc))  # remove pontuação

        if len(doc) == 11:
            if not CPF().validate(doc):
                raise forms.ValidationError("CPF inválido.")
        elif len(doc) == 14:
            if not CNPJ().validate(doc):
                raise forms.ValidationError("CNPJ inválido.")
        else:
            raise forms.ValidationError("Documento deve ser um CPF ou CNPJ válido.")

        # Verificar duplicidade
        if Cliente.objects.filter(documento=doc).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Este documento já está cadastrado.")
        
        return doc
