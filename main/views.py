from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from .form import ContactForm


def index(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'main/index.html',
        context=context
    )


def send_message(name, email, message):
    text = get_template('main/message.html')
    html = get_template('main/message.html')
    context = {'name': name, 'email': email, 'message': message}
    subjext = 'Сообщение от пользователя'
    from_email = 'danila.zenkovitch17@yandex.ru'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subjext, text_content, from_email, ['danila.zenkovitch17@yandex.ru'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
