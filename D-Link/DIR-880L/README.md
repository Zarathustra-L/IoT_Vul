# phpcgi

phpcgi is responsible for processing requests to .php, .asp and .txt pages. Also, it checks whether a user is authorized or not. Nevertheless, if a request is crafted in a proper way, an attacker can easily bypass authorization and execute a script that returns a login and password to a router.


## Affected version

FW1.03WW A1

## Vulnerability

D-Link DIR-880L DIR880L FW1.03WW A1 is vulnerable to Authentication Bypass via phpcgi. The file is responsible for checking user authorization and processing requests to .php, .asp and .txt pages. The attack can set up the request to bypass authorization checks. The malicious request can then execute the scripts to return login credentials to the router.
![image](https://user-images.githubusercontent.com/69450502/226825489-f33fa89e-f996-4d78-b364-d69455a0f687.png)
![image](https://user-images.githubusercontent.com/69450502/226825670-0e0bc9b2-1d4c-4aec-a72a-df10bbdb3cf4.png)


## PoC
https://github.com/Zarathustra-L/IoT_Vul/blob/main/D-Link/DIR-880L/phpcgi.py
