## Задача №1: 

Используя команду cat в терминале операционной системы Linux, создать
два файла Домашние животные (заполнив файл собаками, кошками,
хомяками) и Вьючные животными заполнив файл Лошадьми, верблюдами и
ослы), а затем объединить их. Просмотреть содержимое созданного файла.
Переименовать файл, дав ему новое имя (Друзья человека).

```sh 
mkdir FinalHomeWorkPython
cd FinalHomeWorkPython
cat > home_animals
cats
dogs
hamsters
cat > pack_animals
horse
camel
donkey
cat home_animals pack_animals > animals
cat animals
mv animals human_friends
```


## Задача №2: 

Создать директорию, переместить файл туда.

```sh 
mkdir New_FinalHomeWorkPython
mv human_friends ~/New_FinalHomeWorkPython
cd New_FinalHomeWorkPython
ls -ali
```


## Задача №3: 

Подключить дополнительный репозиторий MySQL. Установить любой пакет
из этого репозитория.

```sh 
sudo wget http://dev.mysql.com/get/mysql-apt-comfig_0.8.23-1_all.deb
sudo dpkg -i mysql-apt-comfig_0.8.23-1_all.deb
sudo apt-get update
sudo apt-get install mysql-server
```

## Задача №4: 

 Установить и удалить deb-пакет с помощью dpkg.

```sh 
wget -c http://ftp.ru.debian.org/debian/pool/main/n/nginx/nginx_1.22.1-9_amd64.deb
sudo dpkg -i nginx_1.22.1-9_amd64.deb
sudo apt-get install -f
sudo dpkg -r nginx nginx-common
```
