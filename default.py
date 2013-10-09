import xbmc, time, xbmcgui, xbmcaddon

# idle time in minutes
addon = xbmcaddon.Addon(id='script.service.IdleUnsubscribe')
max_idle_time = int(addon.getSetting("max_idle_time"))
polling_time = int(addon.getSetting("polling_time"))

print("IdleUnsubscribe: Loaded from settings idletime %d, polling time %d" % (max_idle_time, polling_time))

# set the default values if not automatically loaded
if not max_idle_time: max_idle_time = 60
if not polling_time: polling_time = 5

# set a timeout time in sec for the notification
# works best when this is a modulo polling_time value
notification_duration = 30

# convert maximum idle time from minutes to seconds
# minus the notification we are showing in the end
max_idle_time = (max_idle_time * 60) - notification_duration

# do an initial sleep to let things settle first
xbmc.sleep(5000)
print("IdleUnsubscribe: Starting thread")

while True:
	# if we are playing TV content
	if (xbmc.getCondVisibility('Pvr.IsPlayingTv')):
		# reset, let's go!
		print("IdleUnsubscribe: PVR is showing a TV channel: I'm going to wait for %d sec and poll every %d sec" % (max_idle_time, polling_time))
		time_waiting = 0
		notification_time = 0

		while xbmc.getCondVisibility('Pvr.IsPlayingTv'):
			# get the current time we are being idle in seconds
			current_time_idle = xbmc.getGlobalIdleTime()

			# if the idle time has been reset during our polling_time
			if (current_time_idle < polling_time):
				print("IdleUnsubscribe: Global idle time has been reset, resetting my waiting counter" % (current_time_idle, polling_time))
				time_waiting = 0

			# if we have been waiting longer then ...
			elif (time_waiting >= max_idle_time):
				if (notification_time >= notification_duration):
					print("IdleUnsubscribe: We have waited long enough (%d >= %d), stopping playback" % (time_waiting, max_idle_time))
					xbmc.executebuiltin('PlayerControl(stop)', True)
					break
				else:
					# check if we are already presenting the notification
					if notification_time == 0:
						title = "Idle Timer"
						desc = "Press any key to avoid automatic sleep"
						icon = "special://home/addons/script.service.idleunsubscribe/icon.png"
						xbmc.executebuiltin((u"Notification(%s,%s,%i,%s)" % (title, desc, (notification_duration * 1000), icon)).encode("utf-8"))

					# set the notification time
					notification_time += polling_time

			# sleep for our polling_time
			xbmc.sleep(polling_time * 1000)
			time_waiting += polling_time

	else:
		xbmc.sleep(polling_time * 1000)
