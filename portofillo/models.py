import ssl
from django.db import models

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=255,verbose_name="slider-title")
    image = models.ImageField(verbose_name="image")

    def __str__(self):
        return self.title

    
class Sayac(models.Model):
    project_sayac = models.IntegerField(default=0)
    musteri_sayac = models.IntegerField(default=0)
    referans_sayac = models.IntegerField(default=0)
    uzman_sayac = models.IntegerField(default=0)

    def __str__(self):
        self.count = "Sayac"
        return self.count


class Hizmetlerimiz(models.Model):
    main_hizmetler_title = models.CharField(max_length=255,verbose_name="main-hizmetler-title")
    hizmeler_bir = models.CharField(max_length=255)
    hizmetler_bir_aciklama = models.TextField(verbose_name="hizmetler_bir_aciklama")

    hizmeler_iki = models.CharField(max_length=255)
    hizmetler_iki_aciklama = models.TextField(verbose_name="hizmetler_iki_aciklama")

    hizmeler_uc= models.CharField(max_length=255)
    hizmetler_uc_aciklama = models.TextField(verbose_name="hizmetler_uc_aciklama")

    hizmeler_dort = models.CharField(max_length=255)
    hizmetler_dort_aciklama = models.TextField(verbose_name="hizmetler_dort_aciklama")

    def __str__(self):

        return self.main_hizmetler_title


class Hizmetlermiz_details(models.Model):
    hizmetlerimiz_detail_bir = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_bir = models.TextField(verbose_name="hizmetlerminiz_bir_text")

    hizmetlerimiz_detail_iki = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_iki = models.TextField(verbose_name="hizmetlerminiz_iki_text")

    hizmetlerimiz_detail_uc = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_uc = models.TextField(verbose_name="hizmetlerminiz_uc_text")

    hizmetlerimiz_detail_dort = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_dort = models.TextField(verbose_name="hizmetlerminiz_dort_text")

    hizmetlerimiz_detail_bes = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_bes = models.TextField(verbose_name="hizmetlerminiz_bes_text")

    hizmetlerimiz_detail_altı = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_altı = models.TextField(verbose_name="hizmetlerminiz_altı_text")

        
    def __str__(self):
        self.hizmetler = "hizmetlerimiz_details"
        return self.hizmetler


class Kurumsal_Aciklama(models.Model):
    kurumsal_aciklama_title = models.CharField(max_length=255)

    kurumsal_acikla_text = models.TextField(verbose_name="kurumsal_aciklama_text")

    kurumsal_aciklama_bir = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_bir")

    kurumsal_aciklama_iki = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_iki")

    kurumsal_aciklama_uc = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_uc")

    kurumsal_aciklama_dort = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_dort")

    kurumsal_aciklama_bes = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_bes")

    kurumsal_aciklama_alti = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_altı")


    kurumsal_aciklama_image_uc_bes_dokuz = models.ImageField(verbose_name="image",blank=True,null=True)





    def  __str__(self):
        return self.kurumsal_aciklama_title


class Musteri_Yorumları(models.Model):

    musteri_yorumlari_bir_resim = models.ImageField(verbose_name="image",blank=True,null=True)
    musteri_yorumlari_bir_aciklama = models.TextField(verbose_name="musteri_yorumları_bir",blank=True,null=True,)
    musteri_yorumlari_bir_title = models.CharField(max_length=100)

    musteri_yorumlari_iki_resim = models.ImageField(verbose_name="image",blank=True,null=True,)
    musteri_yorumlari_iki_aciklama = models.TextField(verbose_name="musteri_yorumları_iki",blank=True,null=True,)
    musteri_yorumlari_iki_title = models.CharField(max_length=100)

    musteri_yorumlari_uc_resim = models.ImageField(verbose_name="image",blank=True,null=True,)
    musteri_yorumlari_uc_aciklama = models.TextField(verbose_name="musteri_yorumları_uc",blank=True,null=True,)
    musteri_yorumlari_uc_title = models.CharField(max_length=100)


    def __str__(self):
        self.muster = "musteri_yorum"
        return self.muster
    


class Referanslar(models.Model):
    referans_bir = models.ImageField(verbose_name="referans_image_bir",blank=True,null=True)
    referans_iki = models.ImageField(verbose_name="referans_image_iki",blank=True,null=True)
    referans_uc = models.ImageField(verbose_name="referans_image_uc",blank=True,null=True)
    referans_dort = models.ImageField(verbose_name="referans_image_dort",blank=True,null=True)
    referans_bes = models.ImageField(verbose_name="referans_image_bes",blank=True,null=True)

    def __str__(self):
        self.referans_name = "Referanslar"
        return self.referans_name
    



class SıkcaSorulanSorular(models.Model):
    SikcaSorulanSorular_bir = models.CharField(verbose_name="SıkcaSorulanSorular_bir",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_bir = models.TextField(verbose_name="SıkcaSorulanSorular_bir",blank=True,null=True)


    SikcaSorulanSorular_iki = models.CharField(verbose_name="SıkcaSorulanSorular_iki",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_iki = models.TextField(verbose_name="SıkcaSorulanSorular_iki",blank=True,null=True)


    SikcaSorulanSorular_uc = models.CharField(verbose_name="SıkcaSorulanSorular_uc",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_uc = models.TextField(verbose_name="SıkcaSorulanSorular_uc",blank=True,null=True)


    SikcaSorulanSorular_dort = models.CharField(verbose_name="SıkcaSorulanSorular_dort",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_dort = models.TextField(verbose_name="SıkcaSorulanSorular_dort",blank=True,null=True)


    SikcaSorulanSorular_bes = models.CharField(verbose_name="SıkcaSorulanSorular_bes",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_bes = models.TextField(verbose_name="SıkcaSorulanSorular_bes",blank=True,null=True)

    SikcaSorulanSorular_alti = models.CharField(verbose_name="SıkcaSorulanSorular_alti",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_alti = models.TextField(verbose_name="SıkcaSorulanSorular_alti",blank=True,null=True)


    def __str__(self):
        return self.SikcaSorulanSorular_bir


class Calismalar(models.Model):
    calismalar_title_bir = models.CharField(max_length=255)
    calismalar_image_bir = models.ImageField(verbose_name="image_bir")
    
    calismalar_title_iki = models.CharField(max_length=255)
    calismalar_image_iki = models.ImageField(verbose_name="image_iki")
    
    calismalar_title_uc = models.CharField(max_length=255)
    calismalar_image_uc = models.ImageField(verbose_name="image_uc")

    def __str__(self):
        return self.calismalar_title_bir    


class Sosyal_Media(models.Model):
    facebook = models.URLField(verbose_name="facebook",blank=True,null=True)
    instagram = models.URLField(verbose_name="instagram",blank=True,null=True)
    twitter = models.URLField(verbose_name="twitter",blank=True,null=True)


    def __str__(self):
        return self.facebook
        

