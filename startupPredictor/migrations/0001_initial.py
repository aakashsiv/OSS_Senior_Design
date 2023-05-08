# Generated by Django 4.1.6 on 2023-04-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Organization_Name', models.CharField(max_length=255)),
                ('Last_Funding_Amount_Currency', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Industries', models.CharField(max_length=255)),
                ('Headquarters_Location', models.CharField(max_length=255)),
                ('Description', models.TextField()),
                ('Founded_Date', models.DateField()),
                ('Estimated_Revenue_Range', models.CharField(max_length=255)),
                ('Website', models.CharField(max_length=255)),
                ('Founders', models.CharField(max_length=255)),
                ('Number_of_Funding_Rounds', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Funding_Status', models.CharField(max_length=255)),
                ('Last_Funding_Type', models.CharField(max_length=255)),
                ('Last_Equity_Funding_Amount_Currency', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Last_Equity_Funding_Type', models.CharField(max_length=255)),
                ('Total_Equity_Funding_Amount_Currency', models.DecimalField(decimal_places=2, max_digits=19)),
                ('Total_Funding_Amount_Currency', models.DecimalField(decimal_places=2, max_digits=19)),
            ],
        ),
    ]
