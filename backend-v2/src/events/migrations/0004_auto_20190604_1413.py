# Generated by Django 2.2.1 on 2019-06-04 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190604_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='action',
            field=models.CharField(choices=[('CREATED', 'Created'), ('GENERIC_UPDATE', 'Generic Update'), ('ATTRIBUTE_CHANGE_REQUESTED', 'Attribute change requested'), ('ATTRIBUTE_CHANGE_APPROVED', 'Attribute change approved'), ('ATTRIBUTE_CHANGED', 'Attribute changed'), ('ATTRIBUTE_CHANGE_REJECTED', 'Attribute change rejected'), ('COMMENTED', 'Commented'), ('OUTCOME_ADDED', 'Outcome added'), ('ENTITY_ASSIGNED', 'Entity assigned'), ('ENTITY_REMOVED', 'Entity removed')], max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='affected_attribute',
            field=models.CharField(blank=True, choices=[('STATUS', 'Status'), ('SEVERITY', 'Severity'), ('OUTCOME', 'Outcome')], max_length=50, null=True),
        ),
    ]