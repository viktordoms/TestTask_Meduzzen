That start this project you need install some library. Open terminal and enter next:
- sudo apt-get install docker
- sudo apt-get install docker-compose

When you download application in your computer - need rename file 'env.example' to '.env':
    - in terminal /Test_MeduzZen  enter 'mv env.example .env'

in terminal /TestTask enter 'mv env.example .env'

1.Run :

1.1 in /Test_MeduzZen enter : sudo docker-compose up --build
1.2 you get error "django.db.utils.OperationalError: (2002, "Can't connect to MySQL server on 'db' ()"))" and press "CTRL+C"

1.3 when container is stopping enter "sudo docker-compose up --build"

1.3.1 if you get previous error or another make next: in /Test_MeduzZen enter 'sudo chmod -R 0777 *' and get started from point "1.1"

Next you want to make new migrations :
1. In wew terminal window enter: sudo docker-compose exec web bash
2. Enter : flask db migrate
2.1 If you get error about database - restart docker-container and go from point 1.
3. Enter : flask db upgrade

If you want start test - you need enter next:
1. In wew terminal window enter: sudo docker-compose exec web bash
2.Enter pytest -s -v tests/test_api.py




