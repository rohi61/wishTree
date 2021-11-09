from django import forms


class index_form(forms.Form):

    groop_id = forms.CharField(label='グループID',
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder':'パスコードを入力'}))

class groop_register_form(forms.Form):

    groop_name = forms.CharField(label='グループ名',required=True)
    target = forms.CharField(label='目標',required=True)
    number_of_people = forms.IntegerField(label='人数',required=True)
    member_name = forms.CharField(label='メンバー名',required=False)
    