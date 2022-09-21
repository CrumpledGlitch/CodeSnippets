#This script echos your WAN IP

#Get WAN IP
WANIP=`wget -qO- http://ipecho.net/plain`

#Echo WAN IP
echo $WANIP


#Then it will tell you your ISP

#Get ISP
ISP=`wget -qO- http://ipinfo.io/$WANIP/org`

#Echo ISP
echo $ISP

#Then it will tell you your hostname

#Get hostname
HOSTNAME=`wget -qO- http://ipinfo.io/$WANIP/hostname`

#Echo hostname
echo $HOSTNAME

#Then it will tell you your city

#Get city
CITY=`wget -qO- http://ipinfo.io/$WANIP/city`

#Echo city
echo $CITY

#Then it will tell you your region

#Get region
REGION=`wget -qO- http://ipinfo.io/$WANIP/region`

#Echo region
echo $REGION

#Then it will tell you your country

#Get country
COUNTRY=`wget -qO- http://ipinfo.io/$WANIP/country`

#Echo country
echo $COUNTRY

#Then it will tell you your loc

#Get loc
LOC=`wget -qO- http://ipinfo.io/$WANIP/loc`

#Echo loc

echo $LOC


