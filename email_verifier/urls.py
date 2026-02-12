from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("verify/", views.verify_email_file, name="verify"),
    path("download/csv/", views.download_verified_emails, name="download_csv"),
    path("download/xlsx/", views.download_verified_emails_xlsx, name="download_xlsx"),
]
