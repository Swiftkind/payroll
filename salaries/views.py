from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from django.views.generic import View
from django.utils.text import slugify
from .models import Salary, TimeRecord
from weasyprint import HTML, CSS
from django.template.loader import render_to_string
from .admin import SalaryAdmin

class SendPayslip(View):
    """ send payslip to email
    """
    def get(self, *args, **kwargs):
     
        salary = get_object_or_404(Salary, **kwargs)
        time_record = TimeRecord.objects.filter(salary=salary)
        html = render_to_string('emails/payslip.html',{'salary': salary, 'time_record': time_record})
        pdf = HTML(string=html).write_pdf()

        html_content = "<p>payslip is attached</p>"

        msg = EmailMultiAlternatives("Swiftkind Payroll", "payslip is attached", settings.DEFAULT_FROM_EMAIL, ['erykestabillo@gmail.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.attach('payslip.pdf', pdf, 'application/pdf')
        msg.send()

        return HttpResponse(status=200)


class DownloadPayslip(View):
    """ download payslip
    """
    def get(self, *args, **kwargs):
        
        salary = get_object_or_404(Salary, **kwargs)
        time_record = TimeRecord.objects.filter(salary=salary)
        html = render_to_string('emails/payslip.html',{'salary': salary, 'time_record': time_record})
        pdf = HTML(string=html).write_pdf()

        filename = slugify(f"{salary.user.get_full_name()} {salary.period}")

        response = HttpResponse(pdf, content_type="application/pdf")
        response['Content-Disposition'] = f"attachment; filename=payslip_{filename}.pdf"

        return response