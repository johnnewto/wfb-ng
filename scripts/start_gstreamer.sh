#!/bin/bash

echo "Start gst-launch-1.0 videotestsrc"
gst-launch-1.0 -v videotestsrc ! video/x-raw,width=640,height=480,framerate=10/1 ! videoconvert ! x264enc bitrate=200 ! video/x-h264,profile=baseline ! rtph264pay ! udpsink host=127.0.0.1 port=5602   &
pid1=$!

echo "Start gst-launch-1.0 view"
gst-launch-1.0 udpsrc port=5600 caps='application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264' ! rtph264depay ! avdec_h264 ! videoconvert ! ximagesink    &
pid2=$!

echo "Start wfb-cli gs"
wfb-cli gs
pid3=$!

## Function to terminate all applications
#terminate_sigint() {
#    echo "sigint applications..."
##    kill $pid1
##    kill $pid2
#    kill $pid3
#    echo "sigint terminated."
#    exit
#}
#
## Trap SIGINT signal (Ctrl+C) to call the terminate function
#trap terminate_sigint SIGINT
#
## Monitor the background processes
#while true; do
#    sleep 1
#done