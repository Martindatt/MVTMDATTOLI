from django import forms

class Form_Cliente(forms.Form):

    nombreC = forms.CharField(max_length=40)
    tipo_cli = forms.CharField(max_length=40)
    rama = forms.CharField(max_length=40)


class Form_Proveedor(forms.Form):

    nombreP = forms.CharField(max_length=40)
    codigoprov = forms.IntegerField()
    tipo_prov = forms.CharField(max_length=40)
    rama = forms.CharField(max_length=40)

class Form_Personal (forms.Form):

    nombreU = forms.CharField(max_length=40)
    sector = forms.CharField(max_length=40)
    rol = forms.CharField(max_length=40)