# W902
Elia Bruno, Michael Gerber
Kamera überwachung mit einem Raspberry Pi 
## Übersicht
1. Beschreibung
2. Konfiguration
3. Test
4. Evaluation

## Description
### Required programs:
* Install [vagrant](https://www.vagrantup.com/downloads.html "Vagrant Download Link")
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads "VirtualBox Download Link")
* Install Shell [GIT](https://git-scm.com/downloads "GIT Download Link")
* Install Ubuntu Server [Ubuntu](https://www.ubuntu.com/download/server "Ubuntu Download Link")
### Network plan
![Logical Network Diagram](https://github.com/Uelimueli/Modul-300/blob/master/Netzwerkplan.png "Network Diagram")

## Configuration
### Vagrant File configuration
The whole programm configuration is only on this one file.
After you created a Folder with a from you choosen name, you have to create a vagrant file. in this file you can past the following code.
```Vagrant File

Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.define "web" do |web|
  web.vm.box = "bigdeal/lamp-server"
  web.vm.hostname = 'owncloud.local'
  web.vm.network "private_network", ip: "192.168.1.4"
  web.vm.network "forwarded_port", guest:80, host:8080, auto_correct: true
  web.vm.provider "virtualbox" do |vb|
  vb.memory = "512"
  vb.name = "WEB"
end
#Apache configuration and Owncloud installation
  web.vm.provision "shell", inline: <<-SHELL
  #Update durchführen
  sudo apt-get update
  #PHP installation
  sudo apt-get install -y php7.0-gd php7.0-json php7.0-mysql php7.0-curl \
  php7.0-intl php7.0-mcrypt php-imagick \
  php7.0-zip php7.0-xml php7.0-mbstring
  #Owncloud installation
  sudo wget https://download.owncloud.org/community/owncloud-10.0.7.tar.bz2
  sudo wget https://download.owncloud.org/community/owncloud-10.0.7.tar.bz2.md5
  sudo md5sum -c owncloud-10.0.7.tar.bz2.md5 < owncloud-10.0.7.tar.bz2
  sudo tar -xjf owncloud-10.0.7.tar.bz2  -C /var/www/html
  #Module activation
  a2enmod rewrite
  a2enmod headers
  a2enmod env
  a2enmod dir
  a2enmod mime
  #Webuser rules
  sudo chown -R www-data:www-data /var/www/html/
  #Apache Webserver neu starten
  service apache2 restart
  #Firewall activation
  ufw --force enable
  sudo ufw allow 80/tcp
  sudo ufw allow ssh

  SHELL
end
    #Database VM configuration
    config.vm.define "db" do |db|
    db.vm.box = "ubuntu/xenial64"
    db.vm.network "private_network", ip: "192.168.1.5"
    db.vm.hostname = 'db.local'
    db.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.name = "DB"
    end
    db.vm.provision "shell", inline: <<-SHELL 
      # Debug ON!
      set -o xtrace
      sudo apt-get update
      sudo apt-get -y install debconf-utils 
      sudo apt-get -y install apache2 
      sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password password admin'
      sudo debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password admin'
      sudo apt-get -y install php libapache2-mod-php php-curl php-cli php-mysql php-gd mysql-client mysql-server 
      # Admininer SQL UI 
      sudo mkdir /usr/share/adminer
      sudo wget "http://www.adminer.org/latest.php" -O /usr/share/adminer/latest.php
      sudo ln -s /usr/share/adminer/latest.php /usr/share/adminer/adminer.php
      echo "Alias /adminer.php /usr/share/adminer/adminer.php" | sudo tee /etc/apache2/conf-available/adminer.conf
      sudo a2enconf adminer.conf 
      sudo service apache2 restart

        #Firewall activation
        ufw --force enable
        sudo ufw allow 3306/tcp
        sudo ufw allow ssh
  
      #Remot Access allow
      sudo sed -i "s/.*bind-address.*/bind-address = 0.0.0.0/" /etc/mysql/mysql.conf.d/mysqld.cnf
      # mysql -u root -p
      #CREATE USER 'owncloud'@'%' IDENTIFIED BY '1234';
      #CREATE DATABASE IF NOT EXISTS owncloud;
      #GRANT ALL PRIVILEGES ON owncloud.* TO 'owncloud'@'%';
      #quit
      #sudo reboot
    SHELL
  end
end
```
After you have saved this file, you can change the directory in the shell to the folder. 
You start the Own Cloud configuration with Vagrant up.

## Test
| Step | Description                               | Does it work |
| ----:|:-----------------------------------------:| ------------:|
| 1    | Testing connection of the MySQL Database. | Yes |
| 2    |  |   $12 |
| 3    | are neat      |    $1 |

## Evaluation
The work with Vagrant, was my first touch with automatic installation and I learned a lot of new things. I have now the ability to setup new systems with a self created vagrant file.