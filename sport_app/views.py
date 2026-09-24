from django.shortcuts import render, get_object_or_404, redirect
from .models import Trainer, Section, Athlete, Schedule, Subscription
from .forms import (TrainerForm, SectionForm, AthleteForm,
                    ScheduleForm, SubscriptionForm)


# ---------- Главная ----------
def index(request):
    context = {
        'trainers_count': Trainer.objects.count(),
        'sections_count': Section.objects.count(),
        'athletes_count': Athlete.objects.count(),
        'schedules_count': Schedule.objects.count(),
        'subscriptions_count': Subscription.objects.count(),
    }
    return render(request, 'sport_app/index.html', context)


# ==================== TRAINER ====================
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'sport_app/trainer_list.html', {'trainers': trainers})


def trainer_detail(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    return render(request, 'sport_app/trainer_detail.html', {'trainer': trainer})


def trainer_create(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sport_app:trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'sport_app/trainer_form.html',
                  {'form': form, 'title': 'Добавить тренера'})


def trainer_update(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('sport_app:trainer_detail', pk=trainer.pk)
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'sport_app/trainer_form.html',
                  {'form': form, 'title': 'Редактировать тренера'})


def trainer_delete(request, pk):
    trainer = get_object_or_404(Trainer, pk=pk)
    if request.method == 'POST':
        trainer.delete()
        return redirect('sport_app:trainer_list')
    return render(request, 'sport_app/confirm_delete.html',
                  {'object': trainer, 'cancel_url': 'sport_app:trainer_list'})


# ==================== SECTION ====================
def section_list(request):
    sections = Section.objects.select_related('trainer').all()
    return render(request, 'sport_app/section_list.html', {'sections': sections})


def section_detail(request, pk):
    section = get_object_or_404(Section.objects.select_related('trainer'), pk=pk)
    return render(request, 'sport_app/section_detail.html', {'section': section})


def section_create(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save()
            return redirect('sport_app:section_detail', pk=section.pk)
    else:
        form = SectionForm()
    return render(request, 'sport_app/section_form.html',
                  {'form': form, 'title': 'Добавить секцию'})


def section_update(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('sport_app:section_detail', pk=section.pk)
    else:
        form = SectionForm(instance=section)
    return render(request, 'sport_app/section_form.html',
                  {'form': form, 'title': 'Редактировать секцию'})


def section_delete(request, pk):
    section = get_object_or_404(Section, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('sport_app:section_list')
    return render(request, 'sport_app/confirm_delete.html',
                  {'object': section, 'cancel_url': 'sport_app:section_list'})


# ==================== ATHLETE ====================
def athlete_list(request):
    athletes = Athlete.objects.all()
    return render(request, 'sport_app/athlete_list.html', {'athletes': athletes})


def athlete_detail(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    return render(request, 'sport_app/athlete_detail.html', {'athlete': athlete})


def athlete_create(request):
    if request.method == 'POST':
        form = AthleteForm(request.POST)
        if form.is_valid():
            athlete = form.save()
            return redirect('sport_app:athlete_detail', pk=athlete.pk)
    else:
        form = AthleteForm()
    return render(request, 'sport_app/athlete_form.html',
                  {'form': form, 'title': 'Добавить спортсмена'})


def athlete_update(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == 'POST':
        form = AthleteForm(request.POST, instance=athlete)
        if form.is_valid():
            form.save()
            return redirect('sport_app:athlete_detail', pk=athlete.pk)
    else:
        form = AthleteForm(instance=athlete)
    return render(request, 'sport_app/athlete_form.html',
                  {'form': form, 'title': 'Редактировать спортсмена'})


def athlete_delete(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == 'POST':
        athlete.delete()
        return redirect('sport_app:athlete_list')
    return render(request, 'sport_app/confirm_delete.html',
                  {'object': athlete, 'cancel_url': 'sport_app:athlete_list'})


# ==================== SCHEDULE ====================
def schedule_list(request):
    schedules = Schedule.objects.select_related('section').order_by('date', 'time')
    return render(request, 'sport_app/schedule_list.html', {'schedules': schedules})


def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule.objects.select_related('section'), pk=pk)
    return render(request, 'sport_app/schedule_detail.html', {'schedule': schedule})


def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('sport_app:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'sport_app/schedule_form.html',
                  {'form': form, 'title': 'Добавить занятие'})


def schedule_update(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('sport_app:schedule_detail', pk=schedule.pk)
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'sport_app/schedule_form.html',
                  {'form': form, 'title': 'Редактировать занятие'})


def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    if request.method == 'POST':
        schedule.delete()
        return redirect('sport_app:schedule_list')
    return render(request, 'sport_app/confirm_delete.html',
                  {'object': schedule, 'cancel_url': 'sport_app:schedule_list'})


# ==================== SUBSCRIPTION ====================
def subscription_list(request):
    subscriptions = Subscription.objects.select_related('athlete').all()
    return render(request, 'sport_app/subscription_list.html',
                  {'subscriptions': subscriptions})


def subscription_detail(request, pk):
    subscription = get_object_or_404(
        Subscription.objects.select_related('athlete'), pk=pk)
    return render(request, 'sport_app/subscription_detail.html',
                  {'subscription': subscription})


def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save()
            return redirect('sport_app:subscription_detail', pk=subscription.pk)
    else:
        form = SubscriptionForm()
    return render(request, 'sport_app/subscription_form.html',
                  {'form': form, 'title': 'Добавить абонемент'})


def subscription_update(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            return redirect('sport_app:subscription_detail', pk=subscription.pk)
    else:
        form = SubscriptionForm(instance=subscription)
    return render(request, 'sport_app/subscription_form.html',
                  {'form': form, 'title': 'Редактировать абонемент'})


def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscription, pk=pk)
    if request.method == 'POST':
        subscription.delete()
        return redirect('sport_app:subscription_list')
    return render(request, 'sport_app/confirm_delete.html',
                  {'object': subscription, 'cancel_url': 'sport_app:subscription_list'})