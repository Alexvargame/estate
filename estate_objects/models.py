
from django.db import models
from multiselectfield import MultiSelectField
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, date, time


class City(models.Model):
        
        city = models.CharField(max_length=40, db_index=True)
        region = models.CharField(max_length=40)
        country = models.CharField(max_length=40)
        def get_absolute_url(self):
            return reverse('city_detail_url', kwargs={'city_id':self.id})
        def get_update_url(self):
            return reverse('city_update_url', kwargs={'city_id':self.id})
        def get_delete_url(self):
            return reverse('city_delete_url', kwargs={'city_id':self.id})
        def __str__(self):
            return " Название- %s Регион- %s Страна- %s" % (self.city, self.region,self.country)
       
class Street(models.Model):
        
        name = models.CharField(max_length=40, db_index=True)

        def get_absolute_url(self):
            return reverse('street_detail_url', kwargs={'street_id':self.id})
        def get_update_url(self):
            return reverse('street_update_url', kwargs={'street_id':self.id})
        def get_delete_url(self):
            return reverse('street_delete_url', kwargs={'street_id':self.id})
        def __str__(self):
            return " Название- " % (self.name)

        
class District(models.Model):
        
        name = models.CharField(max_length=40, db_index=True)

        def get_absolute_url(self):
            return reverse('district_detail_url', kwargs={'district_id':self.id})
        def get_update_url(self):
            return reverse('district_update_url', kwargs={'district_id':self.id})
        def get_delete_url(self):
            return reverse('district_delete_url', kwargs={'district_id':self.id})
        def __str__(self):
            return " Название- " % (self.name)
        
class Flat(models.Model):

        typ=[('Квартира','Квартира')]
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        plans=[('улучшенка','улучшенка'),('обычная','обычная')]
        types = models.CharField(max_length=10, choices=sorted(typ))
        city = models.CharField(max_length=20,choices=sorted(cities),blank=True)
        street = models.CharField(max_length=30,choices=sorted(streets), blank=True)
        district = models.CharField(max_length=30, choices=sorted(districts),blank=True)
        price =models.FloatField(null=True, blank=True)
        add_date = models.DateTimeField(auto_now_add=True)
        text_info = models.TextField(max_length=300, blank=True)
        author_object= models.CharField(max_length=10, blank=True)
        rooms=models.IntegerField(blank=True, null=True)
        floor=models.IntegerField(blank=True, null=True)
        floors=models.IntegerField(blank=True, null=True)
        square=models.FloatField(blank=True, null=True)
        plan=models.CharField(max_length=30, choices=plans, blank=True)

        def get_absolute_url(self):
            return reverse('flat_detail_url', kwargs={'flat_id':self.id})
        def get_update_url(self):
            return reverse('flat_update_url', kwargs={'flat_id':self.id})
        def get_delete_url(self):
            return reverse('flat_delete_url', kwargs={'flat_id':self.id})
        def __str__(self):
            return " Автор- %s Дата- %s Тип объекта- %s Город- %s Район- %s Улица- %s Кол-во комнат- %s Этаж/Этажность- %s/%s Планировка- %s Площадь- %s Цена- %s Информация %s  " % (self.author_object, self.add_date,
                  self.types, self.city, self.district, self.street, 
                  self.rooms, self.floor, self.floors, self.plan,  self.square, self.price, self.text_info)

        class Meta:
                ordering=['-add_date']
class FlatImage(models.Model):
        flat=models.ForeignKey(Flat,related_name='flat_image',on_delete=models.CASCADE)
        image_data= models.ImageField(default='default.jpg', upload_to='flats/pics', height_field=None , width_field=None , max_length=100,blank=True, null=True)
        image_url = models.URLField(blank=True)
        def get_remote_url(self):
                if self.image_url and not self.image_data:
                        image_temp=NamedTemporaryFile(delete=True)
                        image_temp.write(request.get(self.image_url).content)
                        image_temp.flush()
                        self.image_data.save(f'photo_{self.pk}.jpg', File(image_temp))
                self.save()         
       
        def get_absolute_url(self):
            return reverse('image_detail_url', kwargs={'flatimage_id':self.id})
        def get_delete_url(self):
            return reverse('image_delete_url', kwargs={'flatimage_id':self.id})


