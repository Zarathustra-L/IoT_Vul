# phpcgi

phpcgi is responsible for processing requests to .php, .asp and .txt pages. Also, it checks whether a user is authorized or not. Nevertheless, if a request is crafted in a proper way, an attacker can easily bypass authorization and execute a script that returns a login and password to a router.


## Affected version

FW1.10 A1

## Vulnerability

D-Link DIR-890L DIR890L FW1.10 A1 is vulnerable to Authentication Bypass via phpcgi. The file is responsible for checking user authorization and processing requests to .php, .asp and .txt pages. The attack can set up the request to bypass authorization checks. The malicious request can then execute the scripts to return login credentials to the router.
![image](https://user-images.githubusercontent.com/69450502/226828196-b5b10c31-edbb-4a47-8c56-2b9f5aa02956.png)
![image](https://user-images.githubusercontent.com/69450502/226828326-821af73f-e7c5-4168-9ea7-5e45301c4f5d.png)


## ExP
https://github.com/Zarathustra-L/IoT_Vul/blob/main/D-Link/DIR-890L/Auth bypass/phpcgi.py
