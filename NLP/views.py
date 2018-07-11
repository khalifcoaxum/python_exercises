# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import User



# Create your views here.


user = User.objects.all()

def user_data (request):
	return render(request, 'NLP/user_data.html', {'user': user})

def save_user_data (request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.isValid():
			user = form.save(commit=False)
			content = form.cleaned_data['first_name']
			user.first_name = request.first_name
			user.last_name = request.last_name
			user.date_of_birth = request.date_of_birth
			user.age = request.age
			user.title = request.title
			user.save()
			return redirect('/')
		else:
			form = UserForm()
			return render(request, 'NLP/user_data.html',{'form': form})