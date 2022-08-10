# Generated by Django 4.1 on 2022-08-09 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rating', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='referralrelationship',
            name='invited',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited', to=settings.AUTH_USER_MODEL, verbose_name='Приглашённый'),
        ),
        migrations.AddField(
            model_name='referralrelationship',
            name='inviting',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inviter', to=settings.AUTH_USER_MODEL, verbose_name='Пригласивший'),
        ),
        migrations.AddField(
            model_name='referralrelationship',
            name='refer_token',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.referralcode', verbose_name='referral_code'),
        ),
        migrations.AddField(
            model_name='referralcode',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Code owner'),
        ),
        migrations.AddConstraint(
            model_name='referralcode',
            constraint=models.UniqueConstraint(fields=('user', 'token'), name='unique user token'),
        ),
    ]
