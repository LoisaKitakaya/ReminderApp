# ReminderApp
A Django CRUD app. Features include User Authentication, CRUD operations, Markdown Field support, Live deployment to Heroku.

[Preview live](<https://appreminderapp.herokuapp.com/> "Live View")

## Technologies
- HTML
- CSS
- Javascript
- Django/python
- Postgresql
- Bootstrap

## Local Installation
Follow these steps if you want to install ReminderApp locally.

```
git clone https://github.com/LoisaKitakaya/ReminderApp/ && cd ReminderApp/

# create and activate virtual environment
virtualenv env
source env/bin/activate

# install requirements
pip install -r requirements.txt

# run migrations to create database
python manage.py migrate

# run the app
python manage.py runserver
```

## Issues/Troubleshooting
The webapp might not be fully responsive on all devices, but should work fine on the standart desktop/laptop.

If you come across any bugs/issues with the code, feel free to open a [new issue](<https://github.com/LoisaKitakaya/ReminderApp/issues>) in the repo. If you experience technical issues, you can always do a quick Google search to see if someone has encountered a similar Django-related issue before.

## Contributing
[Pull requests](<https://github.com/LoisaKitakaya/ReminderApp/pulls>) are welcome. For major changes, please open an [issue](<https://github.com/LoisaKitakaya/ReminderApp/issues>) first to discuss what you would like to change. Make sure to run tests and migrations as appropriate.

## License
[MIT License](<https://github.com/LoisaKitakaya/ReminderApp/blob/main/LICENSE> "MIT License")
