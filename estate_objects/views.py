from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.urls import reverse
from .models import Flat, FlatImage,House,Smartflat, City, Street, District
from .utils import ObjectDetailMixin,ObjectCreateMixin,ObjectSearchMixin
from users.models import Profile, PhoneNumber
from django.contrib.auth.models import User
from datetime import datetime, date, time
from .forms import ImageWidget
from django.core.files.base import ContentFile

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FlatForm, HouseForm,SmartflatForm,SearchFlatForm,SearchHouseForm,SearchSmartflatForm, CityForm, StreetForm, DistrictForm, FlatFormUpdate
from django.db.models import Q
from django.core.paginator import Paginator

from .Calendar import *

def main_menu(request):
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    
    return render(request,'estate_objects/main_page.html',context={'num_visits':num_visits+1})

def main_data_menu(request):
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    
    return render(request,'estate_objects/main_data_page.html')

def visits(request):
    num_visits=request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits+1
    return render(request,'estate_objects/main_data_page.html' )

def users_list(request):
    users=User.objects.all()
    count_obj={}
    phone_numbers={}
    for us in users:
        number_object=[]
        f=Flat.objects.filter(author_object=us.username)
        h=House.objects.filter(author_object=us.username)
        sf=Smartflat.objects.filter(author_object=us.username)
        number_object.extend(f)
        number_object.extend(h)
        number_object.extend(sf)
        count_obj[us.username]=len(number_object)
        phone_numbers[us.username]=[phn for phn in us.profile.phone_number.all()]
        
 
    return render(request,'estate_objects/users/users_list.html', context={'users':users, 'count_obj':count_obj, 'phone_numbers':phone_numbers})


def search_for_phone_number(request):
    search_query=request.GET.get('search','')
    phone_number_object=[]
    numbers=[]
    if search_query:
        users=User.objects.all()
        for us in users:
            if search_query in [phn.phone_number for phn in PhoneNumber.objects.all()]:
                
                numbers=[phn for phn in us.profile.phone_number.all()]
                numbers.remove(search_query)
                f=Flat.objects.filter(author_object=us.username)
                h=House.objects.filter(author_object=us.username)
                sf=Smartflat.objects.filter(author_object=us.username)
                phone_number_object.extend(f)
                phone_number_object.extend(h)
                phone_number_object.extend(sf)
        paginator=Paginator(phone_number_object,3)

        page_number=request.GET.get('page',1)
        page=paginator.get_page(page_number)

        is_paginated=page.has_other_pages()
        if page.has_previous():
            prev_url='?search={}&page={}'.format(search_query,page.previous_page_number())
        else:
            prev_url=''

        if page.has_next():
            next_url='?search={}&page={}'.format(search_query,page.next_page_number())
        else:
            next_url=''

        context={
            'phone_number_object':page,
            'is_paginated':is_paginated,
            'next_url':next_url,
            'prev_url':prev_url,
            'numbers':numbers,
            'len':len(numbers),
            'lenobj':len(phone_number_object),
            'sq':search_query,
            }
        
        return render(request,'estate_objects/search_for_phone_number.html', context=context)
    else:
        return render(request,'estate_objects/main_page.html')

def view_big_image(request, flat_id):
    flat=get_object_or_404(Flat, id=flat_id)
   
    images=['/media/'+str(im.image_data) for im in FlatImage.objects.filter(flat=flat)]
    return render(request,'estate_objects/flat_big_image.html', context={'flat':flat,'images':images})


def delete_image(request,flat_id, flatimage_id):
    
    flat=Flat.objects.get(id=flat_id)
    form=FlatForm(instance=flat)
    image=get_object_or_404(FlatImage, id=flatimage_id)
    image.delete()
    images=['/media/'+str(im.image_data) for im in FlatImage.objects.filter(flat=flat)]
    imgs=[img for img in FlatImage.objects.filter(flat=flat)]
    return redirect(flat)



class Objects_for_author(View):
    def get(self,request, author_object):
        
        author_list_object=[]
        f=Flat.objects.filter(author_object=author_object)
        h=House.objects.filter(author_object=author_object)
        sf=Smartflat.objects.filter(author_object=author_object)
        author_list_object.extend(f)
        author_list_object.extend(h)
        author_list_object.extend(sf)
        return render(request,'estate_objects/objects_for_author.html', context={'author_list_object':author_list_object})
        
    
class Objects_for_phone_number(View):
    def get(self,request, phone_number):
        us=User.objects.filter(user.profile.phone_number==phone_number)
        phone_number_object=[]
        f=Flat.objects.filter(author_object=us.username)
        h=House.objects.filter(author_object=us.username)
        sf=Smartflat.objects.filter(author_object=us.username)
        phone_number_object.extend(f)
        phone_number_object.extend(h)
        phone_number_object.extend(sf)
        return render(request,'estate_objects/objects_for_phone_number.html', context={'phone_number_object':phone_number_object})

