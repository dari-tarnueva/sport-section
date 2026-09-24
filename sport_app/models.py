from django.db import models


class Trainer(models.Model):
    full_name = models.CharField(max_length=200)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.PROTECT, related_name='sections')

    def __str__(self):
        return self.name


class Athlete(models.Model):
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.full_name


class Schedule(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.section.name} — {self.date} {self.time}'


class Subscription(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name='subscriptions')
    type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.athlete.full_name} — {self.type}'
