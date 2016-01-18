#!/bin/sh
ptables -A FORWARD -i em1 -o em3 -j ACCEPT   #em1是转发网口   em3是连接互联网的网口
iptables -A FORWARD -i em3  -o em1  -m state --state ESTABLISHED,RELATED  -j ACCEPT
iptables -t nat -A POSTROUTING -o em3  -j MASQUERADE
