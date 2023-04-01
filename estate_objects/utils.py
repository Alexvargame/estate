from django.shortcuts import render, redirect
from django.views.generic import View
from django.shortcuts import get_object_or_404


from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Flat, District, Street
from datetime import datetime, date, time

class ObjectDetailMixin:
    model=None
    template=None
    #obj_id=model.__name__.lower()+'_id'
    def get(self, request,flat_id):
        obj_id=self.model.__name__.lower()+'_id'
        obj=get_object_or_404(self.model,id=obj_id)
        return render(request, self.template, context={self.model.__name__.lower():obj,'s':obj_id})
            
class ObjectCreateMixin:
    form_model=None
    template=None
    initials=None
    def get(self, request):
        self.initials['author_object']=request.user.username
        form=self.form_model(initial=self.initials)
        return render(request, self.template, context={'form':form})

    def post(self, request):
        bound_form=self.form_model(request.POST)
        if bound_form.is_valid():
            new_obj=bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form':bound_form})

class ObjectSearchMixin:
    form_model=None
    name_model=None
    template=None
    template_l=None
    initials=None
    
    def get(self, request):
        query_dist=[]
        query_st=[]
        phone_numbers={}
        for us in User.objects.all():
            phone_numbers[us.username]=[phn for phn in us.profile.phone_number.all()]

        if request.GET:
            
            bound_form=self.form_model(request.GET, initial=self.initials)
            if bound_form['district'].value()[0]:
                query_dist=bound_form['district'].value()
            else:
                for dist in District.objects.all():
                    query_dist.append(dist.name)
            if bound_form['street'].value()[0]:
                query_st=bound_form['street'].value()
            else:
                for st in Street.objects.all():
                    query_st.append(st.name)
            date_b=[int(i) for i in request.GET['date_begin'].split('-')]
            date_e=[int(i) for i in request.GET['date_end'].split('-')] 
            if self.name_model.__name__=='Flat':
                objs=self.name_model.objects.filter(types=request.GET['types'],city=request.GET['city'],district__in=query_dist,
                                            street__in=query_st, add_date__range=(date(date_b[0],date_b[1],date_b[2]),date(date_e[0],date_e[1],date_e[2])),
                                     rooms__range=(request.GET['rooms_min'],request.GET['rooms_max']),floors__range=(request.GET['floors_min'],request.GET['floors_max']),
                                    floor__range=(request.GET['floor_min'],request.GET['floor_max']),square__range=(request.GET['square_min'],request.GET['square_max']),
                                    price__range=(request.GET['price_min'],request.GET['price_max']))
                
            elif self.name_model.__name__=='House':
                objs=self.name_model.objects.filter(types=request.GET['types'],city=request.GET['city'],district__in=query_dist,street__in=query_st,
                     add_date__range=(date(date_b[0],date_b[1],date_b[2]),date(date_e[0],date_e[1],date_e[2])),
                     rooms__range=(request.GET['rooms_min'],request.GET['rooms_max']),land_part__range=(request.GET['land_part_min'],request.GET['land_part_max']),
                     floor__range=(request.GET['floor_min'],request.GET['floor_max']),square__range=(request.GET['square_min'],request.GET['square_max']),
                     land_square__range=(request.GET['land_square_min'],request.GET['land_square_max']),price__range=(request.GET['price_min'],request.GET['price_max']))
            elif self.name_model.__name__=='Smartflat':
                objs=self.name_model.objects.filter(types=request.GET['types'],city=request.GET['city'],district__in=query_dist,street__in=query_st,
                       add_date__range=(date(date_b[0],date_b[1],date_b[2]),date(date_e[0],date_e[1],date_e[2])),
                                     rooms__range=(request.GET['rooms_min'],request.GET['rooms_max']),floors__range=(request.GET['floors_min'],request.GET['floors_max']),
                                    floor__range=(request.GET['floor_min'],request.GET['floor_max']),square__range=(request.GET['square_min'],request.GET['square_max']),
                                    price__range=(request.GET['price_min'],request.GET['price_max']))
            us=User.objects.all()
            str_url=''
            for i in reversed(request.GET):
                if i=='district':
                    for q in reversed(query_dist):
                        str_url=i+'='+q+'&'+str_url
                elif i=='street':
                    for q in reversed(query_st):
                        str_url=i+'='+q+'&'+str_url
                else:
                    str_url=i+'='+request.GET[i]+'&'+str_url
                    
            paginator=Paginator(objs,2)

            page_number=request.GET.get('page',1)
            page=paginator.get_page(page_number)

            is_paginated=page.has_other_pages()
            if page.has_previous():
                prev_url='?{}&page={}'.format(str_url[:-1],page.previous_page_number())
            else:
                prev_url=''

            if page.has_next():
                next_url='?{}&page={}'.format(str_url[:-1],page.next_page_number())
            else:
                next_url=''

            context={
                
                self.name_model.__name__.lower()+'s':page,
                'is_paginated':is_paginated,
                'next_url':next_url,
                'prev_url':prev_url,
                's1':str_url[:-1],
                'phone_numbers':phone_numbers
                }
        


            return render(request,self.template_l, context=context)
        else:
            form=self.form_model(initial=self.initials)
            return render(request, self.template, context={'form':form})
   
##class ObjectUpdateMixin:
##    model=None
##    form_model=None
##    template=None
##    def get(self,request,slug):
##        obj=self.model.objects.get(slug__iexact=slug)
##        bound_form=self.form_model(instance=obj)
##        return render(request, self.template, context={'form':bound_form,self.model.__name__.lower():obj})
##    def post(self,request,slug):
##        obj=self.model.objects.get(slug__iexact=slug)
##        bound_form=self.form_model(request.POST, instance=obj)
##        if bound_form.is_valid():
##                new_obj=bound_form.save()
##                return redirect(new_obj)
##        return render(request, self.template, context={'form':bound_form, self.model.__name__.lower():obj})
##
##class ObjectDeleteMixin:
##    model=None
##    template=None
##    redirect_url=None
##    def get(self,request, slug):
##        obj=self.model.objects.get(slug__iexact=slug)
##        return render(request, self.template, context={self.model.__name__.lower():obj})
##    def post(self, request, slug):
##        obj=self.model.objects.get(slug__iexact=slug)
##        obj.delete()
##        return redirect(self.redirect_url)
