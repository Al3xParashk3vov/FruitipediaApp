from django.shortcuts import render

# class ProfileCreateView():
#     pass

def create_profile(request):
    return render(request, template_name='profile/create-profile.html')