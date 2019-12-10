from django.urls import path
from .views import SendPayslip, DownloadPayslip

from django.views.generic import TemplateView


urlpatterns = [
    path('send/<int:id>/', SendPayslip.as_view(), name="payslip_send"),
    path('download/<int:id>/', DownloadPayslip.as_view(), name="payslip_download"),
    path('template/', TemplateView.as_view(template_name="emails/payslip.html"), name="test"),
]