class House(models.Model):

        typ=[('Дом','Дом'),('Часть дома','Часть дома')]
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        types = models.CharField(max_length=10, choices=sorted(typ))
        city = models.CharField(max_length=20, choices=sorted(cities), blank=True)#choice
        street = models.CharField(max_length=30,choices=sorted(streets), blank=True)#choice
        district = models.CharField(max_length=30,choices=sorted(districts), blank=True)#choice
        price =models.FloatField(null=True, blank=True)
        add_date = models.DateTimeField(auto_now_add=True)
        text_info = models.TextField(max_length=300, blank=True)
        author_object= models.CharField(max_length=10, blank=True)
        rooms=models.IntegerField(blank=True, null=True)
        floor=models.IntegerField(blank=True, null=True)
        square=models.FloatField(blank=True, null=True)
        land_part=models.FloatField(blank=True, null=True)
        land_square=models.FloatField(blank=True, null=True)
        
        
        def get_absolute_url(self):
            return reverse('house_detail_url', kwargs={'house_id':self.id})
        def get_update_url(self):
            return reverse('house_update_url', kwargs={'house_id':self.id})
        def get_delete_url(self):
            return reverse('house_delete_url', kwargs={'house_id':self.id})
        def __str__(self):
            return " Автор- %s Дата- %s Тип объекта- %s Город- %s Район- %s Улица- %s Кол-во комнат- %s Этаж- %s/ Площадь- %s Цена- %s Часть участка/Площадь участка-%s/%s Информация %s  " % (self.author_object, self.add_date,
                  self.types, self.city, self.district, self.street, 
                  self.rooms, self.floor,self.square, self.price, self.land_part, self.land_square, self.text_info)
        class Meta:
                ordering=['-add_date']

class Smartflat(models.Model):

        typ=[('Квартира','Квартира'),('Часть','Часть')]
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        types = models.CharField(max_length=10, choices=sorted(typ))
        city = models.CharField(max_length=20, choices=sorted(cities),blank=True)#choice
        street = models.CharField(max_length=30, choices=sorted(streets), blank=True)#choice
        district = models.CharField(max_length=30, choices=sorted(districts), blank=True)
        price =models.FloatField(null=True, blank=True)
        add_date = models.DateTimeField(auto_now_add=True)
        text_info = models.TextField(max_length=300, blank=True)
        author_object= models.CharField(max_length=10, blank=True)
        rooms=models.IntegerField(blank=True, null=True)
        floor=models.IntegerField(blank=True, null=True)
        floors=models.IntegerField(blank=True, null=True)
        square=models.FloatField(blank=True, null=True)
        part =models.FloatField(null=True, blank=True)
        
        def get_absolute_url(self):
            return reverse('smart_flat_detail_url', kwargs={'smartflat_id':self.id})
        def get_update_url(self):
            return reverse('smart_flat_update_url', kwargs={'smartflat_id':self.id})
        def get_delete_url(self):
            return reverse('smart_flat_delete_url', kwargs={'smartflat_id':self.id})
        def __str__(self):
            return " Автор- %s Дата- %s Тип объекта- %s Город- %s Район- %s Улица- %s Кол-во комнат- %s Этаж/Этажность- %s/%s Часть- %s Площадь- %s Цена- %s Информация %s  " % (self.author_object, self.add_date,
                  self.types, self.city, self.district, self.street, 
                  self.rooms, self.floor, self.floors, self.part,  self.square, self.price, self.text_info)
        class Meta:
                ordering=['-add_date']


