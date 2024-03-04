---

---
---

**Fuzz LFI /proc/self/fd/[0-100]** 
```bash
seq 0 100 | ffuf -w - -u http://example.com/file=../../../proc/self/fd/FUZZ
```
**Fuzz virtual hosting**
```bash
ffuf -w ~/wordlists/subdomains.txt -H "Host: FUZZ.ffuf.me" -u http://ffuf.me
```
**Or with keyword**
```bash
ffuf -H "Host: FUZZ.example.me" -u http://localhost:8000/ -w $WEB_CONENT/../DNS/subdomains-top1million-5000.txt
```
**Content discovery - Recursion**
```bash
ffuf -w ~/wordlists/common.txt -recursion -u http://ffuf.me/cd/recursion/FUZZ
```
**Content Discovery - File Extensions**
```bash
ffuf -w ~/wordlists/common.txt -e .log -u http://ffuf.me/cd/ext/logs/FUZZ
```

---

**Config files**
```toml
[general]
  colors = true
[http]
    headers = [
        "X-SOC-Tag: clientXYZ-audit042",
    ]
    proxyurl = "http://127.0.0.1:8080"
    url = "http://ffuf.me/cd/basic/FUZZ"
```
*load config file with `-config file.toml`*

**Config input files**: specify a tag such as COMMON and PARAM
```toml
[input]
    wordlists = [
        "/usr/share/seclists/Discovery/Web-Content/common.txt:COMMON",
        "/usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt:PARAM",
        "/usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt:SUBDOMAINS",
        "/usr/share/seclists/Discovery/Web-Content/quickhits.txt:QUICKHITS",
        "/usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt:MEDIUMFILES",
        "/usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt:MEDIUMDIR",
        "/usr/share/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt:MEDIUMWORDS",
        "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt:DIR2.3M"
    ]
```
**Use**
```bash
ffuf -u 'http://ffuf.me/cd/param/COMMON?PARAM=1'
```

**This can be useful to find the credentials for a basic authentication**
```toml
[input]
    inputmode = "clusterbomb"
    wordlists = [
        "/usr/share/seclists/Usernames/top-usernames-shortlist.txt:USER",
        "/usr/share/seclists/Passwords/2020-200_most_used_passwords.txt:PASS"
    ]
```
**Use**
```bash
ffuf -u http://USER:PASS@ffuf.me/ -config config.toml
```

**HTTP status codes trigger a match**
```toml
[matcher]
    status = "200,204,301,302,307,401,403,405,500"
```

---
## Tools
Tools
```
https://github.com/Fuzzapi/fuzzapi
https://github.com/Fuzzapi/API-fuzzer
https://github.com/flipkart-incubator/Astra
https://github.com/BBVA/apicheck
https://github.com/ngalongc/openapi_security_scanner
https://github.com/assetnote/kiterunner
https://github.com/s0md3v/dump/tree/master/json2paths
https://github.com/API-Security/APIKit
```
API keys guesser
```
https://api-guesser.netlify.app/
```
Wordlists
```
https://github.com/chrislockard/api_wordlist
https://github.com/danielmiessler/SecLists/blob/master/Discovery/Web-Content/common-api-endpoints-mazen160.txt
https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content/api
https://github.com/fuzzdb-project/fuzzdb/blob/master/discovery/common-methods/common-methods.txt
```
Swagger to burp
```
https://rhinosecuritylabs.github.io/Swagger-EZ/
```
List swagger routes
```
https://github.com/amalmurali47/swagrouters
```
Checklist
```
https://gitlab.com/pentest-tools/API-Security-Checklist/-/blob/master/README.md
```
Best mindmap
```
https://dsopas.github.io/MindAPI/play/
```
GUID guesser
```
https://gist.github.com/DanaEpp/8c6803e542f094da5c4079622f9b4d18
```
---
## Useful links about ffuf
[ffuf advanced tricks](https://www.acceis.fr/ffuf-advanced-tricks/)
[fuff.me](http://ffuf.me/)

