

#check if script is running as root, if not print "Must run as root / Sudo user"
if [ "$(id -u)" != "0" ]; then
   echo "Must run as root / Sudo user" 1>&2
   exit 1
fi


#check if espeak is installed, if not install it. Dont print anything to the console.
if [ ! -f /usr/bin/espeak ]; then
   apt-get install espeak -y > /dev/null
fi


#using espeak make the PC read out the text in the quotes. Dont print anything to the console.
espeak -ven+f3 -k5 -s150 --punct="<characters>" "Hello World" 2>/dev/null




