from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe

# Create your models here.


class Slider(models.Model):
    title = models.CharField(max_length=255,verbose_name="slider-title")
    image = models.ImageField(verbose_name="image")
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    
    
    class Meta:
        verbose_name_plural = "Sitenin En Üstü"

    def __str__(self):
        return self.title
    
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    
    def image_tag(self):
            return mark_safe(f'<img src="{self.image.url}" width="150" height="150" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
        

    
class Sayac(models.Model):
    project_sayac = models.IntegerField(default=0)
    musteri_sayac = models.IntegerField(default=0)
    referans_sayac = models.IntegerField(default=0)
    uzman_sayac = models.IntegerField(default=0)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Sayac"
        
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days

    def __str__(self):
        self.count = "Sayac"
        return self.count


class Hizmetlerimiz(models.Model):
    main_hizmetler_title = models.CharField(max_length=255,verbose_name="main-hizmetler-title")
    hizmeler_bir = models.CharField(max_length=255)
    hizmetler_bir_aciklama = RichTextField(blank=True,null=True)

    hizmeler_iki = models.CharField(max_length=255)
    hizmetler_iki_aciklama = RichTextField(blank=True,null=True)

    hizmeler_uc= models.CharField(max_length=255)
    hizmetler_uc_aciklama = RichTextField(blank=True,null=True)

    hizmeler_dort = models.CharField(max_length=255)
    hizmetler_dort_aciklama = RichTextField(blank=True,null=True)
    
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name_plural = "Hizmetlerimiz"
        
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days

    def __str__(self):

        return self.main_hizmetler_title


class Hizmetlermiz_details(models.Model):
    hizmetlerimiz_detail_bir = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_bir = RichTextField(blank=True,null=True)

    hizmetlerimiz_detail_iki = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_iki = RichTextField(blank=True,null=True)

    hizmetlerimiz_detail_uc = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_uc = RichTextField(blank=True,null=True)

    hizmetlerimiz_detail_dort = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_dort = RichTextField(blank=True,null=True)

    hizmetlerimiz_detail_bes = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_bes = RichTextField(blank=True,null=True)

    hizmetlerimiz_detail_altı = models.CharField(max_length=255)
    hizmetlerimiz_detail_aciklama_altı = RichTextField(blank=True,null=True)
    
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name = "Hizmetlerimiz Açıklama"
        verbose_name_plural = "Hizmetlerimiz Detail"
        
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    @property
    def hizmetler(self):
        name = "Hizmetlerimiz"
        return name
    
    def __str__(self):
        self.hizmetler = "Hizmet Çeşitleri"
        return self.hizmetler


class Kurumsal_Aciklama(models.Model):
    kurumsal_aciklama_title = models.CharField(max_length=255)

    kurumsal_acikla_text = RichTextField()

    kurumsal_aciklama_bir = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_bir")

    kurumsal_aciklama_iki = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_iki")

    kurumsal_aciklama_uc = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_uc")

    kurumsal_aciklama_dort = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_dort")

    kurumsal_aciklama_bes = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_bes")

    kurumsal_aciklama_alti = models.CharField(max_length=255,blank=True,null=True,verbose_name="kurumsal_aciklama_altı")

    kurumsal_aciklama_image_uc_bes_dokuz = models.ImageField(verbose_name="image",blank=True,null=True)
    
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    
    class Meta:
        verbose_name = "Kurumsal Açıklama"
        verbose_name_plural = "Kurumsal Açıklamalar"

    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days

    def image_tag(self):
            return mark_safe(f'<img src="{self.kurumsal_aciklama_image_uc_bes_dokuz.url}" width="150" height="150" />')

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    def  __str__(self):
        return self.kurumsal_aciklama_title


class Musteri_Yorumları(models.Model):

    musteri_yorumlari_bir_resim = models.ImageField(verbose_name="image",blank=True,null=True)
    musteri_yorumlari_bir_aciklama = RichTextField(blank=True,null=True)
    musteri_yorumlari_bir_title = models.CharField(max_length=100)

    musteri_yorumlari_iki_resim = models.ImageField(verbose_name="image",blank=True,null=True,)
    musteri_yorumlari_iki_aciklama = RichTextField(blank=True,null=True)
    musteri_yorumlari_iki_title = models.CharField(max_length=100)

    musteri_yorumlari_uc_resim = models.ImageField(verbose_name="image",blank=True,null=True,)
    musteri_yorumlari_uc_aciklama = RichTextField(blank=True,null=True)
    musteri_yorumlari_uc_title = models.CharField(max_length=100)
    
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)

    class Meta:
        verbose_name = "Müşteri Yorumlar"
        verbose_name_plural = "Müşteri Yorumları"
        
    def __str__(self):
        self.muster = "musteri_yorum"
        return self.muster
    


