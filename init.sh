sudo mkdir /home/box/logs
sudo touch /home/box/logs/errors.log
sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo ln -s /home/box/web/hello.py       /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/ask_gunicorn_conf.py /etc/gunicorn.d/ask_gunicorn_conf.py
sudo /etc/init.d/nginx start
sudo gunicorn -c hello.py hello:wsgi_app &
sudo gunicorn -c ask_gunicorn_conf.py ask.wsgi:application &
#sudo /etc/init.d/mysql start
#sudo mysql -uroot -e "create datbase db_ask"
git config --global user.email "ershovme@gmail.com"
git config --global user.name "mikershov94"
