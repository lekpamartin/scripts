#!/bin/bash

AUTH_URL=""
TOKEN_URL=""
API_URL=""
USERNAME="${1:-defaultvalue}"
CLIENTID=''
CLIENTSECRET=''
REDIRECT_URI=''
SCOPE=""

if [ "$TOKEN_URL"=="" ] || [ "$API_URL"=="" ] || [ "$CLIENTID"=="" ] || [ "$CLIENTSECRET"=="" ]; then
	echo "Some variables are unset in the script"
	exit 1
fi

echo -n "Mot de passe de $USERNAME : "
read -s PASSWORD
echo -e "\n"

grant_type='password'
OUTPUT=`curl -s -X POST -d "grant_type=$grant_type&client_id=$CLIENTID&client_secret=$CLIENTSECRET&scope=$SCOPE&username=$USERNAME&password=$PASSWORD&redirect_uri=$REDIRECT_URI" $TOKEN_URL`
#echo $OUTPUT

SCOPE=`echo $OUTPUT | cut -d'"' -f4`
ACCESSTOKEN=`echo $OUTPUT | cut -d'"' -f18`

echo -e "Les valeurs obtenues:\n\t- SCOPE\t\t: $SCOPE \n\t- ACCESSTOKEN\t: $ACCESSTOKEN\n"

grant_type='tokeninfo'
curl "$API_URL&grant_type=$grant_type&client_id=$CLIENTID&client_secret=$CLIENTSECRET&access_token=$ACCESSTOKEN&redirect_uri=$REDIRECT_URI"

echo -e "\n"
