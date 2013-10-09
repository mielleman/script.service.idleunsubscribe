xbmc-idleubsubscribe
====================

XBMC script add-on that will auto unsubscribe from current tv channel if no activity detected for a set amount of time.

The script will present a notification before the expiry of the max_idle_time and if no action is taken (button press, remote press, mouse movement) it will stop the current activity on XBMC.

Currently some values can be adjusted through the resources/settings.xml file:
* max_idle_time (time after which playback is automatically stopped)
* polling_time (how frequently we check if XBMC is still idle)

REQUIREMENTS:
=============

* XBMC Frodo or later

INSTALLATION:
=============

To install please follow the following guide.

http://forum.xbmc.org/showthread.php?tid=123465
