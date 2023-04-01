try:
    import usocket as socket
except:
    import socket
    
import network

ssid = "daedalusone"
password = "override"
dev_hostname = "arch-light"

def config():
    host = dev_hostname
    wlan = network.WLAN(network.STA_IF)

    wlan.active(True)

    if not wlan.isconnected():
        wlan.active(True)
        # hostname has a max hostname length of 15 characters, apparently?
        if len(host) > 15:
            host = host[:15]
        network.hostname(host)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass

    print('Wifi connected as {}/{}, net={}, gw={}, dns={}'.format(
        host, *wlan.ifconfig()))
