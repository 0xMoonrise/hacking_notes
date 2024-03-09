***
### Hashcat
md5 cracking
```bash
hashcat -m [mode] hashes.txt rockyou.txt
```

Most common modes used on `ctfs`

| name    | mode |
| ------- | ---- |
| md5     | 0    |
| sha1    | 100  |
| sha256  | 1400 |
| bcrypt  | 3200 |
| md4     | 900  |
| NTLM    | 1000 |
| SHA-512 | 1800 |
- You can add a salt in md5 such as: hash:salt