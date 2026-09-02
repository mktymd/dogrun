from django.db import models
from django.urls import reverse


class  Profile(models.Model):
    name = models.CharField(
        verbose_name='名前', max_length=200)
    breed = models.CharField(
        verbose_name='犬種',max_length=100)
    birthday = models.DateField(
       verbose_name='誕生日' )
    personality = models.CharField(
        verbose_name='性格',max_length=200)
    allergy = models.CharField(
        verbose_name='アレルギー', max_length=200)
    memo = models.TextField(
        verbose_name='備考',blank=True)
    profile_image = models.ImageField(
        verbose_name='プロフィール画像',
        upload_to='profiles/',
        blank=True,
        null=True )
    rabies_vaccine_date = models.ImageField(
        verbose_name='狂犬病ワクチン接種済み証',
        upload_to='profiles/',
        blank=True,
        null=True )
    mixed_vaccine_date =models.ImageField(
        verbose_name='混合ワクチン接種済み証',
        upload_to='profiles/',
        blank=True,
        null=True )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('dogruns:dogruns_list',kwargs={'pk':self.pk})
    

