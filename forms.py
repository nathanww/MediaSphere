from django import newforms as forms

class GuestbookForm(forms.Form):
  message = forms.CharField(label='Sign the Guestbook', widget=forms.Textarea())
