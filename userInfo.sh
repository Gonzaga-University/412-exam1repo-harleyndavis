#1/bin/bash

#check if username is provided
if [ ! -z $1 ]
then
	UNAME=$1
else
	echo "USAGE: script <username>"
fi

#chekc if userfolder exists
if [ ! -d /home/$UNAME ]
then
	echo "ERROR: User doesn't exist"
	exit
fi

echo "**** SIZE OF HOME ****"
du -sh /home/$UNAME
echo
echo "**** First Ten Files In Home ****"
ls /home/$UNAME | head
