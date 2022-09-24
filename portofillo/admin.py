from xml.parsers.expat import model
from django.contrib import admin
from .models import Slider,Sayac,Hizmetlerimiz,Hizmetlermiz_details,Kurumsal_Aciklama,Musteri_Yorumları,Referanslar,SıkcaSorulanSorular,Calismalar,Sosyal_Media
# Register your models here.



class SliderAdmin(admin.ModelAdmin):
    
    list_display = ('title','eklenme_tarihi','guncellenme_tarihi','kac_gun_once','image_tag')
    list_filter = ('title',)
    ordering = ('title','-guncellenme_tarihi')
    search_fields = ('title',)
 
 
class SayacAdmin(admin.ModelAdmin):

    list_display = ('project_sayac','musteri_sayac','referans_sayac','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')
    list_filter = ('project_sayac','musteri_sayac','referans_sayac')
    ordering = ('-guncellenme_tarihi',)
    search_fields = ('project_sayac',)
    


class HizmetlerimizAdmin(admin.ModelAdmin):

    list_display = ('main_hizmetler_title','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')
    list_filter = ('main_hizmetler_title',)
    ordering = ('-guncellenme_tarihi',)
    search_fields = ('main_hizmetler_title',)
 
 
class HizmetlerimizDetailAdmin(admin.ModelAdmin):
    
    list_display = ('hizmetler','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')
    list_filter = ('hizmetlerimiz_detail_bir',)
    ordering = ('-guncellenme_tarihi',)
    search_fields = ('hizmetlerimiz_detail_bir',)


class KurumsalAcıklamaAdmin(admin.ModelAdmin):
    
    list_display = ('kurumsal_aciklama_title','eklenme_tarihi','guncellenme_tarihi','kac_gun_once','image_tag')
    list_filter = ('kurumsal_aciklama_title',)
    ordering = ('-guncellenme_tarihi',)
    search_fields = ('kurumsal_aciklama_title',)
    
    
    
class ReferanslarAdmin(admin.ModelAdmin):
    
    list_display = ('Referans','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')

    list_filter = ('referans_bir',)
    ordering = ('-guncellenme_tarihi',)
    search_fields = ('referans_bir',)
    

class SSSAdmin(admin.ModelAdmin):
    
    list_display = ('FAQ','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')

    ordering = ('-guncellenme_tarihi',)
    
    

class CalismalarAdmin(admin.ModelAdmin):
    
  
    list_display = ('calismalar','eklenme_tarihi','guncellenme_tarihi','kac_gun_once','image_tag_bir','image_tag_iki','image_tag_uc')

    ordering = ('-guncellenme_tarihi',)
    
    
class SosyalMedyaAdmin(admin.ModelAdmin):
    list_display = ('SosyalMedya','eklenme_tarihi','guncellenme_tarihi','kac_gun_once')
    ordering = ('-guncellenme_tarihi',)
    

    
admin.site.register(Slider,SliderAdmin)
admin.site.register(Sayac,SayacAdmin)
admin.site.register(Hizmetlerimiz,HizmetlerimizAdmin)
admin.site.register(Hizmetlermiz_details,HizmetlerimizDetailAdmin)
admin.site.register(Kurumsal_Aciklama,KurumsalAcıklamaAdmin)
admin.site.register(Musteri_Yorumları)
admin.site.register(Referanslar,ReferanslarAdmin)
admin.site.register(SıkcaSorulanSorular,SSSAdmin)
admin.site.register(Calismalar,CalismalarAdmin)
admin.site.register(Sosyal_Media,SosyalMedyaAdmin)
