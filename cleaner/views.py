from django.shortcuts import render, redirect
from django.conf import settings
from django.core.mail import EmailMessage
import logging

logger = logging.getLogger(__name__)


def index(request):
    return render(request, 'cleaner/index.html')

def send(request):
    if request.method == 'POST':
        logger.debug('settings.EMAIL_HOST_USER={}'.format(settings.EMAIL_HOST_USER))
        name = request.POST.get("name", "")
        email = request.POST.get("email","")
        contact = request.POST.get("contact","")
        date = request.POST.get("date_time","")
        address = request.POST.get("address","")
        subject = '시연 신청(' + name + ')'
        message = '이름: ' +name + '\n' + '연락처: ' + contact + '\n' + '시연 날짜: ' + date + '\n' + '주소: ' + address + '\n' + '이메일: ' + email
        from_email = settings.EMAIL_HOST_USER
        email = EmailMessage(subject, message, from_email,[from_email])
        email.send()
        return redirect('index')
    else:
        return redirect('index')



