On server:
```
sudo socat openssl-listen:443,reuseaddr,cert=server.pem,verify=0,fork EXEC:"./server_stub.py password 192.168.88.1/24"
```

On client:
```
sudo socat openssl-connect:yourserver.domain.com:443,cafile=server.crt,verify=0 SYSTEM:"./client_stub.bash password 192.168.88.2/24"
```

server.pem and server.crt are common X.509 certificate and/or private key, refer to openssl document for how to generate them.

the 'password' and 192.168.88.1/2 can be changed to fit your network environment, for strong password and avoiding network confliction.

after above you need some iptables configuration on server to allow forward pkgs from 192.168.88.2, and do masqrade/SNAT for 192.168.88.2
on client, you need some routing config to route through 192.168.88.2

