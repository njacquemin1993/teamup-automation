# teamup-automation
automation of teamup registration

## Login
### Address
https://goteamup.com/en-us/login/customer/?next=/dashboard/

### Html
```
<div id="cookies_enabled" style="">
    
    <form class="form-horizontal disable-on-submit" method="POST" action="/en-us/login/customer/?next=/dashboard/" id="auth_form">
        <input name="csrfmiddlewaretoken" value="i3EawD74HGcQ33ZRSqVqtDZepaL1pA0Z" type="hidden">

        <div class="form-group">
            <div class="col-sm-6 col-sm-push-2">
            <strong>Do you already have an account with teamup?</strong>
            <div class="clearfix"></div>
            <div class="controls">
                <label class="radio">
                    <input name="action" value="login" tabindex="10" data-bind-auth="checked: action" type="radio"> Yes, I already have an account
                </label>
                <label class="radio">
                    <input name="action" value="register" tabindex="11" data-bind-auth="checked: action" type="radio"> No, I do not yet have an account
                </label>
            </div>
            </div>
        </div>

        <div data-bind-auth="visible: action() == 'login' || registerAuthOption() == 'email'">
            <div class="form-group ">
                <label class="control-label col-sm-2">
                    Email Address
                </label>
                <div class="col-sm-6">
                    <input id="id_email" name="email" type="email">
                    
                </div>
            </div>
            <div class="form-group ">
                <label class="control-label col-sm-2">
                    Password
                </label>
                <div class="col-sm-6">
                    <input id="id_password" name="password" type="password">
                </div>
            </div>
        </div>
    </form>
</div>
```
### POST data
```
csrfmiddlewaretoken : ...
action: login
name : <empty>
register_auth_option: email
email: ...
password: ...(clear)
password_confirm: <empty>
fbid: <empty>
```

### POST address
https://goteamup.com/en-us/login/customer/?next=/dashboard/

### cURL command
`curl 'https://goteamup.com/en-us/login/customer/?next=/dashboard/' --2.0 -H 'Host: goteamup.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://goteamup.com/en-us/login/customer/?next=/dashboard/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: sessionid=fewsa3umh7sl8nrv8xj055ekdc8sxett; csrftoken=i3EawD74HGcQ33ZRSqVqtDZepaL1pA0Z; ajs_user_id=%22581902%22; ajs_group_id=null; ajs_anonymous_id=%22a7745ede-44d1-4817-8e2c-ed7b1a541eb4%22' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data 'csrfmiddlewaretoken=i3EawD74HGcQ33ZRSqVqtDZepaL1pA0Z&action=login&name=&register_auth_option=email&email=*****%40gmail.com&password=*********&password_confirm=&fbid='`

### Cookies response
```
HTTP/2.0 302 Found
date: Tue, 12 Dec 2017 07:41:21 GMT
content-type: text/html; charset=utf-8
server: nginx/1.4.6 (Ubuntu)
strict-transport-security: max-age=15552001
content-language: en-us
expires: Tue, 12 Dec 2017 07:41:21 GMT
vary: Cookie
last-modified: Tue, 12 Dec 2017 07:41:21 GMT
x-teamup-user: 581902-
etag: "d41d8cd98f00b204e9800998ecf8427e"
location: /dashboard/
cache-control: no-cache, no-store, must-revalidate, max-age=0
p3p: CP="IDC DSP COR ADM DEVi TAIi PSA PSD IVAi IVDi CONi HIS OUR IND CNT"
set-cookie: csrftoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU; expires=Tue, 11-Dec-2018 07:41:21 GMT; Max-Age=31449600; Path=/
sessionid=fewsa3umh7sl8nrv8xj055ekdc8sxett; expires=Tue, 26-Dec-2017 07:41:21 GMT; httponly; Max-Age=1209600; Path=/
X-Firefox-Spdy: h2
```
## Register
### Address
https://goteamup.com/p/787790-crossfit-vetroz/e/9947791-wod/

### Html
```
<div>
    <form action="/p/787790-crossfit-vetroz/e/9947791-wod/register/" method="POST" style="margin-bottom:0">
      <input name="csrfmiddlewaretoken" value="fWBQhSntDu7NUVKDwr61yBm8abu2EAcU" type="hidden">
      <input name="status" value="book" type="hidden">
      <input name="due_now_price" value="0" type="hidden">
      <input name="consumerprofile" value="1275730" type="hidden">
      <input name="consumermembership" value="817662" type="hidden">

      <button type="submit" style="background: #0d88cc; border-color: #0d88cc; border: 0px; color: #fff; line-height: 38px; text-shadow: none; font-size: 16px; border-radius: 4px; padding: 0px 20px; height: 43px;">Register for Single Class</button>

    </form>
</div>
```
### POST data
```
csrfmiddlewaretoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU
status=book
due_now_price=0
consumerprofile=1275730
consumermembership=817662
```
### POST address
https://goteamup.com/p/787790-crossfit-vetroz/e/9947791-wod/register/

### cURL command
`curl 'https://goteamup.com/p/787790-crossfit-vetroz/e/9947791-wod/register/' --2.0 -H 'Host: goteamup.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' -H 'Accept-Language: en-US,en;q=0.5' --compressed -H 'Referer: https://goteamup.com/p/787790-crossfit-vetroz/e/9947791-wod/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: sessionid=fewsa3umh7sl8nrv8xj055ekdc8sxett; csrftoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU; ajs_user_id=%22581902%22; ajs_group_id=null; ajs_anonymous_id=%22a7745ede-44d1-4817-8e2c-ed7b1a541eb4%22' -H 'DNT: 1' -H 'Connection: keep-alive' -H 'Upgrade-Insecure-Requests: 1' --data 'csrfmiddlewaretoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU&status=book&due_now_price=0&consumerprofile=1275730&consumermembership=817662'`

### Minimum request

```curl 'https://goteamup.com/p/787790-crossfit-vetroz/e/9947893-wod/register/' -H 'Referer: https://goteamup.com/p/787790-crossfit-vetroz/e/9947893-wod/' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: sessionid=fewsa3umh7sl8nrv8xj055ekdc8sxett; csrftoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU' --data 'csrfmiddlewaretoken=fWBQhSntDu7NUVKDwr61yBm8abu2EAcU&status=book&due_now_price=0&consumerprofile=1275730&consumermembership=817662'```


```curl '<page_address>/register/' -H 'Referer: <page_address>' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Cookie: sessionid=<session_id>; csrftoken=<csrftoken>' --data 'csrfmiddlewaretoken=<csrftoken>&status=book&due_now_price=0&consumerprofile=<profile>&consumermembership=<membership>'```

page_address = https://goteamup.com/p/787790-crossfit-vetroz/e/9947893-wod
session_id = fewsa3umh7sl8nrv8xj055ekdc8sxett
csrftoken = fWBQhSntDu7NUVKDwr61yBm8abu2EAcU (Seems that anything with 32 chars works)
profile = 1275730
membership = 817662
