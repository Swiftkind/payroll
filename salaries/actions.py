from django.utils import timezone


def salary_sent(modeladmin, request, queryset):
    """ update the sent date to
        the current date.
    """
    queryset.update(date_sent=timezone.now().date())

salary_sent.short_description = "Mark the salary as sent"