from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .actions import salary_sent
from .models import Salary, Deduction, TimeRecord


@admin.register(Deduction)
class DeductionAdmin(admin.ModelAdmin):
    pass


@admin.register(TimeRecord)
class TimeRecordAdmin(admin.ModelAdmin):
    pass


class TimeRecordInlineAdmin(admin.StackedInline):
    model = TimeRecord
    extra = 0


@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display = (
        'get_full_name',
        'period',
        'get_base_amount',
        'get_total_benefits',
        'get_total_dtr_deductions',
        'get_net',
        'date_due',
        'date_sent',
        'download'
    )
    filter_horizontal = ('deductions',)
    inlines = (TimeRecordInlineAdmin,)
    actions = (salary_sent,)

    def get_base_amount(self, instance):
        return f"{instance.base_amount:,}"
    get_base_amount.short_description = 'Base Amount'

    def get_full_name(self, instance):
        return f"{instance.user.get_full_name()}"
    get_full_name.admin_order_field  = 'user'
    get_full_name.short_description = 'Employee Name'

    def get_total_benefits(self, instance):
        return f"{instance.total_benefits:,}"
    get_total_benefits.short_description = "Benefits"

    def get_total_dtr_deductions(self, instance):
        return f"{instance.total_absent + instance.total_late:,}"
    get_total_dtr_deductions.short_description = "Time Record Deductions"

    def get_net(self, instance):
        return f"{instance.net:,}"
    get_net.short_description = "Net"

    def download(self, instance):
        return format_html(f"<a href='{reverse('payslip_download', args=[instance.id])}'>Download</a>")
    download.allow_tags = True