class SearchFlat(models.Model):

        typ=[('Квартира','Квартира')]
        
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        plans=[('улучшенка','улучшенка'),('обычная','обычная')]
        types = models.CharField(max_length=10, choices=sorted(typ),default=typ[0])
        city = models.CharField(max_length=20, choices=sorted(cities), blank=True, default=cities[0])#choice
        street =models.CharField(max_length=300,choices=sorted(streets), blank=True, default=streets[0])
        #street_s =models.CharField(max_length=200, blank=True,null=True)
        district = models.CharField(max_length=30,choices=sorted(districts),default=districts[0], blank=True)#choic
        price_min =models.FloatField(null=True, blank=True)
        price_max =models.FloatField(null=True, blank=True)
        date_begin = models.DateTimeField()
        date_end = models.DateTimeField()
        rooms_min=models.IntegerField(blank=True, null=True)
        rooms_max=models.IntegerField(blank=True, null=True)
        floor_min=models.IntegerField(blank=True, null=True)
        floor_max=models.IntegerField(blank=True, null=True)
        floors_min=models.IntegerField(blank=True, null=True)
        floors_max=models.IntegerField(blank=True, null=True)
        square_min=models.FloatField(blank=True, null=True)
        square_max=models.FloatField(blank=True, null=True)
        #plan=models.CharField(max_length=30, choices=plans, blank=True)#choice
        
class SearchHouse(models.Model):

        typ=[('Дом','Дом'),('Часть дома','Часть дома')]
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        types = models.CharField(max_length=10, choices=sorted(typ))
        city = models.CharField(max_length=20, choices=sorted(cities), blank=True,default=cities[0])#choice
        street = models.CharField(max_length=30,choices=sorted(streets), blank=True, default=streets[0])#choice
        district = models.CharField(max_length=30,choices=sorted(districts),  blank=True, default=districts[0])#choic
        price_min =models.FloatField(null=True, blank=True)
        price_max =models.FloatField(null=True, blank=True)
        date_begin = models.DateTimeField()
        date_end = models.DateTimeField()
        rooms_min=models.IntegerField(blank=True, null=True)
        rooms_max=models.IntegerField(blank=True, null=True)
        floor_min=models.IntegerField(blank=True, null=True)
        floor_max=models.IntegerField(blank=True, null=True)
        land_part_min=models.FloatField(blank=True, null=True)
        land_part_max=models.FloatField(blank=True, null=True)
        land_square_min=models.FloatField(blank=True, null=True)
        land_square_max=models.FloatField(blank=True, null=True)
        square_min=models.FloatField(blank=True, null=True)
        square_max=models.FloatField(blank=True, null=True)
        #plan=models.CharField(max_length=30, choices=plans, blank=True)#choice



class SearchSmartFlat(models.Model):

        typ=[('Квартира','Квартира'),('Часть','Часть')]
        cities =[(obj.city,obj.city) for obj in City.objects.all()]
        streets=[(obj.name,obj.name) for obj in Street.objects.all()]
        districts=[(obj.name,obj.name) for obj in District.objects.all()]
        types = models.CharField(max_length=10, choices=sorted(typ))
        city = models.CharField(max_length=20, choices=sorted(cities),default=cities[0], blank=True)#choice
        street = models.CharField(max_length=30,choices=sorted(streets), blank=True, default=streets[0])#choice
        district = models.CharField(max_length=30,choices=sorted(districts), blank=True,default=districts[0])#choic
        price_min =models.FloatField(null=True, blank=True)
        price_max =models.FloatField(null=True, blank=True)
        date_begin = models.DateTimeField()
        date_end = models.DateTimeField()
        rooms_min=models.IntegerField(blank=True, null=True)
        rooms_max=models.IntegerField(blank=True, null=True)
        floor_min=models.IntegerField(blank=True, null=True)
        floor_max=models.IntegerField(blank=True, null=True)
        floors_min=models.IntegerField(blank=True, null=True)
        floors_max=models.IntegerField(blank=True, null=True)
        square_min=models.FloatField(blank=True, null=True)
        square_max=models.FloatField(blank=True, null=True)
        
        

