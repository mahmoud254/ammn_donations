Steps Of Deployment

  install required packages:

      pip install -r requirements.txt

  make migrations for DB:

      python manage.py makemigrations

  apply the migrations:

      python manage.py migrate

  start the server:

      python manage.py runserver
