from django.shortcuts import render, redirect
from django.http import HttpResponse
from .pay import process_payment
from .forms import UserForm
# Create your views here.
def main(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']

            return redirect(process_payment(amount, name, email))
    return render(request, 'home.html', {'form': form})






def user_info(request):
    message = '<h1>This is the films USER_INFO page.</h1>'
    return HttpResponse(message)
    from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # remove these print statements later
    print('\n\nRequest object:', request)
    print('Request object type:', type(request), '\n\n')
    
    html_tags = '''
    <h1>This is the Home Page</h1>
    <h3>Thanks for visiting us</h3>
    <p>MVT means:</p>
    <ul>
      <li>Model</li>
      <li>View</li>
      <li>Template</li>
    </ul>'''
    
    response = HttpResponse(html_tags)
    # remove these print statements later
    print('Response object:', response)
    print('Response object type:', type(response))
    print('\n\nUser-agent info :', end='')
    print(request.META['HTTP_USER_AGENT'], '\n\n')
   
    return response