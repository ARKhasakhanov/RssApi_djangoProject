from django.db import models


class Message(models.Model):
    thread = models.ForeignKey('Thread', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    message_text = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'message'


class Section(models.Model):
    section_name = models.TextField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'section'


class Thread(models.Model):
    section = models.ForeignKey('Section', models.DO_NOTHING, blank=True, null=True)
    header = models.TextField()
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    tread_text = models.TextField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'thread'


class User(models.Model):
    login = models.TextField()
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'user'
