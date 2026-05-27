import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileFieldNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field_key', models.CharField(max_length=100)),
                ('note', models.TextField(blank=True)),
                ('resolved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='field_notes',
                    to='profiles.profile',
                )),
                ('reviewer', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT,
                    related_name='field_notes_authored',
                    to=settings.AUTH_USER_MODEL,
                )),
            ],
            options={
                'verbose_name': 'Nhận xét trường hồ sơ',
                'verbose_name_plural': 'Nhận xét trường hồ sơ',
                'db_table': 'profile_field_notes',
                'ordering': ['field_key'],
                'unique_together': {('profile', 'field_key')},
            },
        ),
    ]
