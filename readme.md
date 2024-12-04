

#configuration de la base de donnée mysql
bd: digital_college
user: root
mdp: mysql
dossier contenant les données de la bd: ./sql_data

docker run -d  --name mysql-flask-container  -e MYSQL_ROOT_PASSWORD=mysql  -e MYSQL_DATABASE=digital_college    -v "$(pwd)\sql_data:/var/lib/mysql"   -p 3306:3306  mysql:latest   

connect to the container instance
docker exec -it mysql-flask-container  mysql -uroot -pmysql


#command to create project structure
chmod +x create_project_folder.sh

#Install dependencies for flask
pip install flask flask-sqlalchemy pymysql flask-migrate

#Install requirement.txt
python install -r requirements.txt

#Initiation des migration
set $env:FLASK_APP="run.py"
flask db init

#Effectuer les migrations
flask db migrate -m "First Migration"
#Appliquer les changements
flask db upgrade

#Remove migrations
rm -rf migrations

