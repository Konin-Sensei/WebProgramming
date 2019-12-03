from django import forms
from mysite.core.models import Puzzle
from django.contrib.auth.models import User


class PuzzleForm(forms.ModelForm):
    box_1_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=4, disabled=True)
    box_1_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=8, disabled=True)
    box_1_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_1_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=8, disabled=True)
    box_2_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=3, disabled=True)
    box_2_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=4, disabled=True)
    box_2_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_2_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=5, disabled=True)
    box_3_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=3, disabled=True)
    box_3_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_3_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_3_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_3_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=4, disabled=True)
    box_3_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=2, disabled=True)
    box_3_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=9, disabled=True)
    box_3_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_3_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=7, disabled=True)
    box_4_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=3, disabled=True)
    box_4_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_4_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=2, disabled=True)
    box_4_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_4_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=5, disabled=True)
    box_4_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_4_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=6, disabled=True)
    box_4_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_4_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=8, disabled=True)
    box_5_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=7, disabled=True)
    box_5_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_5_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=9, disabled=True)
    box_5_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_6_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=5, disabled=True)
    box_6_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_6_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=8, disabled=True)
    box_6_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_6_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=7, disabled=True)
    box_6_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_6_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=2, disabled=True)
    box_6_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_6_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=1, disabled=True)
    box_7_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=4, disabled=True)
    box_7_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_7_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=6, disabled=True)
    box_7_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=5, disabled=True)
    box_7_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=2, disabled=True)
    box_7_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_7_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_7_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_7_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=7, disabled=True)
    box_8_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=2, disabled=True)
    box_8_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_8_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=7, disabled=True)
    box_8_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=9, disabled=True)
    box_8_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_8_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_8_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_8_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=1, disabled=True)
    box_8_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_1 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_2 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_3 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=9, disabled=True)
    box_9_value_4 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_5 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_6 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_7 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=4, disabled=True)
    box_9_value_8 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    box_9_value_9 = forms.IntegerField(widget=forms.TextInput(attrs={'style':'width: 10px; height: 10px;'}), label='', initial=0)
    class Meta:
        model = Puzzle
        fields ="__all__"
        """fields = ['box_1_value_1','box_1_value_2','box_1_value_3','box_1_value_4','box_1_value_5','box_1_value_6','box_1_value_7','box_1_value_8','box_1_value_9',
                'box_2_value_1','box_2_value_2','box_2_value_3','box_2_value_4','box_2_value_5','box_2_value_6','box_2_value_7','box_2_value_8','box_2_value_9',
                'box_3_value_1','box_3_value_2','box_3_value_3','box_3_value_4','box_3_value_5','box_3_value_6','box_3_value_7','box_3_value_8','box_3_value_9',
                'box_4_value_1','box_4_value_2','box_4_value_3','box_4_value_4','box_4_value_5','box_4_value_6','box_4_value_7','box_4_value_8','box_4_value_9',
                'box_5_value_1','box_5_value_2','box_5_value_3','box_5_value_4','box_5_value_5','box_5_value_6','box_5_value_7','box_5_value_8','box_5_value_9',
                'box_6_value_1','box_6_value_2','box_6_value_3','box_6_value_4','box_6_value_5','box_6_value_6','box_6_value_7','box_6_value_8','box_6_value_9',
                'box_7_value_1','box_7_value_2','box_7_value_3','box_7_value_4','box_7_value_5','box_7_value_6','box_7_value_7','box_7_value_8','box_7_value_9',
                'box_8_value_1','box_8_value_2','box_8_value_3','box_8_value_4','box_8_value_5','box_8_value_6','box_8_value_7','box_8_value_8','box_8_value_9',
                'box_9_value_1','box_9_value_2','box_9_value_3','box_9_value_4','box_9_value_5','box_9_value_6','box_9_value_7','box_9_value_8','box_9_value_9']"""
    
    
