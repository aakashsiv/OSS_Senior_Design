from django.db import models
'''
class Organizations(models.Model):
    organization_name = models.CharField(db_column='Organization Name', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_funding_amount_currency_in_usd_field = models.DecimalField(db_column='Last Funding Amount Currency (in USD)', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    industries = models.CharField(db_column='Industries', max_length=200, blank=True, null=True)  # Field name made lowercase.
    headquarters_location = models.CharField(db_column='Headquarters Location', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    founded_date = models.DateField(db_column='Founded Date', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    estimated_revenue_range = models.CharField(db_column='Estimated Revenue Range', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website = models.CharField(db_column='Website', max_length=200, blank=True, null=True)  # Field name made lowercase.
    founders = models.CharField(db_column='Founders', max_length=200, blank=True, null=True)  # Field name made lowercase.
    number_of_funding_rounds = models.FloatField(db_column='Number of Funding Rounds', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    funding_status = models.CharField(db_column='Funding Status', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_funding_type = models.CharField(db_column='Last Funding Type', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    last_equity_funding_amount_currency_in_usd_field = models.DecimalField(db_column='Last Equity Funding Amount Currency (in USD)', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    last_equity_funding_type = models.CharField(db_column='Last Equity Funding Type', max_length=200, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    total_equity_funding_amount_currency_in_usd_field = models.DecimalField(db_column='Total Equity Funding Amount Currency (in USD)', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    total_funding_amount_currency_in_usd_field = models.DecimalField(db_column='Total Funding Amount Currency (in USD)', max_digits=65535, decimal_places=65535, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.       
    id = models.AutoField(primary_key=True)
    roi = models.DecimalField(db_column='roi', max_digits=65535, decimal_places=65535, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'organizations'

'''
class Organizations(models.Model):
    organization_name = models.TextField(blank=True, null=True)
    last_funding_amount_currency_usd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    industries = models.TextField(blank=True, null=True)
    headquarters_location = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    founded_date = models.DateField(blank=True, null=True)
    estimated_revenue_range = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    founders = models.TextField(blank=True, null=True)
    number_of_funding_rounds = models.IntegerField(blank=True, null=True)
    funding_status = models.TextField(blank=True, null=True)
    last_funding_type = models.TextField(blank=True, null=True)
    last_equity_funding_amount_currency_usd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)   
    last_equity_funding_type = models.TextField(blank=True, null=True)
    total_equity_funding_amount_currency_usd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)  
    total_funding_amount_currency_usd = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    roi = models.DecimalField(db_column='roi', max_digits=65535, decimal_places=65535, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'organizations'
