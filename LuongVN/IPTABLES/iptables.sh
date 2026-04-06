#!/bin/bash

trust_host='192.168.70.0/24'
server_host='192.168.70.101'

echo 1 > /proc/sys/net/ipv4/ip_forward

/sbin/iptables -F
/sbin/iptables -t nat -F
/sbin/iptables -X

/sbin/iptables -P INPUT DROP 
/sbin/iptables -P OUTPUT ACCEPT
/sbin/iptables -P FORWARD DROP 

/sbin/iptables -A FORWARD -i eth0 -o eth1 -s $trust_host -j ACCEPT
/sbin/iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

/sbin/iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT

/sbin/iptables -A INPUT -p icmp --icmp-type echo-request -s $trust_host -d $server_host -m limit --limit 1/m --limit-burst 5 -j ACCEPT

/sbin/iptables -A INPUT -p tcp -m state --state NEW -m tcp -s $trust_host -d $server_host --dport 22 -j ACCEPT

/sbin/iptables -t nat -A POSTROUTING -o eth1 -s $trust_host -j MASQUERADE

service iptables save
systemctl restart iptables 
