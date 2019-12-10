class SalaryCalculator(object):
    """
    """
    def __init__(self, *args, **kwargs):
        return super(SalaryCalculator, self).__init__(*args, **kwargs)

    @property
    def total_benefits(self):
        return sum(self.deductions.values_list('total', flat=True))

    @property
    def total_absent(self):
        record = self.timerecord_set
        return sum(record.filter(type=record.model.ABSENT).values_list('amount', flat=True))

    @property
    def total_late(self):
        record = self.timerecord_set
        return sum(record.filter(type=record.model.LATE).values_list('amount', flat=True))

    @property
    def net(self):
        return self.base_amount - (self.total_benefits + self.total_absent + self.total_late)

    @property
    def per_payperiod(self):
        return self.net / 2