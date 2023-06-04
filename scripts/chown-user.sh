#!/bin/bash

directory="/home/jn/PycharmProjects/wfb-ng/"
echo "****************************************************************************************"
echo "**** Change  root owned files in the directory:" $directory   " to user jn  ****"
echo "****************************************************************************************"


chown -R jn $directory

find $directory -user root