class Referanslar(models.Model):
    referans_bir = models.ImageField(verbose_name="referans_image_bir",blank=True,null=True)
    referans_iki = models.ImageField(verbose_name="referans_image_iki",blank=True,null=True)
    referans_uc = models.ImageField(verbose_name="referans_image_uc",blank=True,null=True)
    referans_dort = models.ImageField(verbose_name="referans_image_dort",blank=True,null=True)
    referans_bes = models.ImageField(verbose_name="referans_image_bes",blank=True,null=True)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name = "Referans"
        verbose_name_plural = "Referanslar"

    
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    @property
    def Referans(self):
        name = "Hizmetlerimiz"
        return name
    
    def __str__(self):
        self.referans_name = "Referanslar"
        
        return self.referans_name
    



class SıkcaSorulanSorular(models.Model):
    SikcaSorulanSorular_bir = models.CharField(verbose_name="SıkcaSorulanSorular_bir",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_bir = RichTextField(blank=True,null=True)

    SikcaSorulanSorular_iki = models.CharField(verbose_name="SıkcaSorulanSorular_iki",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_iki = RichTextField(blank=True,null=True)


    SikcaSorulanSorular_uc = models.CharField(verbose_name="SıkcaSorulanSorular_uc",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_uc = RichTextField(blank=True,null=True)


    SikcaSorulanSorular_dort = models.CharField(verbose_name="SıkcaSorulanSorular_dort",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_dort = RichTextField(blank=True,null=True)


    SikcaSorulanSorular_bes = models.CharField(verbose_name="SıkcaSorulanSorular_bes",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_bes = RichTextField(blank=True,null=True)

    SikcaSorulanSorular_alti = models.CharField(verbose_name="SıkcaSorulanSorular_alti",max_length=255,blank=True,null=True)
    SikcaSorulanSorular_text_alti = RichTextField(blank=True,null=True)

    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name = "S.S.S"
        verbose_name_plural = "Sıkca Sorulan Sorular"
    
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    @property
    def FAQ(self):
        name = "S.S.S"
        return name

    def __str__(self):
        return self.SikcaSorulanSorular_bir


class Calismalar(models.Model):
    calismalar_title_bir = models.CharField(max_length=255)
    calismalar_image_bir = models.ImageField(verbose_name="image_bir")
    
    calismalar_title_iki = models.CharField(max_length=255)
    calismalar_image_iki = models.ImageField(verbose_name="image_iki")
    
    calismalar_title_uc = models.CharField(max_length=255)
    calismalar_image_uc = models.ImageField(verbose_name="image_uc")
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name = "Çalışma"
        verbose_name_plural = "Çalışmalar"

    def __str__(self):
        return self.calismalar_title_bir    


    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    def image_tag_bir(self):
            return mark_safe(f'<img src="{self.calismalar_image_bir.url}" width="150" height="150" />')

    image_tag_bir.short_description = 'Image 1'
    image_tag_bir.allow_tags = True
    
    def image_tag_iki(self):
            return mark_safe(f'<img src="{self.calismalar_image_iki.url}" width="150" height="150" />')

    image_tag_iki.short_description = 'Image 2'
    image_tag_iki.allow_tags = True
    
    def image_tag_uc(self):
            return mark_safe(f'<img src="{self.calismalar_image_uc.url}" width="150" height="150" />')

    image_tag_uc.short_description = 'Image 3'
    image_tag_uc.allow_tags = True
    
    @property
    def calismalar(self):
        name = "Çalışmalarımız"
        return name


class Sosyal_Media(models.Model):
    facebook = models.URLField(verbose_name="facebook",blank=True,null=True)
    instagram = models.URLField(verbose_name="instagram",blank=True,null=True)
    twitter = models.URLField(verbose_name="twitter",blank=True,null=True)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    guncellenme_tarihi = models.DateTimeField(auto_now=True,blank=True,null=True)
    
    class Meta:
        verbose_name = "Sosyal Medya"
        verbose_name_plural = "Sosyal Medyalar"

    def __str__(self):
        return self.facebook
    
    
    @property
    def kac_gun_once(self):
        fark = timezone.now() - self.eklenme_tarihi
        return fark.days
    
    @property
    def SosyalMedya(self):
        name = "Sosyal Medya"
        return name
        

