#!/bin/bash
#if script fail to install please install
#md5deep,sha1dep,sha224sum,sha256deep,sha384sum,sha512sum
#and python package manually.after that open terminal at this directory
#location and run cmd
#$cp crackit.py /usr/bin/crackit



apt-get  >>/dev/null
if [ `echo $?` -eq 0 ];
  then
  arch=deb
  else
  arch=rpm
fi

if [ $arch=='deb' ]
  then
  nohup  python --version 
  if [ `echo $?` -eq 0 ]
    then
    tput setaf 6
    echo "Python package found!"
    sleep 2
    tput setaf 9
    else
    tput setaf 6
    echo "installing python...."
    apt-get install python
    tput setaf 9
  fi
  
  nohup echo we | md5deep >>/dev/null
  if [ `echo $?` -eq 0 ]
    then
    tput setaf 6
    echo "md5deep package found!"
    sleep 2
    tput setaf 9
    else
    tput setaf 6
    echo "installing md5deep....!!"
    apt-get install sha1deep
    echo "installing sha1deep....!!"
    apt-get install sha224sum
    echo "installing sha224sum....!!"
    apt-get install sha224sum
    echo "installing sha256deep....!!"
    apt-get install sha256deep
    echo "installing sha384sum....!!"
    apt-get install sha384sum
    echo "installing sha512sum....!!"
    apt-get install sha512sum
    tput setaf 9
  fi
fi
if [ $arch=='rpm' ]
  then
  nohup  python --version
  if [ `echo $?` -eq 0 ]
    then
    tput setaf 6
    echo "Python package found!"
    sleep 2
    tput setaf 9
    else
    tput setaf 6
    echo "installing python...."
    yum install python
    tput setaf 9
  fi

  nohup echo we | md5deep >>/dev/null
  if [ `echo $?` -eq 0 ]
    then
    tput setaf 6
    echo "md5deep package found!"
    sleep 2
    tput setaf 9
    else
    tput setaf 6
    echo "installing md5deep....!!"
    yum install sha1deep
    echo "installing sha1deep....!!"
    yum install sha224sum
    echo "installing sha224sum....!!"
    yum install sha224sum
    echo "installing sha256deep....!!"
    yum install sha256deep
    echo "installing sha384sum....!!"
    yum install sha384sum
    echo "installing sha512sum....!!"
    yum install sha512sum
    tput setaf 9
  fi
fi

cp crackit.py crackit
mv crackit /usr/bin/crackit
chmod +x /usr/bin/crackit
echo "Installation successful..!!"
sleep 3

  