***

Tricks bypass
- Some regex might be bypassed with `%0a` -> `\n`
Blacklisting Bypass
- PHP 
```
.phtm
.phtml
.phps
.pht
.php[2-5]
.shtml
.phar
```
- ASP
```
.asp
.aspx
.cer
.asa
```
- jsp
```
.jsp
.jspx
.jsw
.jsv
.jspf
```
- ColdFusion
```
.cfm
.cfml
.cfc
.dbm
```
- Using random capitalization
```
.pHp
.pHP5
.PhAr
```

**Whitelisting bypass**
```
file.jpg.php
file.php.jpg
file.php.blah123jpg
file.php%20
file.php%0d%0a.jpg
file.php.....
file.php/
file.php.\
file.php#.png
file.
.html
```

---
### Tips on bypassing 403 and 401 errors

Here's a list of tips on how to bypass 403 Forbidden and 401 Unauthorized errors:

1. **By adding headers:** X-Originating-IP, X-Remote-IP, X-Client-IP, X-Forwarded-For etc. Sometimes companies whitelist the IP for those who can access sensitive data. These header take IP address as a value and let you access the resource if the supplied IP matches with their whitelisted ones.
2. **With unicode chars:** Try inserting unicode characters to bypass the defenses. Try e.g. ½
3. **By overriding, overwriting URL with headers:** If GET /admin gives you 403 Forbidden, try to GET /accessible (any accessible endpoint) and add any of these HTTP headers:
	- X-Original-URL: /admin
	- X-Override-URL: /admin
	- X-Rewrite-URL: /admin
4. **Try different payloads:** if GET /admin gives you 403 Forbidden, try accessing:
	- /accessible/..;/admin
	- /.;/admin
	- /admin;/
	- /admin/~
	- /./admin/./
	- /admin?param
	- /%2e/admin
	- /admin#
5. **Method switching:** Change the method from GET to POST, and see if you get something
6. **Via IP, Vhost:** Access the site via its IP or Vhost to get the forbidden content.
7. **Fuzzing:** By brute forcing (fuzzing) files or directories further 
---
### Account Takeover Via Rate-Limit Bypass
In a private bug bounty program, when a password reset was initiated, users were required to enter a `six-digit numeric code` sent to their email for verification.

To prevent `brute forece` attacks, the application implemented `rate-limit` protection, restricting the number of requests users could make within a specific time frame. If this limit was surpassed, the system issued a `429 Too Many Requests` error message.

However, the rate limit protection was bypassed by admin two `X-Forwarded-For: IP` headers.
```http
POST /reset HTTP/2
Host: example.com
X-Forwarded-For: 1.1.1.1
X-Forwarded-For: 2.2.2.2
```
By replacing the IP address in the second `X-Forwarded-For` header, it came possible to bypass the `rate-limit` and try multiple code until the correct one was found.

Exploiting this vulnerability allowed for the unauthorized takeover of any account within the application.