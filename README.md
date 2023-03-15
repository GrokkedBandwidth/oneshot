# Oneshot

Scapy based program to replicate aireplay-ng deauthentication attack, but only sends one deauth per count of 1 instead of 64 per count. 

## Installation Guide
```
git clone https://github.com/GrokkedBandwidth/oneshot.git
cd oneshot/
chmod u+x configure.sh
./configure.sh
```
## Help
```
usage: OneShot [-h] [-0 COUNT] -a BSSID -c CLIENT [-r REASON] --channel
               CHANNEL
               interface

A Python based deauthentication constructor that allows full control of frames
sent and reason why. Behaves similar to aireplay-ng but allows a user to send
1 deauthentication frame as opposed to 64 per count of 1.

positional arguments:
  interface             Sets the interface to send the deauthentication frame.
                        Interface will be put in monitor mode. Required

options:
  -h, --help            show this help message and exit
  -0 COUNT, --count COUNT
                        Sets the number of frames to be sent. A value of 0
                        will make oneshot continuously senddeauthentication
                        frames. Default value is 1
  -a BSSID, --bssid BSSID
                        Sets the target BSSID of the deauthentication frame.
                        Required
  -c CLIENT, --client CLIENT
                        Sets the target client of the deauthentication frame.
                        Required
  -r REASON, --reason REASON
                        Sets the reason code of the deauthentication frame.
                        Default value is 7: Class 3 frame received from
                        nonassociated STA
  --channel CHANNEL     Sets the channel for the deauthentication frame to be
                        sent on. Required

```
