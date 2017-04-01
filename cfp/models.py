from django.db import models

class Proposal(models.Model):
    first_name = models.CharField(verbose_name="First Name", max_length=50)
    last_name = models.CharField(verbose_name="Last Name", max_length=50)
    category = models.IntegerField(choices=
        [(1, 'Fundamentals'),
         (2, 'Language Internals'),
         (3, 'All things Web'),
         (4, 'Dealing with Data'),
         (5, 'Security'),
         (6, 'Performant Python'),
         (7, 'Scalable Python'),
         (8, '/etc')])

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
