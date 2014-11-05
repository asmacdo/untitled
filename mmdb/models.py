from django.db import models


class Person(models.Model):
    person_first_name = models.CharField('First Name', max_length=50)
    person_last_name = models.CharField('Last Name', max_length=50)
    person_birth_date = models.DateField('birth date')

    def __str__(self):
        return "{ln}, {fn}".format(
            ln=self.person_last_name, fn=self.person_first_name
        )


class Work(models.Model):
    work_name = models.CharField('Work Name', max_length=100)
    work_type = models.CharField('Work Type', max_length=100)
    work_parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return self.work_name


class Relationship(models.Model):
    rel_name = models.CharField('Relationship', max_length=100)
    person = models.ForeignKey(Person)
    work = models.ForeignKey(Work)

    def __str__(self):
        return "{person} -> {work}".format(
            person=self.person.person_last_name, work=self.work.work_name
        )
