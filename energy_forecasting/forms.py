from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(required=True)  # Ensure this matches the field name
