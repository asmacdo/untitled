from django.db import models


class Person(models.Model):
    person_last_name = models.CharField(max_length=50)
    person_first_name = models.CharField(max_length=50)
    person_birth_date = models.DateField('birth date')

    def __str__(self):
        return "{ln}, {fn}".format(
            ln=self.person_last_name, fn=self.person_first_name
        )

class Work(models.Model):
    work_name = models.CharField(max_length=100)

    def __str__(self):
        return self.work_name


class Relationship(models.Model):
    rel_name = models.CharField(max_length=100)
    person = models.ForeignKey(Person)
    work = models.ForeignKey(Work)

    def __str__(self):
        return "{person} -> {work}".format(
            person=self.person.person_last_name, work=self.work.work_name
        )