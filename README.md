# Project Setup Instructions

## Related to Provided Postman Collection
Some of the aircraft fields named as airlines, so I changed them. I also proceeded with POST requests for deletions as shown in the Postman collection.

## Running This Project

1. **Activate a Virtual Environment**

   Make sure to activate your virtual environment before proceeding.

2. **Install Required Libraries and Frameworks**

   Run the following command to install the necessary packages:

   ```bash
   pip install -r requirements.txt

3. **Create a new user for the testing**
   ```bash
   python manage.py shell
   from django.contrib.auth.models import User

   # Create a new user this is the data provided in the postman for testing
   user = User.objects.create_user(username='user', password='1234')

   # Save the user and exit
   user.save()
   exit()
4. **after exiting the shell run server**
   ```bash
   python manage.py runserver 8000 #prefered local port
5. **Slash Related Errors**
   if the server gives error because of the slashes in the end of urls, please check if the settings.py includes 'APPEND_SLASH = False' field if it doesn't then add it to the settings.py, it should work correctly