class User_profile(View):
    def get(self,request, author_object):
        user_profile=get_object_or_404(User,username=author_object)
        return render(request,'estate_objects/user_profile.html', context={'user_profile':user_profile})
        



class FlatCreate(LoginRequiredMixin,ObjectCreateMixin, View):
     form_model=FlatForm
     template='estate_objects/flat_create.html'
     initials={'rooms':1,'floor':1,'floors':50,'price':1, 'square':1}
     raise_exception=True
     
class FlatDetailView(View):
    
    def get (self, request, flat_id):
       
        flat=get_object_or_404(Flat, id=flat_id)
        images=['/media/'+str(im.image_data) for im in FlatImage.objects.filter(flat=flat)]
        us=User.objects.filter(username=flat.author_object)
        phone_number=[phn for phn in us[0].profile.phone_number.all()]

        return render(request,'estate_objects/flat_detail.html', context={'flat':flat,'phone_number':phone_number,'images':images})


        
def flats_list(request):
    
    flats=Flat.objects.order_by('-add_date')[:15]
    phone_numbers={}
    for us in User.objects.all():
        phone_numbers[us.username]=[phn for phn in us.profile.phone_number.all()]
    paginator=Paginator(flats,3)
    
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)

    is_paginated=page.has_other_pages()
    if page.has_previous():
        prev_url='?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?page={}'.format(page.next_page_number())
    else:
        next_url=''

    context={
        'flats':page,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url':prev_url,
        'us':us,
        'phone_numbers':phone_numbers
        }
    
    return render(request,'estate_objects/flats_list.html', context=context)

    

class FlatUpdate(LoginRequiredMixin,View):
    
    def get(self, request, flat_id):
        flat=Flat.objects.get(id=flat_id)
        form=FlatFormUpdate(instance=flat)
        images=['/media/'+str(im.image_data) for im in FlatImage.objects.filter(flat=flat) if im]
        imgs=[img for img in FlatImage.objects.filter(flat=flat) if img]
        return render(request, 'estate_objects/flat_update.html', context={'form':form, 'flat':flat,'images':images, 'imgs':imgs})
    def post(self, request, flat_id):
   
        flat=Flat.objects.get(id=flat_id)
        bound_form=FlatFormUpdate(request.POST, request.FILES, instance=flat)
        if bound_form.is_valid():
            new_flat=bound_form.save()
            for f in request.FILES.getlist('flat_image'):
                data=f.read()
                image=FlatImage(flat=new_flat)
                image.image_data.save(f.name, ContentFile(data))
                image.save()
            return redirect(new_flat)
        context={
            'form':bound_form,
            'flat':flat,
            's':request.FILES.getlist('flat_image')
            }
        return render(request, 'estate_objects/flat_update.html', context=context) 
       

class FlatDelete(LoginRequiredMixin, View):
    
    def get(self, request, flat_id):
        flat=Flat.objects.get(id=flat_id)
        return render(request, 'estate_objects/flat_delete.html', context={'flat':flat})

    def post(self, request, flat_id):
        flat=Flat.objects.get(id=flat_id)
        flat.delete()
        return redirect(reverse('flats_list_url'))



class SearchFlat(ObjectSearchMixin,View):

    form_model=SearchFlatForm
    name_model=Flat
    template='estate_objects/search_flat.html'
    template_l='estate_objects/flats_list_search.html'
    initials={'rooms_min':0,'rooms_max':20,'floor_min':1,'floor_max':50,'floors_min':1,'floors_max':50,'price_min':1,
                                       'price_max':1000000,'square_min':1,'square_max':100000,'date_begin': date(2014,1,1),'date_end': date.today()}
  
    
class SearchHouse(ObjectSearchMixin,View):
    form_model=SearchHouseForm
    name_model=House
    template='estate_objects/search_house.html'
    template_l='estate_objects/houses_list_search.html'
    initials={'rooms_min':1,'rooms_max':20,'floor_min':1,'floor_max':50,'land_part_min':0.1,'land_part_max':1,
              'land_square_min':1,'land_square_max':1000,'price_min':1,
                'price_max':1000000,'square_min':1,'square_max':100000,'date_begin': date(2014,1,1),'date_end': date.today()}

class SearchSmartflat(ObjectSearchMixin,View):
    form_model=SearchSmartflatForm
    name_model=Smartflat
    template='estate_objects/search_smart_flat.html'
    template_l='estate_objects/smart_flats_list_search.html'
    initials={'rooms_min':1,'rooms_max':20,'floor_min':1,'floor_max':50,'floors_min':1,'floors_max':50,'price_min':1,
                                       'price_max':1000000,'square_min':1,'square_max':100000,'date_begin': date(2014,1,1),'date_end': date.today()}
  

   
