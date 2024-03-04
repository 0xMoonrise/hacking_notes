***
**Sodan Dorks**
```
ssl.cert.subject.CN:"*.target.com" http.title:"index of/"
```

```
ssl.cert.subject.CN:"*.target.com" http.title:"gitlab"
```

```
ssl.cert.subject.CN:"*.wur.nl" http.title:"gitlab"
```

```
ssl.cert.subject.CN:"*.target.com" "230 login sucessful" port:"21"
```

```
ssl.cert.subject.CN:"*.target.com" "230 login successful" port:"21"
```

```
ssl.cert.subject.CN:"*.govin"+200 http.title:"Admin"
```

**Critical Open Redirects using Google dorks**
```
-site:target.com inurl:go
```

```
-site:target.com inurl:return_path
```

```
-site:target.com inurl:redirect
```

```
-site:target.com inurl:redirect_url
```

```
-site:target.com inurl:locationUrl
```

```
-site:target.com inurl:locationUri
```

```
-site:target.com inurl:.next
```

```
-site:target.com inurl:.dest
```

```
-site:target.com inurl:.destination
```

```
-site:target.com inurl:.continue
```

```
-site:target.com inurl:cneckout_uri
```