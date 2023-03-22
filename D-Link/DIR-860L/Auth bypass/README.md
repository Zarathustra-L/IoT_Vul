# phpcgi

phpcgi is responsible for processing requests to .php, .asp and .txt pages. Also, it checks whether a user is authorized or not. Nevertheless, if a request is crafted in a proper way, an attacker can easily bypass authorization and execute a script that returns a login and password to a router.


## Affected version

FW2.03 B1

## Vulnerability

D-Link DIR-860L DIR860L FW2.03 B1 is vulnerable to Authentication Bypass via phpcgi. The file is responsible for checking user authorization and processing requests to .php, .asp and .txt pages. The attack can set up the request to bypass authorization checks. The malicious request can then execute the scripts to return login credentials to the router.
![image](https://user-images.githubusercontent.com/69450502/226832282-1ed580bc-b886-4a00-9c68-6e0fd0d397b9.png)
![image](https://user-images.githubusercontent.com/69450502/226832457-c35d50ba-e890-449a-a720-dcf2a2ca1053.png)


## ExP
https://github.com/Zarathustra-L/IoT_Vul/blob/main/D-Link/DIR-860L/Auth bypass/phpcgi.py
