### Subdomain Brute Forcing
<%* const address = await tp.system.prompt("Set the target address"); -%>
#### subdomains top one million 5000
- [ ] Subdomain brute forcing
```bash
ffuf -w $WEB_CONENT/../DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.<%address%>" -u http://<%address%>
```
- Relevant subdomains found 
```

```
