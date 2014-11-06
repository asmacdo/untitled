from django.db import models


class Person(models.Model):
    #Substitute for artist
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    # Blob from Wikipedia or something. NOT scratchpad!!
    info = models.CharField(max_length=400)

    def __str__(self):
        return "{fn} {ln}".format(
            ln=self.last_name, fn=self.first_name
        )
    
    def __short_str(self):
        return self.last_name


class PeopleGroup(models.Model):
    #Substitute for ensemble
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def __short_str(self):
        return self.name


class Publisher(models.Model):
    #Substitute for label
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def __short_str(self):
        return self.name


class WorkCollection(models.Model):
    # Substitute for Album
    publish_date = models.DateField()
    name = models.CharField(max_length=100)

    # Sub-collection?
    parent = models.ForeignKey('self', null=True, blank=True)

    def __str__(self):
        return "{name}({year})".format(name=self.name, year=self.publish_date.year)

    def __short_str(self):
        return self.name
    

class SoundFormat(models.Model):
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Track(models.Model):
    # One additional thought is that a track doesn't have to map to a work, it could map to a recording or
    # performance. This is problematic though because it might be remastered, a different length, etc. I am not sure
    # at what point to consider it a different recording. I also think it would be really hard to get accurate
    # information. So as it is, the same recording on two different albums would only be  related as much as two
    # different recordings by the same artists. I don't like that, but I have to draw the line somewhere.

    # TODO How long can filenames be?
    # TODO, actually, revisit all charfield lengths...
    filename = models.CharField(max_length=300)
    length = models.IntegerField('Length')
    id = models.IntegerField(unique=True, db_index=True)
    work = models.ForeignKey(Work)
    format = models.ForeignKey(SoundFormat)
    number = models.IntegerField()

    def __str__(self):
        return self.filename
    
    def __short_str(self):
        # TODO make short
        return self.filename


class Work(models.Model):
    name = models.CharField('Work Name', max_length=100)
    type = models.CharField('Work Type', max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True)
    # Many other fields are possible as backrefs to relationships

    def __str__(self):
        return self.work_name

    def __short_str(self):
        return self.name


class RoleType(models.Model):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role


class Relationship(models.Model):
    role = models.ForeignKey(RoleType, default=None)

    # TODO one and only one of this group
    person = models.ForeignKey(Person)
    people_group = models.ForeignKey(PeopleGroup)
    publisher = models.ForeignKey(Publisher)

    # TODO one and only one of this group
    work = models.ForeignKey(Work, null=True, blank=True)
    work_collection = models.ForeignKey(WorkCollection, null=True, blank=True)
    track = models.ForeignKey(Track, null=True, blank=True)

    # If this relationship has an id number, ie publisher -> work_collection
    outside_relationship_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        people = self.person or self.people_group or self.publisher
        entity = self.work or self.work_collection or self.track
        return "{people} -> {entity}".format(people=people.__short_str(), entity=entity.__short_str())
