from django.db import models


class Board(models.Model):
    idx = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    id = models.ForeignKey('User', models.DO_NOTHING,
                           db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board'


class User(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
