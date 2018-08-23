#!/bin/bash

TOKEN_URL=""
API_URL=""
CLIENTID=""
CLIENTSECRET=""
SCOPE=""

echo -n "Login : "
read -s USERNAME
echo -e "\n"

echo -n "Mot de passe de $USERNAME : "
read -s PASSWORD
echo -e "\n"

grant_type='password'
OUTPUT=`curl -q -s -X POST -d "grant_type=$grant_type&client_id=$CLIENTID&client_secret=$CLIENTSECRET&scope=$SCOPE&username=$USERNAME&password=$PASSWORD&redirect_uri=$REDIRECT_URI" $TOKEN_URL`

SCOPE=`echo $OUTPUT | cut -d'"' -f4`
REFRESTOKEN=`echo $OUTPUT | cut -d'"' -f14`
ACCESSTOKEN=`echo $OUTPUT | cut -d'"' -f18`

echo -e "Les valeurs obtenues:\n\t- SCOPE\t\t: $SCOPE \n\t- ACCESSTOKEN\t: $ACCESSTOKEN\n"

grant_type='tokeninfo'
curl "$API_URL&access_token=$ACCESSTOKEN"

echo -e "\n"
