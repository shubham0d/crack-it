#!/usr/bin/python
# crack-it -- hash cracking and creating utility
# Copyright (C) 2015 shubham dubey
#
# This package is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# found in the file COPYING that should have accompanied this file.
#
# This package is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

####this script will help you to automate the process of cracking
#hash of most of the algorithm and even help in creating hash from
#any desired word.
#the script use most of the pre-installed utility to find the correct
#hash value and use dictonary attack to find the correct match.
###it is well tested in kali linux and will also easily work in other
#distribution also with some minimal installation.
#this is the starting phase of the development so if you find any bug
#please help us in improving it.



import commands
import os
def banner():
  
  os.system("tput setaf 2")
  print """
        .----.				       ___   __
        |    | .----. .----. .----. .--.      |   | |  |_
	| |--- |   _| | o  | |  __| |  |// __ |.  | |   _|
	| |--- |__|   |____|\|____| |__|\     |:  | |____|
	|____|				      |::.|
	       the-ultimate hash cracker v1.0 `---'
	       creator:"$hubh4m dubey"
	       contact/mail_at_sdubey504@gmail.com
	"""
  os.system("tput setaf 5")


while True:
  os.system("clear")
  os.system("tput setaf 2")
  print """
        .----.				       ___   __
        |    | .----. .----. .----. .--.      |   | |  |_
	| |--- |   _| | o  | |  __| |  |// __ |.  | |   _|
	| |--- |__|   |____|\|____| |__|\     |:  | |____|
	|____|				      |::.|
	       the-ultimate hash cracker v1.0 `---'
	       creator:"$hubh4m dubey"
	       contact/mail_at_sdubey504@gmail.com
  """
  os.system("tput setaf 5")
  print "Press 1:To create a hash value"
  print "Press 2:To crack a hash value"
  print "Press 3:To crack a shadow file hash(pwd+salt)"
  print "Press 4:To exit the program"
  i=raw_input("Please enter your choice:")

  flag=1
  #creating hash from word
  if int(i)==1:
    
    while flag==1:
      os.system("clear")
      banner()
      #word
      word=raw_input("Enter the word to create hash:")
      #type of hash algo to use
      htype=raw_input("""Enter the algorithm to use
      (avaliable blowfish,md5,sha1,sha224,,sha256,sha512):""")
      #salt value to add
      saltv=raw_input("Enter the salt value (left blank if want hash without salt:")
      #if want hash without salt value
      if len(saltv)==0:
	
	if htype=='md5':
	  import crypt
	  hash_v=commands.getoutput("echo "+word+" |md5deep")
	  os.system("tput setaf 6")

	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break

	if htype=='sha1':
	  import crypt
	  hash_v=commands.getoutput("echo "+word+" |sha1deep")
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break

	if htype=='sha224':
	  hash_v=commands.getoutput("echo "+word+" |sha224sum |cut -d' ' -f1")#cut delete the xtra letters
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break
	  
	if htype=='sha256':
	  hash_v=commands.getoutput("echo "+word+" |sha256deep")
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break

	if htype=='sha384':
	  hash_v=commands.getoutput("echo "+word+" |sha384sum |cut -d' ' -f1")
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break

	if htype=='sha512':
	  hash_v=commands.getoutput("echo "+word+" |sha512sum |cut -d' ' -f1")
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue--------->>>>>>")
	  flag=0
	  break

	else:
	  print("Please enter the correct hash format")
	  raw_input("Press enter to try again---->>>>>>>>>")
	  #flag rerun this while loop because wrong value is inputed
	  flag=1

	  
      #with salt value
      elif len(saltv)>0:

	if htype=='blowfish':
	  import crypt
	  hash_v=crypt.crypt(word,"$2a$"+saltv)#2a for using blowfish algo
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue------------->>>>>>>>")
	  flag=0
	  break
	  
	if htype=='md5':
	  import crypt
	  hash_v=crypt.crypt(word,"$1$"+saltv)#1 for using md5 algo
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue------------->>>>>>>>")
	  flag=0
	  break


	if htype=='sha256':
	  import crypt
	  hash_v=crypt.crypt(word,"$5$"+saltv)#5 for using sha256 algo
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue------------->>>>>>>>")
	  flag=0
	  break

	if htype=='sha512':
	  import crypt
	  hash_v=crypt.crypt(word,"$6$"+saltv)#6 for using sha512 algo
	  os.system("tput setaf 6")
	  
	  print hash_v
	  print
	  os.system("tput setaf 5")
	  raw_input("Press enter to continue------------->>>>>>>>")
	  flag=0
	  break

	else:
	  print("Please enter the correct hash format")
	  raw_input("Press enter to try again-------->>>>>>>>>>>>")
	  #flag rerun this while loop because wrong value is inputed
	  flag=1


  if int(i)==2:
    while True:
      os.system("clear")
      banner()
      
      hash_value=raw_input("Enter the hash value to crack(or 0 to go back):")
      if hash_value=='0':
	break
      #path of the dictonary file
      path=raw_input("Enter the full path of password list file:")

      #no of letters in the hash
      letters=commands.getoutput("echo "+hash_value+" |wc -c")
      #wc give one xtra letter so
      letters=int(letters)-1


      #md5 is 32 bit long
      if letters==32:
	print("md5 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  #will grep line by line word which then
	  # is converted into hash.
	  
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo '"+password+"' |md5deep ")

	  #once hash is created it will be compared by hash
	  # provided by user.@ If the hash match then
	  # then the greped hash will display and break the loop.

	  
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	    os.system("tput setaf 5")
	    
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")
	    
	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break

	  
      #sha1 is 40 bit long 
      elif letters==40:
	print("sha1 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo "+password+" |sha1deep ")
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	    os.system("tput setaf 5")
	    
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")
	  
	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break
	  
      #sha224 is 56 bit long
      elif letters==56:
	print("sha224 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo "+password+" |sha224sum |cut -d' ' -f1")
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	    os.system("tput setaf 5")
	   
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")

	    
	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break

	  
      #sha256 is 64 bit long
      elif letters==64:
	print("sha256 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo "+password+" |sha256deep ")
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	    os.system("tput setaf 5")
	   
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")

	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break

      #sha384 is 96 bit long
      elif letters==96:
	print("sha384 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo "+password+" |sha384sum |cut -d' ' -f1")
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	   
	    os.system("tput setaf 5")
	    
	    
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")

	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break
	    
      #sha512 is 128 bit long
      elif letters==128:
	print("sha512 hash cracking in progress...")
	lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
	lines=int(lines)
	for x in range(1,lines):
	  x=str(x)
	  password=commands.getoutput("sed '"+x+"q;d' "+path)
	  hashed=commands.getoutput("echo "+password+" |sha512sum |cut -d' ' -f1")
	  if hashed==hash_value:
	    print "Password match successfully:"
	    os.system("tput setaf 6")
	    print password
	    print
	    os.system("tput setaf 5")

	    
	  if x==lines:
	    print ("Password does'nt match ...Please try another password file")
	    
	  raw_input("Press enter to continue---------->>>>>>>>>>>>")
	  break

	  
      else:
	print ("Please enter the correct hash value")
	print
        raw_input("Press enter to continue------------>>>>>>>>>>>>>>>")
      

  #this will find the correct word for hashes
  #  which are combination of word + salt value(a random word)
  # this type of hash method is used in storing password in
  #  linux system in /etc/shadow file
  
  if int(i)==3:
    os.system("clear")
    banner()
    
    shash=raw_input("Please enter the hash value:")

    #these are the most common algo in which password
    # is saved in /etc/shadow file
    #to view the algo used in your system use cmd:-
    #  authconfig --test |grep hashing
    
    method=raw_input("Enter the algorithm used(supported md5,sha256,sha512):")


    #python crypt module is used to convert dictonary
    # file word into hash form but openssl can also
    #  be used but openssl only give md5 hash.
    #cmd:-openssl passwd -1 -salt Etg2Sa redhat (-1 for md5)

    
    import crypt

    if method=='md5':

      #this will cut the salt value.
      #eg:for the given hash value
      #$6$dS.2ZrK4$PphydDIE8J2gbLKodXqv1VEehhZhmNYp5iE/8mITQN9NjBBThRD
      #dS.2ZrK4 will be the salt value
      
      salt=commands.getoutput("echo '"+shash+"' |cut -d'$' -f3")
      path=raw_input("Enter the full path of password list file:")
      lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
      lines=int(lines)
      for x in range(1,lines):
	x=str(x)
	password=commands.getoutput("sed '"+x+"q;d' "+path)

	#$1$ is used to tell that md5 algo has to used
	hashed=crypt.crypt(password,"$1$"+salt)
	if hashed==shash:
	  print "Password match successfully:"
	  os.system("tput setaf 6")
	  print password
	  print
	  
	  os.system("tput setaf 5")
	  
	if x==lines:
	  print ("Password does'nt match ...Please try another password file")
	  
	raw_input("Press enter to continue---------->>>>>>>>>>")
	break


    if method=='sha256':
      salt=commands.getoutput("echo '"+shash+"' |cut -d'$' -f3")
      path=raw_input("Enter the full path of password list file:")
      lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
      lines=int(lines)
      for x in range(1,lines):
	x=str(x)
	password=commands.getoutput("sed '"+x+"q;d' "+path)

	#$5$ is used to tell that sha256 algo has to used

	hashed=crypt.crypt(password,"$5$"+salt)
	if hashed==shash:
	  print "Password match successfully:"
	  os.system("tput setaf 6")
	  print password
	  print
	  os.system("tput setaf 5")
	 
	if x==lines:
	  print ("Password does'nt match ...Please try another password file")

	raw_input("Press enter to continue------------->>>>>>>>>")
	break

    if method=='sha512':
      salt=commands.getoutput("echo '"+shash+"' |cut -d'$' -f3")
      path=raw_input("Enter the full path of password list file:")
      lines=commands.getoutput("wc -l "+path+" |cut -d' ' -f1")
      lines=int(lines)
      for x in range(1,lines):
	x=str(x)
	password=commands.getoutput("sed '"+x+"q;d' "+path)

	#$6$ is used to tell that sha512 algo has to used
	
	hashed=crypt.crypt(password,"$6$"+salt)
	if hashed==shash:
	  print "Password match successfully:"
	  os.system("tput setaf 6")
	  print password
	  print
	  os.system("tput setaf 5")
	 
	if x==lines:
	  print ("Password does'nt match ...Please try another password file")

		  
	raw_input("Press enter to continue----->>>>")
	break

	
  if int(i)==4:
    os.system("clear")
    quit()
    
raw_input("Press enter to continue:-------------->>>")
