# DDWRT_WOL
Remotely Wake on Lan a device via your DD-WRT equipped router, from anywhere! Configure this python script with your DDWRT Login and network info, then run it to remotely wake your device. Works over the internet, and can WOL your device with just a quick double-click.

## Requirements
- DD-WRT installed on your router
- Telnet Enabled
- You must know the WAN IP of the router, or DDNS name
- Know the MAC Address of the device you want to wake. You may be able to find this in the DD-WRT config page.

## Configuration
- in the DDWRT_WOL.py file, add your credentials to the quoted areas, within the quotes. e.g. password = 'your_password'

## Other notes
I realize this isn't particularly secure, but it works and it's handy. If you have a suggestion on how to make it more secure, let me know!
