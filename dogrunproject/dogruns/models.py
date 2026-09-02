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
    
class DogRun(models.Model):
    AREA_CHOICES = [
        ('west', '西部'),
        ('central', '中部'),
        ('east', '東部'),
        ('izu', '伊豆'),
        ]
    created_at = models.DateField(
        verbose_name='登録日',
        auto_now_add=True)
    area = models.CharField(
        verbose_name='エリア',
        max_length=20,
        choices=AREA_CHOICES)
    name = models.CharField(
        verbose_name='施設名',
        max_length=100)
    parking = models.BooleanField(
        verbose_name='駐車場',
        default=False)
    water = models.BooleanField(
        verbose_name='水道',
        default=False)
    restroom = models.BooleanField(
        verbose_name='トイレ',
        default=False)
    shower = models.BooleanField(
        verbose_name='シャワー',
        default=False)
    roof_rest = models.BooleanField(
        verbose_name='屋根付き休憩所',
        default=False)
    address = models.CharField(
        verbose_name='住所',
        max_length=200)
    price = models.TextField(
        verbose_name='料金',
        blank=True)
    appeal = models.TextField(
        verbose_name='施設の魅力',
        blank=True)
    memo = models.TextField(
        verbose_name='備考',
        blank=True)
    official_url = models.URLField(
        verbose_name='公式サイト・SNS',
        blank=True)
    business_hours = models.TextField(
        verbose_name='営業時間',
        blank=True)
    main_image = models.ImageField(
        verbose_name='代表画像',
        upload_to='dogruns/',
        blank=True,
        null=True)
    sub_image1 = models.ImageField(
        verbose_name='サブ画像1',
        upload_to='dogruns/',
        blank=True,
        null=True)
    sub_image2 = models.ImageField(
        verbose_name='サブ画像2',
        upload_to='dogruns/',
        blank=True,
        null=True)
    def __str__(self):
        return self.name
    
    
    

    

