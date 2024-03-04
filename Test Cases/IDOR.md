****
# Insecure Direct Object Reference
- Find and Replace `IDs` in urls, headers and body: `/users/01` -> `/users/02`
- Try Parameter Pollution `users=01` -> `users=01&users=02`
- Special Characters `/users/01*` or `/users/*` -> Disclosure of every single user
- Try older versions of API endpoints `/api/v3/users/01` -> `/api/v1/users/02`
- Add extension: `/users/01` -> `/users/02.json`
- Change Request Methods: `POST /users/01` -> `GET, PUT, PATCH, DELETE` etc.
- Check if refer or some other Headers are used to validate the IDs:
	`GET /users/01`                                   ->         `403 Forbidden`
	`Referer: example.com/users/01`
	`GET /users/02`                                  ->          `200 OK`
	`Referer: example.com/users/02`
- Encrypted IDs: if the application using encrypted IDs, try to decrypt using hashed.com or other tools.
- Swap GUID with Numeric ID or email:
	`/user/1b04c196-89f4-426a-b18b-ed85924ce283` -> `/users/02` or `/users/a@b.com`
- Try GUID such as 
	`00000000-0000-0000-0000-000000000000` and `11111111-1111-1111-1111-111111111111`
- GUID Enumeration: Try to disclose GUIDs Using `Google dorks`, `Github`, `Wayback`, `Burp History`
- if none of the GUID Enumeration methods work then try: `SignUp`, `Reset Password`, `Other endpoints` within application and analyze response. These endpoints mostly disclose user's GUID.
- 403/401 Bypass: if server responds back with 403/401 then try to use burp intruder and send 50-100 request having different IDs: Example from `/users/01` to `/users/100`
- If server responds with a 403/401, double check the function within the application. Sometime 403/401 is thrown but the action is performed.
- Blind IDORs: sometimes information is not directly disclosed. Lookout for endpoints and features that may disclose information such as export files, emails or message alerts.
- Chain IDOR with XSS for Account Takeover.

---

When you come across an `IDOR` that requires `UUID` such as:
```http
DELETE /v1/api_tokens/3fa85f64-5717-4562-b3fc-2c963f66afa6 HTTP/2
Host: api.site.com
Cookie:
```
If you are unable to find the `UUID` anywhere, try to find endpoints which disclose the `UUID` within the same organization.
```http
GET /v1/api_tokens/ HTTP/2
Host: api.site.com
Cookie:
```
Now check if you can access the same endpoint using a `Lower Privileged` user account. If you can, then you can exploit the `IDOR` using a `Lower Privileged` user account.   

---
Base Steps:

1. Create two accounts if possible or else enumerate users first.
2. Check if the endpoint is private or public and does it contains any kind of id param.
3. Try changing the param value to some other user see if does anything to their account.

- Image profile
- Delete account
- Information account
- VIEW & DELETE & Create api_key
- Allows to read any comment
- Change price
- Change the coin from dollar to euro
- Try decode the ID, if the ID encoded user md5,base64 etc.

```http
GET /GetUser/<code> HTTP/1.1
```
- Change HTTP method
```
GET /users/delete/victim_id -> 403
POST /users/delete/victim_id -> 200
```
- Try replacing parameter names
Instead of this:
```http
GET /api/albums>album_id=<album id>
```
Try this:
```http
GET /api/albums?account_id=<account id>
```
Tip: There is a Burp extension called `Paramalyzer` which will help with this by remembering all the parameter you have passed to a host.

---
