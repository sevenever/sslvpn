#/bin/bash

PW=$1
CLIENT_PRI_IP=$2

printf "%*s" 16 ${PW}
socat - TUN:${CLIENT_PRI_IP},tun-name=sslvpn_client,up
