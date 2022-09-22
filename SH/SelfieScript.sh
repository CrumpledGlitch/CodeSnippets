#This script takes a picture using inbuilt webcam.

#Check if fswebcam is installed and if not, install it.
if [ ! -f /usr/bin/fswebcam ]; then
    sudo apt-get install fswebcam
fi

#Get date
DATE=`date +%Y-%m-%d_%H:%M:%S`

#Get hostname
HOSTNAME=`hostname`

#Get picture
fswebcam -r 1280x720 --no-banner /home/$USER/Pictures/$HOSTNAME-$DATE.jpg

#Echo picture
echo /home/$USER/Pictures/$HOSTNAME-$DATE.jpg

