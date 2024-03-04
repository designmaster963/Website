from django.shortcuts import render, redirect
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def home(request):
    return render(request, "home.html")


def contact(request):
    return render(request, "contact.html")
def about(request):
    return render(request, "about.html")
def club(request):
    return render(request, "club.html")
def projects(request):
    return render(request, "projects.html")
def team(request):
    return render(request, "3dc.html")
def post_create(request):
    if request.method == 'POST':
        # Extract form data from POST request
        first_name = request.POST.get('first')
        last_name = request.POST.get('last-name')
        kl_mail = request.POST.get('kl-mail')
        personal_email = request.POST.get('email')
        mobile_no = request.POST.get('mob_no.')
        data = {
            'First Name': first_name,
            'Last Name': last_name,
            'KL Mail': kl_mail,
            'Personal Email': personal_email,
            'Mobile No.': mobile_no,
        }
        cred = credentials.Certificate(
            r"C:\Users\dhruv\PycharmProjects\TheDeigningSphere\thedesigningsphere\designing_sphere\key.json")
        firebase_admin.initialize_app(cred)
        db = firestore.client()

        # Store the data in Firestore
        doc_ref = db.collection('taskCollections').document()
        doc_ref.set(data)
        return redirect('http://127.0.0.1:8000/')

    else:
        return render(request, 'club.html')