from django.shortcuts import render

from .models import Slider,Sayac,Hizmetlerimiz,Hizmetlermiz_details,Kurumsal_Aciklama,Musteri_Yorumları,Referanslar,SıkcaSorulanSorular,Calismalar,Sosyal_Media


def index(request):
    slider = Slider.objects.all()
    sayac = Sayac.objects.all()
    hizmetler = Hizmetlerimiz.objects.all()
    hizmetler_details = Hizmetlermiz_details.objects.all()
    kurumsal_aciklama = Kurumsal_Aciklama.objects.all()
    musteri_yorumları = Musteri_Yorumları.objects.all()
    referanslar = Referanslar.objects.all()
    sıkca_sorulan_sorular = SıkcaSorulanSorular.objects.all()
    calismalar = Calismalar.objects.all()
    sosyal_medyalar = Sosyal_Media.objects.all()
    
    context = {
        'sliders':slider,
        'sayaclar':sayac,
        'hizmetler':hizmetler,
        'hizmetler_details':hizmetler_details,
        'kurumsal_aciklama':kurumsal_aciklama,
        'musteri_yorumları':musteri_yorumları,
        'referanslar':referanslar,
        'sikca_sorulan_sorular':sıkca_sorulan_sorular,
        'calismalar':calismalar,
        'sosyal_medyalar':sosyal_medyalar
    }
    
    return render(request,"index.html",context)