def houses_list(request):
    houses=House.objects.order_by('-add_date')[:15]
    phone_numbers={}
    for us in User.objects.all():
        phone_numbers[us.username]=[phn for phn in us.profile.phone_number.all()]
    paginator=Paginator(houses,3)
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)

    is_paginated=page.has_other_pages()
    if page.has_previous():
        prev_url='?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?page={}'.format(page.next_page_number())
    else:
        next_url=''

    context={
        'houses':page,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url':prev_url,
        'us':us,
        'phone_numbers':phone_numbers
        }
    

    return render(request,'estate_objects/houses_list.html', context=context)


class HouseDetailView(View):  
    def get (self, request, house_id):
        house=get_object_or_404(House, id=house_id)
        us=User.objects.filter(username=house.author_object)
        phone_number=[phn for phn in us[0].profile.phone_number.all()]
        return render(request,'estate_objects/house_detail.html', context={'house':house,'phone_number':phone_number})

        


class HouseCreate(LoginRequiredMixin,ObjectCreateMixin,View):
     form_model=HouseForm
     template='estate_objects/house_create.html'
     initials={'rooms':1,'floor':1,'land_square':1,'land_part':0.1,'price':1, 'square':1}
     raise_exception=True

class HouseUpdate(LoginRequiredMixin,View):
    def get(self, request, house_id):
        house=House.objects.get(id=house_id)
        bound_form=HouseForm(instance=house)
        return render(request, 'estate_objects/house_update.html', context={'form':bound_form, 'house':house})
    def post(self, request,house_id):
        house=House.objects.get(id=house_id)
        bound_form=HouseForm(request.POST, instance=house)
        if bound_form.is_valid():
            new_house=bound_form.save()
            return redirect(new_house)
        return render(request, 'estate_objects/house_update.html', context={'form':bound_form, 'house':house}) 
       

class HouseDelete(LoginRequiredMixin,View):
    def get(self, request, house_id):
        house=House.objects.get(id=house_id)
        return render(request, 'estate_objects/house_delete.html', context={'house':house})

    def post(self, request, house_id):
        house=House.objects.get(id=house_id)
        house.delete() 
        return redirect(reverse('houses_list_url'))

class SmartflatCreate(LoginRequiredMixin,ObjectCreateMixin, View):
     form_model=SmartflatForm
     template='estate_objects/smart_flat_create.html'
     initials={'rooms':1,'floor':1,'floors':1,'price':1, 'square':1, 'part':1}
     raise_exception=True

class SmartflatDetailView(View):  
    def get (self, request, smartflat_id):
        smartflat=get_object_or_404(Smartflat, id=smartflat_id)
        us=User.objects.filter(username=smartflat.author_object)
        phone_number=[phn for phn in us[0].profile.phone_number.all()]
        return render(request,'estate_objects/smart_flat_detail.html', context={'smartflat':smartflat,'phone_number':phone_number})

def smart_flats_list(request):
    smartflats=Smartflat.objects.order_by('-add_date')[:15]
    phone_numbers={}
    for us in User.objects.all():
        phone_numbers[us.username]=[phn for phn in us.profile.phone_number.all()]
    paginator=Paginator(smartflats,3)
    page_number=request.GET.get('page',1)
    page=paginator.get_page(page_number)

    is_paginated=page.has_other_pages()
    if page.has_previous():
        prev_url='?page={}'.format(page.previous_page_number())
    else:
        prev_url=''

    if page.has_next():
        next_url='?page={}'.format(page.next_page_number())
    else:
        next_url=''

    context={
        'smartflats':page,
        'is_paginated':is_paginated,
        'next_url':next_url,
        'prev_url':prev_url,
        'us':us,
        'phone_numbers':phone_numbers
        }
    

    return render(request,'estate_objects/smart_flats_list.html', context=context)

class SmartflatUpdate(LoginRequiredMixin,View):
    def get(self, request, smartflat_id):
        smartflat=Smartflat.objects.get(id=smartflat_id)
        bound_form=SmartflatForm(instance=smartflat)
        return render(request, 'estate_objects/smart_flat_update.html', context={'form':bound_form, 'smartflat':smartflat})
    def post(self, request, smartflat_id):
        smartflat=Smartflat.objects.get(id=smartflat_id)
        bound_form=SmartflatForm(request.POST, instance=smartflat)
        if bound_form.is_valid():
            new_smartflat=bound_form.save()
            return redirect(new_smartflat)
        return render(request, 'estate_objects/smart_flat_update.html', context={'form':bound_form, 'smartflat':smartflat})
    
