from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0006_familymember_party_dang_bo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='relationship',
            field=models.CharField(
                choices=[
                    ('cha_ruot', 'Cha ruột'),
                    ('cha_duong', 'Cha dượng'),
                    ('me_ruot', 'Mẹ ruột'),
                    ('me_ke', 'Mẹ kế'),
                    ('anh_chi_em_ruot', 'Anh/Chị/Em ruột'),
                    ('vo_chong', 'Vợ/Chồng'),
                    ('vo_ke', 'Vợ kế'),
                    ('cha_chong_vo', 'Cha chồng/vợ'),
                    ('me_chong_vo', 'Mẹ chồng/vợ'),
                    ('ong_noi', 'Ông nội'),
                    ('ba_noi', 'Bà nội'),
                    ('ong_ngoai', 'Ông ngoại'),
                    ('ba_ngoai', 'Bà ngoại'),
                    ('anh_chi_em_chong_vo', 'Anh/Chị/Em chồng/vợ'),
                    ('ong_noi_chong_vo', 'Ông nội chồng/vợ'),
                    ('ba_noi_chong_vo', 'Bà nội chồng/vợ'),
                    ('ong_ngoai_chong_vo', 'Ông ngoại chồng/vợ'),
                    ('ba_ngoai_chong_vo', 'Bà ngoại chồng/vợ'),
                    ('con', 'Con'),
                ],
                max_length=30,
            ),
        ),
    ]
