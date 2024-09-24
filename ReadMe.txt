# Related to provided postman collection;
# Some of the aircraft fields named as airlines so I changed them.
# I also porceeded with POST requests for deletions as it showed in the postman collection. 

#For running this project;

activate a virtual enviroment

# for the required libaries and frameworks
pip install -r requirements.txt

# Create a new user for the testing
python manage.py shell
from django.contrib.auth.models import User

# Create a new user this is the data provided in the postman for testing
user = User.objects.create_user(username='user', password='1234')

# Save the user and exit
user.save()
exit()

#after exiting the shell run server

python manage.py runserver 8000 #prefered local port

#if the server gives error because of the slashes in the end of urls, please check if the settings.py includes 'APPEND_SLASH = False' field if it doesn't then add it to the settings.py, it should work correctly