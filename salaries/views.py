from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader, Context
from django.views.generic import View
from django.utils.text import slugify

from easy_pdf.rendering import render_to_pdf
from .models import Salary


class SendPayslip(View):
    """ send payslip to email
    """
    def get(self, *args, **kwargs):
        #payroll = get_object_or_404(Salary, **kwargs)

        pdf = render_to_pdf(
            'emails/payslip.html',
            {}
        )
        html_content = "<p>payslip is attached</p>"

        msg = EmailMultiAlternatives("Swiftkind Payroll", "payslip is attached", settings.DEFAULT_FROM_EMAIL, ['earvin@swiftkind.com'])
        msg.attach_alternative(html_content, "text/html")
        msg.attach('payslip.pdf', pdf, 'application/pdf')
        msg.send()

        return HttpResponse(status=200)


class DownloadPayslip(View):
    """ download payslip
    """
    def get(self, *args, **kwargs):
        salary = get_object_or_404(Salary, **kwargs)
        pdf = render_to_pdf('emails/payslip.html', {'salary': salary})

        filename = slugify(f"{salary.user.get_full_name()} {salary.period}")

        response = HttpResponse(pdf, content_type="application/pdf")
        response['Content-Disposition'] = f"attachment; filename=payslip_{filename}.pdf"

        return response