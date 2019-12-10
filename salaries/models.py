from django.db import models
from django.contrib.auth.models import User
from .mixins import SalaryCalculator


class Salary(SalaryCalculator, models.Model):
    """ employee salary
    """
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    base_amount = models.DecimalField(max_digits=999, decimal_places=2, default=0.00)
    deductions = models.ManyToManyField('Deduction', blank=True)
    
    period = models.CharField(max_length=150, null=True, blank=True)

    date_due = models.DateField(null=True, blank=True)
    date_sent = models.DateField(null=True, blank=True)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} {self.date_due}"


class Deduction(models.Model):
    """ deductions
    """
    BENEFIT = "benefit"
    LOAN = "loan"
    TYPES = (
        (BENEFIT, "Benefit"),
        (LOAN, "Loan"),
    )
    name = models.CharField(max_length=200, null=True, blank=True)
    type = models.CharField(max_length=200, choices=TYPES, default=BENEFIT)
    breakdown = models.TextField(null=True, blank=True)
    total = models.DecimalField(max_digits=999, decimal_places=2, default=0.00)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} Total: P{self.total}"


class TimeRecord(models.Model):
    """ dtr
    """
    LATE = "late"
    ABSENT = "absent"
    TYPES = (
        (LATE, "Late"),
        (ABSENT, "absent")
    )
    salary = models.ForeignKey(Salary, null=True, on_delete=models.SET_NULL)
    amount = models.DecimalField(max_digits=999, decimal_places=2, default=0.00)
    type = models.CharField(max_length=200, choices=TYPES, default=LATE)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.salary} P{self.amount}"

