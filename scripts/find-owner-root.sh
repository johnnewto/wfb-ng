#!/bin/bash

directory="/home/jn/PycharmProjects/wfb-ng/"
echo "****************************************************************************************"
echo "**** Find  root owned files in the directory:" $directory   "****"
echo "****************************************************************************************"


find $directory -user root
echo ""
echo "end"
echo "****************************************************************************************"
