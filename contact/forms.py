from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
    tel_number = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['from_email'].label = "Twój email*"
        self.fields['tel_number'].label = "Twój telefon"
        self.fields['subject'].label = "Temat*"
        self.fields['message'].label = "Twoja wiadomość*"
