from django import forms

class FarmingForm(forms.Form):
    
    farming_title = forms.CharField(label='파밍제목', max_length=100)
    rotation = forms.IntegerField(label='로테이션', min_value=0)
    yellow = forms.IntegerField(label='노란생기', min_value=0)
    red = forms.IntegerField(label='빨간생기', min_value=0)
    blue = forms.IntegerField(label='파란생기', min_value=0)
    divine = forms.IntegerField(label='럭키', min_value=0)
    
    # Choice Field for 17T 지도
    MAP_CHOICES = [
        ('흉물', '흉물'), 
        ('성역', '성역'), 
        ('성채', '성채'), 
        ('요새', '요새'), 
        ('지구라트', '지구라트')
    ]
    
    map_type = forms.ChoiceField(label='17T 지도 종류', choices=MAP_CHOICES)
    map_count = forms.IntegerField(label='17T 지도', min_value=0)