from django.db import models
from django.core.exceptions import ValidationError
from smart_selects.db_fields import ChainedForeignKey


class AboutService(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='AboutServices/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)
    # slug = models.SlugField(verbose_name='URL', default='category-', unique=True, db_index=True)

    class Meta:
        verbose_name = 'About Service'
        verbose_name_plural = 'About Services'
        ordering = ['id']

    def __str__(self):
        return self.title


class Slogan(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Slogan'
        verbose_name_plural = 'Slogans'
        ordering = ['id']

    def __str__(self):
        return self.title


class SloganItems(models.Model):
    slogan = models.ForeignKey(Slogan, on_delete=models.CASCADE, verbose_name='Slogan', related_name='SloganItems')
    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='SloganItems/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Slogan Item'
        verbose_name_plural = 'Slogan Items'
        ordering = ['id']

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='AboutUs/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'
        ordering = ['id']

    def __str__(self):
        return self.title


class AboutUsItems(models.Model):
    about_us = models.ForeignKey(AboutUs, on_delete=models.CASCADE, verbose_name='About', related_name='AboutUs')
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'About Us Item'
        verbose_name_plural = 'About Us Items'
        ordering = ['id']

    def __str__(self):
        return self.title


class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(verbose_name='Image', upload_to='Services/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['id']

    def __str__(self):
        return self.title


class ServicesItems(models.Model):
    services = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Services',
                                 related_name='ServicesItems')
    title = models.CharField(max_length=100, verbose_name='Title')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Service Item'
        verbose_name_plural = 'Service Items'
        ordering = ['id']

    def __str__(self):
        return self.title


class Features(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='Features/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Feature'
        verbose_name_plural = 'Features'
        ordering = ['id']

    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(verbose_name='Image', upload_to='Partners/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
        ordering = ['id']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(verbose_name='Image', upload_to='AboutServices/')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)
    # slug = models.SlugField(verbose_name='URL', default='category-', unique=True, db_index=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['id']

    def __str__(self):
        return self.title


class PhoneNumbers(models.Model):
    phonenumber = models.PositiveIntegerField(verbose_name="Phone number")
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Phone Number'
        verbose_name_plural = 'Phone Numbers'
        ordering = ['id']

    def __str__(self):
        return self.phonenumber

    # def clean(self):
    #     p = self.phonenumber
    #
    #     check = ['700', '701', '705', '707', '709',
    #              '772', '777', '775', '778', '779',
    #              '500', '503', '505', '509', '550',
    #              '555', '999', '995', '992']
    #
    #     if len(p) == 13:
    #         if p[:4] != '+996':
    #             raise ValidationError('Please enter: +996')
    #         elif p[4:7] not in check:
    #             raise ValidationError('Wrong number!')
    #     else:
    #         raise ValidationError('Please enter right number!')


class Contacts(models.Model):
    gmail = models.EmailField(max_length=100, verbose_name='Email', unique=True)
    phonenumbers = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE, verbose_name='Phone Numbers',
                                     related_name='phonenumbers')
    address = models.TextField(verbose_name='Address')
    whatsapp = models.ForeignKey(PhoneNumbers, on_delete=models.CASCADE, verbose_name='WhatsApp',
                                 related_name='whatsapp')
    active = models.BooleanField(verbose_name='Active', default=True)
    created = models.DateField(verbose_name='Date public', auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['id']

    def __str__(self):
        return self.gmail
