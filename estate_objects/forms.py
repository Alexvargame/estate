from django import forms
from django.forms import widgets, fields

from .models import Flat, FlatImage, SearchFlat, House, SearchHouse, Smartflat, SearchSmartFlat, City, Street, District

from datetime import datetime, date, time

class ImageWidget(forms.MultiWidget):
    def __init__(self,n, attrs=None):

        widgets=[forms.ClearableFileInput(attrs={'class':'form-control', 'empty_value':True})]*n
        super().__init__(widgets,attrs)

    def decompress(self, value):
        imgs=[img for img in str(value).split('.')]
        return imgs

class CityForm(forms.ModelForm):
    class Meta:
        model=City
        fields=['city','region','country']

        widgets={
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'region':forms.TextInput(attrs={'class':'form-control','empty_value':True}),
            'country':forms.TextInput(attrs={'class':'form-control','empty_value':True})
            }


class StreetForm(forms.ModelForm):
    class Meta:
        model=Street
        fields=['name']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            }

class DistrictForm(forms.ModelForm):
    class Meta:
        model=District
        fields=['name']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            }
        
class  FlatForm(forms.ModelForm):

    

    class Meta:
        model=Flat
        fields=['author_object','types','city','street','district',
                'rooms', 'floor', 'floors', 'square', 'plan', 'price', 'text_info']
        widgets={
            'author_object':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'street':forms.Select(attrs={'class':'form-select','empty_value':True}),
            'district':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'rooms':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True }),
            'floor':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'plan':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'text_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
          
           }
class  FlatFormUpdate(forms.ModelForm):
    flat_image=forms.ImageField(label=u'Фотографии', widget=forms.ClearableFileInput(attrs={'class':'form-control','multiple': 'multiple', 'empty_value':True}))
    

    class Meta:
        model=Flat
        fields=['author_object','types','city','street','district',
                'rooms', 'floor', 'floors', 'square', 'plan', 'price', 'text_info']
        widgets={
            'author_object':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'street':forms.Select(attrs={'class':'form-select','empty_value':True}),
            'district':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'rooms':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True }),
            'floor':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'plan':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'text_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
          
           }
class  HouseForm(forms.ModelForm):


    class Meta:
        model=House
        fields=['author_object','types','city','street','district',
                'rooms', 'floor', 'land_part', 'square', 'land_square', 'price', 'text_info']

        widgets={
            'author_object':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'street':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'district':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'rooms':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True }),
            'floor':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_part':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_square':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'text_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
           }
class  SmartflatForm(forms.ModelForm):


    class Meta:
        model=Smartflat
        fields=['author_object','types','city','street','district',
                'rooms', 'floor', 'floors', 'square', 'part', 'price', 'text_info']

        widgets={
            'author_object':forms.TextInput(attrs={'class':'form-control', 'empty_value':True}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'street':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'district':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'rooms':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True }),
            'floor':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'part':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'text_info':forms.Textarea(attrs={'class':'form-control', 'empty_value':True}),
           }


class  SearchFlatForm(forms.ModelForm):


    class Meta:
        model=SearchFlat
        fields=['date_begin','date_end','types','city','street','district','rooms_min', 'rooms_max',
                'floor_min', 'floor_max','floors_min','floors_max',
                'square_min', 'square_max', 'price_min','price_max']

        widgets={
            #'date_begin':forms.SelectDateWidget(years=range(2014, date.today().year+1),attrs={'class':'form-control', 'empty_value':True}),
            'date_begin':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
            #'date_end':forms.SelectDateWidget(years=range(2014, date.today().year+1),attrs={'class':'form-control', 'empty_value':True}),
            'date_end':forms.DateInput(attrs={'class':'form-control', 'empty_value':True, 'type':'date'}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),
            'street':forms.SelectMultiple(attrs={'class':'form-control','empty_value':True}),
            'district':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}),
            'rooms_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'rooms_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            
           }
 
class  SearchHouseForm(forms.ModelForm):


    class Meta:
        model=SearchHouse
        fields=['date_begin','date_end','types','city','street','district','rooms_min', 'rooms_max',
                'floor_min', 'floor_max','land_part_min','land_part_max',
                'square_min', 'square_max', 'price_min','price_max',
                'land_square_min','land_square_max']

        widgets={
            'date_begin':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
            'date_end':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'street':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}),
            'district':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}),#choice
            'rooms_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'rooms_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_part_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_part_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_square_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'land_square_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            
           }
 
class  SearchSmartflatForm(forms.ModelForm):


    class Meta:
        model=SearchSmartFlat
        fields=['date_begin','date_end','types','city','street','district','rooms_min', 'rooms_max',
                'floor_min', 'floor_max','floors_min','floors_max',
                'square_min', 'square_max', 'price_min','price_max']

        widgets={
            'date_begin':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
            'date_end':forms.DateInput(attrs={'class':'form-control', 'empty_value':True,'type':'date'}),
            'types':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control', 'empty_value':True}),#choice
            'street':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}),
            'district':forms.SelectMultiple(attrs={'class':'form-control', 'empty_value':True}),#choice
            'rooms_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'rooms_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floor_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'floors_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'square_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_min':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            'price_max':forms.NumberInput(attrs={'class':'form-control', 'empty_value':True}),
            
           }


##        def save(self):
##            new_flat=Flat.objects.create(types=self.cleaned_data['types'],
##                                         city=self.cleaned_data['city'],
##                                         street=self.cleaned_data['street'],
##                                         district=self.cleaned_data['district'],
##                                         price=self.cleaned_data['price'],
##                                         text_info=self.cleaned_data['text_info'],
##                                         author_object=self.cleaned_data['author_object'],
##                                         rooms=self.cleaned_data['rooms'],
##                                         floor=self.cleaned_data['floor'],
##                                         floors=self.cleaned_data['floors'],
##                                         square=self.cleaned_data['square'],
##                                         plan=self.cleaned_data['plan'],)
##            return new_flat

