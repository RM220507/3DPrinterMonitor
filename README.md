3D Printer Monitor
Ryan Mitcham <ryanmitcham512@gmail.com> - 2023

The host Raspberry Pi should be running an Apache2 web server, which will display the latest photo, and provide a scroll through time

camera.py - python program that should be set up to run at boot to take photos every minute and saves in a folder (only latest is shown on the website - the others can be extracted for use in time-lapses)
index.html - takes the latest photo and displays it on the webpage
