# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-20 13:12
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0004_auto_20201115_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditionDownload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incomplete', models.BooleanField(default=True)),
                ('download_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'get_latest_by': 'download_date',
                'verbose_name': 'descarga de edici\xf3n',
                'verbose_name_plural': 'descargas de edici\xf3n',
            },
        ),
        migrations.CreateModel(
            name='OAuthState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=32, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PollAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.CharField(max_length=50, unique=True, verbose_name='documento')),
                ('answer', models.CharField(max_length=16, verbose_name='respuesta')),
            ],
        ),
        migrations.CreateModel(
            name='SentMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150, verbose_name='asunto')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='fecha de envio')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costumer_id', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='ID ss')),
                ('name', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator("^[A-Za-z0-9\xf1\xfc\xe1\xe9\xed\xf3\xfa\xd1\xdc\xc1\xc9\xcd\xd3\xda _'.\\-]*$", 'El nombre s\xf3lo admite caracteres alfanum\xe9ricos, ap\xf3strofes, espacios, guiones y puntos.')], verbose_name='nombre')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='direcci\xf3n')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='pa\xeds')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='ciudad')),
                ('province', models.CharField(blank=True, choices=[('Artigas', 'Artigas'), ('Canelones', 'Canelones'), ('Cerro Largo', 'Cerro Largo'), ('Colonia', 'Colonia'), ('Durazno', 'Durazno'), ('Flores', 'Flores'), ('Florida', 'Florida'), ('Lavalleja', 'Lavalleja'), ('Maldonado', 'Maldonado'), ('Montevideo', 'Montevideo'), ('Paysand\xfa', 'Paysand\xfa'), ('R\xedo Negro', 'R\xedo Negro'), ('Rivera', 'Rivera'), ('Rocha', 'Rocha'), ('Salto', 'Salto'), ('San Jos\xe9', 'San Jos\xe9'), ('Soriano', 'Soriano'), ('Tacuaremb\xf3', 'Tacuaremb\xf3'), ('Treinta y tres', 'Treinta y tres')], max_length=20, null=True, verbose_name='departamento')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to=b'perfiles')),
                ('document', models.CharField(blank=True, max_length=50, null=True, verbose_name='documento')),
                ('phone', models.CharField(max_length=20, verbose_name='tel\xe9fono')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de registro')),
                ('downloads', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='descargas')),
                ('pdf', models.BooleanField(default=False)),
                ('lento_pdf', models.BooleanField(default=False, verbose_name='pdf L.')),
                ('ruta', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('plan_id', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ruta_lento', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('ruta_fs', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('days', models.CharField(default=None, max_length=5, null=True)),
                ('allow_promotions', models.BooleanField(default=True, verbose_name='acepta promociones')),
                ('allow_polls', models.BooleanField(default=True, verbose_name='acepta encuestas')),
                ('subscription_mode', models.CharField(blank=True, default=None, max_length=1, null=True)),
                ('last_paid_subscription', models.DateTimeField(blank=True, null=True, verbose_name='Ultima subscripcion comienzo')),
            ],
            options={
                'verbose_name': 'suscriptor',
                'permissions': (('es_suscriptor_ladiaria', 'Es suscriptor actualmente'),),
            },
        ),
        migrations.CreateModel(
            name='SubscriberEditionDownloads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downloads', models.PositiveIntegerField(default=0, verbose_name='descargas')),
                ('edition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers_downloads', to='core.Edition', verbose_name='edici\xf3n')),
            ],
            options={
                'ordering': ('-edition', '-downloads', 'subscriber'),
                'verbose_name': 'descargas de edici\xf3n',
                'verbose_name_plural': 'descargas de ediciones',
            },
        ),
        migrations.CreateModel(
            name='SubscriberEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=150, verbose_name='descripcion')),
                ('date_occurred', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150, verbose_name='nombres')),
                ('last_name', models.CharField(max_length=150, verbose_name='apellidos')),
                ('document', models.CharField(max_length=11, null=True, verbose_name='documento')),
                ('telephone', models.CharField(max_length=20, verbose_name='tel\xe9fono')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='direcci\xf3n')),
                ('country', models.CharField(max_length=50, verbose_name='pa\xeds')),
                ('city', models.CharField(blank=True, max_length=64, null=True, verbose_name='ciudad')),
                ('province', models.CharField(blank=True, choices=[('Artigas', 'Artigas'), ('Canelones', 'Canelones'), ('Cerro Largo', 'Cerro Largo'), ('Colonia', 'Colonia'), ('Durazno', 'Durazno'), ('Flores', 'Flores'), ('Florida', 'Florida'), ('Lavalleja', 'Lavalleja'), ('Maldonado', 'Maldonado'), ('Montevideo', 'Montevideo'), ('Paysand\xfa', 'Paysand\xfa'), ('R\xedo Negro', 'R\xedo Negro'), ('Rivera', 'Rivera'), ('Rocha', 'Rocha'), ('Salto', 'Salto'), ('San Jos\xe9', 'San Jos\xe9'), ('Soriano', 'Soriano'), ('Tacuaremb\xf3', 'Tacuaremb\xf3'), ('Treinta y tres', 'Treinta y tres')], max_length=20, null=True, verbose_name='departamento')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='observaciones para la entrega')),
                ('subscription_type', models.CharField(choices=[(b'PAP', 'Edici\xf3n papel + Digital (S\xf3lo para Uruguay)'), (b'DIG', 'Digital (Edici\xf3n web)')], default=b'DIG', max_length=3, verbose_name='suscripci\xf3n')),
                ('subscription_plan', models.CharField(choices=[('MO', 'Mensual'), ('QU', 'Trimestral'), ('BA', 'Semestral'), ('AN', 'Anual')], max_length=2, verbose_name='plan')),
                ('subscription_end', models.DateTimeField(auto_now_add=True, verbose_name='\xfaltima fecha de suscripci\xf3n')),
                ('credit_card', models.CharField(blank=True, choices=[('OC', 'OCA'), ('VI', 'VISA'), ('CA', 'CABAL'), ('MA', 'MASTER')], max_length=2, null=True, verbose_name='tarjeta')),
                ('friend1_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='nombre')),
                ('friend1_email', models.CharField(blank=True, max_length=150, null=True, verbose_name='email')),
                ('friend1_telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='tel\xe9fono')),
                ('friend2_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='nombre')),
                ('friend2_email', models.CharField(blank=True, max_length=150, null=True, verbose_name='email')),
                ('friend2_telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='tel\xe9fono')),
                ('friend3_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='nombre')),
                ('friend3_email', models.CharField(blank=True, max_length=150, null=True, verbose_name='email')),
                ('friend3_telephone', models.CharField(blank=True, max_length=20, null=True, verbose_name='tel\xe9fono')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='fecha de creaci\xf3n')),
                ('public_profile', models.BooleanField(default=True, verbose_name='perf\xedl comunidad')),
                ('promo_code', models.CharField(blank=True, max_length=8, null=True)),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='suscripciones', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
            options={
                'ordering': ('-date_created', 'first_name', 'last_name'),
                'get_latest_by': 'date_created',
                'verbose_name': 'suscripci\xf3n',
                'verbose_name_plural': 'suscripciones',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_type', models.CharField(choices=[(b'DDIGM', 'Suscripci\xf3n Ilimitada'), (b'DDIGMFS', 'Suscripci\xf3n Recargada'), (b'PAPYDIM', 'Suscripci\xf3n papel'), (b'LDFS', 'la diaria fin de semana'), (b'PAPYLAS', 'la diaria lunes a s\xe1bados'), (b'LENM', 'Revista Lento')], default=b'PAPYDIM', max_length=7, unique=True, verbose_name='tipo')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio')),
                ('order', models.PositiveSmallIntegerField(null=True, verbose_name='Orden')),
                ('paypal_button_id', models.CharField(blank=True, max_length=13, null=True)),
                ('ga_sku', models.CharField(blank=True, max_length=10, null=True)),
                ('ga_name', models.CharField(blank=True, max_length=64, null=True)),
                ('ga_category', models.CharField(blank=True, choices=[(b'D', b'Digital'), (b'P', b'Papel')], max_length=1, null=True)),
                ('auth_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='Grupo asociado al permiso')),
                ('publication', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Publication')),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Precio',
                'verbose_name_plural': 'Precios',
            },
        ),
        migrations.CreateModel(
            name='UsersApiSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('udid', models.CharField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='api_sessions', to=settings.AUTH_USER_MODEL, verbose_name='usuario')),
            ],
        ),
        migrations.CreateModel(
            name='WebSubscriber',
            fields=[
                ('subscriber_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='thedaily.Subscriber')),
            ],
            bases=('thedaily.subscriber',),
        ),
        migrations.AddField(
            model_name='subscription',
            name='subscription_type_prices',
            field=models.ManyToManyField(blank=True, to='thedaily.SubscriptionPrices', verbose_name='tipo de subscripcion'),
        ),
        migrations.AddField(
            model_name='subscriberevent',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedaily.Subscriber'),
        ),
        migrations.AddField(
            model_name='subscribereditiondownloads',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='edition_downloads', to='thedaily.Subscriber', verbose_name='suscriptor'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='category_newsletters',
            field=models.ManyToManyField(blank=True, to='core.Category'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='newsletters',
            field=models.ManyToManyField(blank=True, to='core.Publication'),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subscriber', to=settings.AUTH_USER_MODEL, verbose_name='usuario'),
        ),
        migrations.AddField(
            model_name='sentmail',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='thedaily.Subscriber'),
        ),
        migrations.AddField(
            model_name='editiondownload',
            name='subscriber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriber_downloads', to='thedaily.SubscriberEditionDownloads', verbose_name='suscriptor'),
        ),
        migrations.CreateModel(
            name='ExteriorSubscription',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
            },
            bases=('thedaily.subscription',),
        ),
        migrations.AddField(
            model_name='websubscriber',
            name='referrer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='referred', to='thedaily.Subscriber', verbose_name='referido'),
        ),
        migrations.AlterUniqueTogether(
            name='subscribereditiondownloads',
            unique_together=set([('subscriber', 'edition')]),
        ),
        migrations.AlterUniqueTogether(
            name='editiondownload',
            unique_together=set([('subscriber', 'download_date')]),
        ),
    ]
