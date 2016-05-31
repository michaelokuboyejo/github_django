from django.shortcuts import render, HttpResponse

import requests

# Create your views here.

def index(request):
	return HttpResponse('Hello, World!')

def test(request):
	return HttpResponse('Test View')

def another(request):
	return HttpResponse('Another View')

def profile(request):
	parsed_data = []
	if request.method == 'POST':
		username = request.POST.get('user')
		req = requests.get('https://api.github.com/users/' + username)
		jsonList = []
		jsonList.append(req.json())
		userData = {}
		for data in jsonList:
			userData['name'] = data['name']
			userData['blog'] = data['blog']
			userData['email'] = data['email']
			userData['public_gists'] = data['public_gists']
			userData['public_repos'] = data['public_repos']
			userData['avatar_url'] = data['avatar_url']
			userData['followers'] = data['followers']
			userData['following'] = data['following']
		parsed_data.append(userData)
	return render(request, 'app/profile.html' , {'data' : parsed_data})
