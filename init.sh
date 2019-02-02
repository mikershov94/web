sudo mkdir /home/box/logs
sudo touch /home/box/logs/errors.log
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/hello.py       /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask_gunicorn_conf.py /etc/gunicorn.d/ask_gunicorn_conf.py
sudo /etc/init.d/nginx start
sudo gunicorn -c hello.py hello:wsgi_app &
sudo gunicorn -c /home/box/web/etc/ask_gunicorn_conf.py ask.wsgi:application &
sudo /etc/init.d/mysql start
sudo mysql -u root -e "CREATE DATABASE db_ask"
sudo mysql -u root -e "CREATE USER ask_user@localhost IDENTIFIED BY '12345678'"
sudo mysql -u root -e "GRANT ALL PRIVILEGES ON db_ask.* TO ask_user@localhost"
sudo mysql -u root -e "FLUSH PRIVILEGES"
python /home/box/web/ask/manage.py makemigrations qa
python /home/box/web/ask/manage.py migrate
python /home/box/web/ask/manage.py createsuperuser
git config --global user.email "ershovme@gmail.com"
git config --global user.name "mikershov94"
