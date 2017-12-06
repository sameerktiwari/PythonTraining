import sqlalchemy
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from sqlalchemy import create_engine
from Employee import Employee
from sqlalchemy.orm import sessionmaker


# disabling csrf (cross site request forgery)
@csrf_exempt
def getLastName(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        lastName = request.POST.get('lastName')
        firstName = request.POST.get('firstName')
        # adding the values in a context variable
        context = {
            'lastName': lastName,
            'firstName': firstName,
        }

        # getting our showdata template
        template = loader.get_template('getQual.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('lastName.html')
        return HttpResponse(template.render())

# disabling csrf (cross site request forgery)
@csrf_exempt
def getFirstName(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        firstName = request.POST.get('firstName')

        # adding the values in a context variable
        context = {
            'firstName': firstName,
        }

        # getting our showdata template
        template = loader.get_template('lastName.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('firstName.html')
        return HttpResponse(template.render())

@csrf_exempt
def getQual(request):
    # if post request came
    if request.method == 'POST':
        # getting values from post
        lastName = request.POST.get('lastName')
        firstName = request.POST.get('firstName')
        qual = request.POST.get('qual')

        # adding the values in a context variable
        context = {
            'lastName': lastName,
            'firstName': firstName,
            'qual': qual,
        }
        engine = create_engine('mysql+pymysql://root:password@localhost/test')
        emp=Employee(firstName,lastName,qual)
        Session = sessionmaker(bind=engine)
        session=Session()
        session.add(emp)
        session.commit()
        # getting our showdata template
        template = loader.get_template('success.html')

        # returing the template
        return HttpResponse(template.render(context, request))
    else:
        # if post request is not true
        # returing the form template
        template = loader.get_template('qual.html')
        return HttpResponse(template.render())