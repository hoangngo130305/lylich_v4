from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_officerpermission_delete_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
            ],
            options={
                'verbose_name': 'Cán bộ Đảng',
                'verbose_name_plural': 'Quản lý Cán bộ Đảng',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('accounts.user',),
        ),
    ]