class SmartflatDelete(LoginRequiredMixin,View):
    def get(self, request, smartflat_id):
        smartflat=Smartflat.objects.get(id=smartflat_id)
        return render(request, 'estate_objects/smart_flat_delete.html', context={'smartflat':smartflat})

    def post(self, request, smartflat_id):
        smartflat=Smartflat.objects.get(id=smartflat_id)
        smartflat.delete()
        return redirect(reverse('smart_flats_list_url'))


class CityCreate(LoginRequiredMixin,ObjectCreateMixin, View):
     form_model=CityForm
     template='estate_objects/city/city_create.html'
     initials={}
     raise_exception=True
def city_list(request):
    cities=City.objects.all()
    return render(request,'estate_objects/city/cities_list.html', context={'cities':cities})
class CityDetailView(View):  
    def get (self, request, city_id):
        city=get_object_or_404(City, id=city_id)
        return render(request,'estate_objects/city/city_detail.html', context={'city':city})

class CityUpdate(LoginRequiredMixin,View):
    
    def get(self, request, city_id):
        city=City.objects.get(id=city_id)
        bound_form=CityForm(instance=city)
        return render(request, 'estate_objects/city/city_update.html', context={'form':bound_form, 'city':city})
    def post(self, request,city_id):
        city=City.objects.get(id=city_id)
        bound_form=CityForm(request.POST, instance=city)
        if bound_form.is_valid():
            new_city=bound_form.save()
            return redirect(new_city)
        return render(request, 'estate_objects/city/city_update.html', context={'form':bound_form, 'city':city}) 
       

class CityDelete(LoginRequiredMixin, View):
    
    def get(self, request, city_id):
        city=City.objects.get(id=city_id)
        return render(request, 'estate_objects/city/city_delete.html', context={'city':city})

    def post(self, request, city_id):
        city=City.objects.get(id=city_id)
        city.delete()
        return redirect(reverse('cities_list_url'))

    
class StreetCreate(LoginRequiredMixin,ObjectCreateMixin, View):
     form_model=StreetForm
     template='estate_objects/street/street_create.html'
     initials={}
     raise_exception=True
def street_list(request):
    streets=Street.objects.all()
    return render(request,'estate_objects/street/streets_list.html', context={'streets':streets})
class StreetDetailView(View):  
    def get (self, request, street_id):
        street=get_object_or_404(Street, id=street_id)
        return render(request,'estate_objects/street/street_detail.html', context={'street':street})

class StreetUpdate(LoginRequiredMixin,View):
    
    def get(self, request, street_id):
        street=Street.objects.get(id=street_id)
        bound_form=StreetForm(instance=street)
        return render(request, 'estate_objects/street/street_update.html', context={'form':bound_form, 'street':street})
    def post(self, request,street_id):
        street=Street.objects.get(id=street_id)
        bound_form=StreetForm(request.POST, instance=street)
        if bound_form.is_valid():
            new_street=bound_form.save()
            return redirect(new_street)
        return render(request, 'estate_objects/street/street_update.html', context={'form':bound_form, 'street':street}) 
       

class StreetDelete(LoginRequiredMixin, View):
    
    def get(self, request, street_id):
        street=Street.objects.get(id=street_id)
        return render(request, 'estate_objects/street/street_delete.html', context={'street':street})

    def post(self, request, street_id):
        street=Street.objects.get(id=street_id)
        street.delete()
        return redirect(reverse('streets_list_url'))



class DistrictCreate(LoginRequiredMixin,ObjectCreateMixin, View):
     form_model=DistrictForm
     template='estate_objects/district/district_create.html'
     initials={}
     raise_exception=True
     
def district_list(request):
    districts=District.objects.all()
    return render(request,'estate_objects/district/district_list.html', context={'districts':districts})


class DistrictDetailView(View):  
    def get (self, request, district_id):
        district=get_object_or_404(District, id=district_id)
        return render(request,'estate_objects/district/district_detail.html', context={'district':district})

class DistrictUpdate(LoginRequiredMixin,View):
    
    def get(self, request, district_id):
        district=District.objects.get(id=district_id)
        bound_form=DistrictForm(instance=district)
        return render(request, 'estate_objects/district/district_update.html', context={'form':bound_form, 'district':district})
    def post(self, request,district_id):
        district=District.objects.get(id=district_id)
        bound_form=DistrictForm(request.POST, instance=district)
        if bound_form.is_valid():
            new_district=bound_form.save()
            return redirect(new_district)
        return render(request, 'estate_objects/district/district_update.html', context={'form':bound_form, 'district':district}) 
       

class DistrictDelete(LoginRequiredMixin, View):
    
    def get(self, request, district_id):
        district=District.objects.get(id=district_id)
        return render(request, 'estate_objects/district/district_delete.html', context={'district':district})

    def post(self, request, district_id):
        district=District.objects.get(id=district_id)
        district.delete()
        return redirect(reverse('districts_list_url'))


    
