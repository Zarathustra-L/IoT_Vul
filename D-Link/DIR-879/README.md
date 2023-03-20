# phpcgi

phpcgi is responsible for processing requests to .php, .asp and .txt pages. Also, it checks whether a user is authorized or not. Nevertheless, if a request is crafted in a proper way, an attacker can easily bypass authorization and execute a script that returns a login and password to a router.


## Affected version

1.05A1

## Vulnerability

D-Link DIR-879 DIR879 FW105A1 is vulnerable to Authentication Bypass via phpcgi. The file is responsible for checking user authorization and processing requests to .php, .asp and .txt pages. The attack can set up the request to bypass authorization checks. The malicious request can then execute the scripts to return login credentials to the router.
![image](https://user-images.githubusercontent.com/69450502/226443549-51693ccd-aa74-48f2-92c1-5b2f22f17f2d.png)
![image](https://user-images.githubusercontent.com/69450502/226444327-071c821e-7d29-4b4b-af5f-2ac007bbf696.png)
![image](https://user-images.githubusercontent.com/69450502/226444528-5977994b-b3e8-44f4-908d-fdb627de6e15.png)


## PoC
https://github.com/Zarathustra-L/IoT_Vul/blob/main/D-Link/DIR-879/phpcgi.py
