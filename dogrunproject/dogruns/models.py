from django.db import models
from django.urls import reverse
from django.conf import settings


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
        ('seibu', '西部'),
        ('chubu', '中部'),
        ('tobu', '東部'),
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


    outdoor = models.BooleanField(
        verbose_name='屋外',
        default=False)
    indoor = models.BooleanField(
        verbose_name='屋内',
        default=False)
    pool = models.BooleanField(
        verbose_name='プール',
        default=False)
    private = models.BooleanField(
        verbose_name='貸切',
        default=False)
    large_dog = models.BooleanField(
        verbose_name='大型犬',
        default=False)
    agility = models.BooleanField(
        verbose_name='アジリティ',
        default=False)
    cafe = models.BooleanField(
        verbose_name='カフェ併設',
        default=False)
    shop = models.BooleanField(
        verbose_name='ショップ併設',
        default=False)
    stay = models.BooleanField(
        verbose_name='宿泊施設',
        default=False)
    bbq = models.BooleanField(
        verbose_name='BBQ',
        default=False)
    grass = models.BooleanField(
        verbose_name='天然芝',
        default=False)
    shampoo = models.BooleanField(
        verbose_name='シャンプー施設',
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
    sub_image3 = models.ImageField(
        verbose_name='サブ画像3',
        upload_to='dogruns/',
        blank=True,
        null=True)
    def __str__(self):
        return self.name
    
