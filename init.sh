sudo mkdir /home/box/logs
sudo touch /home/box/logs/errors.log
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/hello.py       /etc/gunicorn.d/hello.py
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
#sudo mysql -uroot -e "create datbase db_ask"
git config --global user.email "ershovme@gmail.com"
git config --global user.name "mikershov94"
