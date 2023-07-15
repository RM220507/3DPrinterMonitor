#3D Printer Monitor
##Ryan Mitcham - 2023

This web service is designed to be hosted by an Apache2 webserver on a Raspberry Pi. The Pi should also run the `camera.py` script, that will capture an image every 30 seconds and store it in the `/var/www/html/Images` directory, on boot. 
<br/>
Connect a Raspberry Pi Camera Module to the port on your Pi and position it with a view of your print bed. Boot the Pi up and visit `yourhostname.local` in a browser to see the resulting images.
<br/>
This project is designed for 3D printers that are not compatible with OctoPrint
