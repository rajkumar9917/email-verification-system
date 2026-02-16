from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from celery import group
from .forms import EmailForm
from .tasks import send_email
from .utils import get_valid_emails


@login_required
def index(request):

    if request.method == "POST":
        form = EmailForm(request.POST, request.FILES)

        if form.is_valid():
            file = form.cleaned_data["file"]
            subject = form.cleaned_data["subject"]
            message_body = form.cleaned_data["message"]

            emails = get_valid_emails(file)

            if not emails:
                messages.warning(
                    request,
                    "No valid email addresses found in the uploaded CSV file."
                )
                return redirect("bulk_sender:index")

            try:
                group(
                    send_email.s(email, subject, message_body)
                    for email in emails
                ).apply_async()

                messages.success(
                    request,
                    f"{len(emails)} emails successfully sent!"
                )

            except Exception as e:
                messages.error(
                    request,
                    f"Failed to send emails. Error: {str(e)}"
                )

            return redirect("bulk_sender:index")

        else:
            messages.error(
                request,
                "Form submission failed. Please correct the errors below."
            )

    else:
        form = EmailForm()

    return render(request, "bulk_sender/index.html", {
        "form": form
    })
