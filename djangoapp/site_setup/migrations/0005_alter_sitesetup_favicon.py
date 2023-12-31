# Generated by Django 4.2.5 on 2023-09-13 16:01

from django.db import migrations, models
import utils.model_validatiors


class Migration(migrations.Migration):

    dependencies = [
        ('site_setup', '0004_sitesetup_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetup',
            name='favicon',
            field=models.ImageField(blank=True, default='', upload_to='assets/favicon/%Y/%m', validators=[utils.model_validatiors.validate_png]),
        ),
    ]
