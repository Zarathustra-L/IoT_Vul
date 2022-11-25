# phpcgi

phpcgi is responsible for processing requests to .php, .asp and .txt pages. Also, it checks whether a user is authorized or not. Nevertheless, if a request is crafted in a proper way, an attacker can easily bypass authorization and execute a script that returns a login and password to a router.



## Product

1. firmware download:  ftp://ftp2.dlink.com/PRODUCTS/DIR-869/REVA/

## Affected version

1.02B15

## Vulnerability

D-Link DIR-869 DIR869Ax_FW102B15 is vulnerable to Authentication Bypass via phpcgi. The file is responsible for checking user authorization and processing requests to .php, .asp and .txt pages. The attack can set up the request to bypass authorization checks. The malicious request can then execute the scripts to return login credentials to the router.

![image-20221126022613113](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20221126022613113.png)
