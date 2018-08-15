from django.http import JsonResponse     # HttpResponse的子类
from django.shortcuts import render

# Create your views here
from emailapp.models import Email


def goemail(req):
    return render(req,'email.html')

def get_emails(request, state_code):
    email_queryset = Email.objects.filter(state=state_code)  # 根据传递的状态参数，获取相应的邮件
    email_list = []
    for email in email_queryset:
        email_dict = {}
        email_dict['id'] = email.id
        email_dict['title'] = email.title
        email_dict['content'] = email.content
        email_dict['sender'] = email.sender
        email_list.append(email_dict)
    return JsonResponse({'emails': email_list})   # 字典传递到js为一个数组，js没有字典


