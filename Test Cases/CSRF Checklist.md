### CSRF standard 
- **Capture requests in Burp:** use Burp or a similar tool to intercept and analyze requests to identify if there is any CSRF token present.
- **Check token predictability**: Assess if the CSRF tokens used in the application are predictable or easily guessable.
- **Remove header-base tokens:** If the CSRF token is included in a header, temporarily remove it from the request and check if the request still functions correctly.
- **Manipulate token in the request body:** If the CSRF token is included in the request body as a parameter, try removing only the value of the parameter. If the request still succeeds, try removing both the parameter name and its value to see if the request remains vulnerable.
- **Same CSRF token for different accounts:** Test if the application uses the same CSRF token for multiple user accounts.
- **Replace CSRF token with a different value:** Substitute the CSRF token value with a different value of the same length to check if the application properly validate the token. 
- **Change request method:** Modify the request method from `POST` to `GET` and remove the CSRF token.
- **Append `_method` parameter for PUT/PATCH requests:** For applications using `PUT` or `PATCH` requests, attempt appending the `_method` parameter in the request body to emulate a different request method.
- **Check alternative content types:** Verify if other content types such as `application/x-www-form-urlencoded` are allowed. If they are allowed, modify the request body manually or using a tool. For example: `{"name":"Test"}` should be changed to `name=test`
- **Bypass Referer Validation:** Try bypassing Referer validation by including the following code in your CSRF proof-of-concept HTML file: `<meta name="referrer" content="never">`
- **Steal CSRF tokens using XSS or CORS:** Test if the application is vulnerable to Cross-Site Scripting or Cross-Origin Resource Sharing attacks, which can be utilized to steal CSRF tokens.
- **Bypass JSON-based CSRF protection:** If the application implements JSON-based CSRF protection, try bypassing it using methods such as sending date in plain text or exploiting Flash-based CSRF vulnerabilities

---
### CSRF Functions checklist
- Delete account
- Change email
- Change password, if old password not required
- Add new admin if you target support roles
- Change normal information first, last name etc.
- Checkbox like receive notification
- Change profile picture/delete it
- POST xss to CSRF
**CSRF Bypasses**
- Delete token and send request with blank parameter
- Delete token parameter
- Change request from POST to GET
- Change body encoding
- Replace token with random value
- Delete referee or use this line in CSRF file | `<meta name="referrer" conent="no-referrer">`
- Use another user token
- Changing one character in token, Content length bypass

