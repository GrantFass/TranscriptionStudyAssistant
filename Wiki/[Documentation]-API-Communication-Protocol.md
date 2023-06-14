## Table of Contents

[[_TOC_]]

---

---

---

## Description

This document describes how messages will be sent between the application frontend and the application backend. This goes into detail about each individual message, how the message will be formatted, and what it will contain. Parts of the authorization pipeline and endpoints take inspiration from the [Auth0 API](https://auth0.com/docs/get-started/authentication-and-authorization-flow/add-login-auth-code-flow) as well as [RFC 8252](https://www.rfc-editor.org/rfc/rfc8252)

---

---

---

## Future Expansion

<details>
<summary>


</summary>

- We should add in the [state parameter](https://auth0.com/docs/secure/attack-protection/state-parameters) to our authorization endpoints as it can be used to help prevent cross site request forgery attacks.
- We need to define a limit for how much data can be stored on the remote server
- We should look into adding 2 factor authentication
- We should look into verifying the phone numbers on signup
- We should look into verifying the email addresses on signup
- we should look into adding security questions and answers on signup
- we should define a method for changing user data
- look into salting and encrypting the access tokens. may relate to the state parameter.
- look into storing a client instance ID instead of the username and token for security reasons
- Look into shared embedding between text and images using [CLIP](https://openai.com/blog/clip/).
- Look into performing node vectorization and embedding over entire sentences as a whole. Find similar ones to group before summarization.

</details>

---

---

---

## Communication Protocol

The original aim was to develop the protocol to run over MQTT. This would let us publish messages to a channel over a broker. We could then subscribe to the required channels. With the transition to a web application this is no longer necessary or practical. Instead the application backend will be setup as a REST service. This will let us set up individual endpoints for every action we would like to be available on the webpage.

---

---

---

## Communication Format

Messages will be formatted in JSON. This will allow for easy analysis and parsing of the message. It also allows us to run JSON schema validation over the message in order to quickly check for missing fields during development. The data for the messages is passed in the REST request body.

---

---

---

## Standard Message Components

<details>
<summary>


</summary>
This section details the standard components that all messages should have. These fields are always required and should always be populated. The backend will return error codes if one of these components is missing.

- `ts`
  - This field represents the timestamp of when the message was sent. It contains the number of milliseconds since epoch in UNIX standard time.
  - formatted as a long
- `cID`
  - This field represents the correlation identifier for the given message. This primarily used to identify what request a response message is associated with. See the UUID section for format.

### Additional Standard Message Components For Requests

This section details the standard components that all request messages should have. This is in addition to the standard message components defined above. These fields are always required and should always be populated for all topics EXCEPT the authorization and authentication topic endpoints. The backend will return error codes if one of these components is missing.

- `username`
  - This field contains the username of the currently active user as cached in the application. The cached value should be updated during the login and authentication process. As such, this field is required for every message, except those under the list of authentication topics.
  - This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `token`
  - This field contains the authorization token of the currently active user as cached in the application. As with the `username` field, this cached value should be updated during the login and authentication process. As such, this field is also required for every message, except those under the list of authentication topics. See the UUID section for format details.

### Additional Standard Message Components For Responses

This section details the standard components that all response messages should have. This is in addition to the standard message components defined above. As with the standard message components, these fields are always required and should always be populated unless otherwise stated. The backend will return error codes if one of these components is missing.

- `err`
  - This field is used to report errors that may have occurred with a given request.
  - This field is a JSON object. Below is a listing of keys that must be present in this object.
    - `code`
      - This field is populated with a value denoting the type of error that occurred. See the below section on error codes for exact values.
      - This field is formatted as an integer.
    - `msg`
      - This field should be populated with a message denoting the nature of the error and or providing more information for a given error.
      - This field is formatted as a string.
  - Below is a listing of keys that are optionally present in this object. The inclusion of these keys depend on the topic the response message is generated for.
    - `info`
      - This key is used to provide additional information about a given error code. It is commonly used with the file handling endpoints. In these cases it is used to return a listing of files that failed a given operation. Due to its ambiguous nature its type can shift between JSON object and list of JSON objects as need by individual endpoints. See the specific endpoints for more details.

### Optional Message Components

This section details message components that are optional. These components are required on a topic-by-topic basis. As such, see the individual topic endpoints for more details.

- `p`
  - This is the payload field. Any additional information that is contained in a message is sent in this field. This field is used for almost every message except acknowledgment messages.
  - This is always a JSON object and will be populated with various keys. The exact keys depend on the topic the message is being sent over, as well as the direction the message is traveling.

### Example Standard Message

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {...}
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {...}
}
```

</details>

---

---

---

## Topics & Endpoints

The topic field will change based on three properties:

1. The direction of the message being sent.
2. The subtopic data is being sent for. ~~3. The correlation ID for a response message.~~

Messages sent from the backend to the frontend will have their REST endpoints prefixed with `bf`. Messages sent from the frontend to the backend will have their REST endpoint prefixed with `fb`. Endpoints may optionally be suffixed by the correlation ID in certain cases as defined by the individual below topic sections.

---

### Authentication Topics

These topics relate to authentication. This includes logging in, signing up, and exchanging passwords.

#### Create New User

<details>
<summary>


</summary>
This command should be used to create a new user profile in the application backend. All of the required information to create a new account should be passed through this method. This does not login the new account. The user must do that manually after their new account is created.

**_Topic:_**\
A request to create a new user should be sent over the REST endpoint `fb/auth/new`. ~~The response to this request should be sent over `bf/auth/cID`.~~

**_Request Payload Components:_**

- `email`
  - The email address of the client.
  - This field is formatted as a string. It should follow proper email address syntax as defined in [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322).
- `password`
  - The password to use to authenticate logins to this client account.
  - The password should be formatted as a string. It should be at least 8 characters in length. It should also require at least one letter and one number.
- `birthday`
  - The client's birthday. This should be formatted as MM/DD/YYYY.
  - This is formatted as a string. Values for the months should be in the range \[0, 12\]. Values for the days should be in the range \[0, 31\]. Values for the year should not exceed the current year, nor precede 1900.
- `org`
  - The name of the organization the client is affiliated with. This should be left blank if not applicable.
  - This is formatted as a string. This should be a sanitized input. It likely should only allow alphanumeric, spaces, and hyphens.
- `first`
  - The first name of the client.
  - This is a string. It likely should only allow alphanumeric, spaces, and hyphens.
- `last`
  - The last name of the client.
  - This is a string. It likely should only allow alphanumeric, spaces, and hyphens.
- `gender`
  - The gender of the client. This should be an enumerator of values including the following options:
    - male, female, other, prefer not to disclose.
- `phone`
  - The client's phone number.
  - This should be an 11 digit number as defined by [RFC 3966](https://www.ietf.org/rfc/rfc3966.txt). Thus it can be formatted as an integer.
- `job`
  - The title of the client's job. This should likely be an enumerator of possible values including the following options:
    - student, developer, other.
- `username`: The username for the new account. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `username`
  - This is the value of the username field that was sent to the authentication system. If login failed we should use this value to repopulate the username field of the login form. If login succeeded we should temporarily store this value so that we can pass it as a part of other requests to the backend.
  - This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `redirect`
  - This is used to redirect the application to a specific page after the signup process has completed. If the authentication failed this value should be empty. This is so that signup can be attempted again.
  - This should be formatted as a string containing a URI to another webpage on our site. Usually this other page will be the login page. This is done so the newly created account can login right away.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "email": "example@mail.net",
    "password": "QwertY123!",
    "birthday": "12/25/1970",
    "org": "MSOE",
    "first": "Jane",
    "last": "Doe",
    "gender": 3,
    "phone": 12345678901,
    "job": 0,
    "username": "DoeJ1970"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "redirect": "login.ts"
  }
}
```

</details>

#### Login User

<details>
<summary>


</summary>
This command should be used to log in an existing user profile. Required login information should be passed through this method.

**_Topic:_**\
A request to log in a user should be sent over the REST endpoint `fb/auth/in`. ~~The response to this request should be sent back over `bf/auth/cID`.~~

**_Request Payload Components:_**\
The request payload components, aside from the usual login information, are used for security purposes. The extra information is used to detect if somebody is trying to brute force their way into an account. Data that can be used for this can be seen from [Deviceinfo.me](https://www.deviceinfo.me/).

- `username`: The account to login. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `password`
  - The password to use to attempt to login the account.
  - The password should be formatted as a string. It should be at least 8 characters in length. It should also require at least one letter and one number.
- `ip`
  - The IP address of the client requesting the login. This should be recorded as IPv6 if possible, otherwise it should be recorded as IPv4. This will follow [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) for IPv4 and [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291.html) for IPv6.
  - This is a string that contains a IPv4 or IPv6 address.
- `os`
  - The operating system of the device the application was launched on.
  - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
- `browser`
  - The web browser name and version of of the device the application was launched on.
  - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
- `device`
  - The type of device the application was launched on.
  - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
- `location`
  - The device's geolocation.
  - This should be a string. It should be in the format of CITY, REGION OR STATE, COUNTRY. As such it should be a sanitized string that includes alphanumeric, spaces, underscores, hyphens, parentheses, and commas.
- `redirect`
  - This is used to store the location in the web page that the login request was generated from. This is used so we can return to that location after login is completed. If it is unknown where the login request was launched from, we should populate this value with the home page or index page of the application.
  - This should be formatted as a string containing a URI to another webpage on our site.

**_Response Payload Components:_**

- `token`
  - This the authorization token generated by the authentication system if the authentication process succeeded. This should be a unique key. This key should expire in the backend after 15 minutes of inactivity on a user's account. This way we can automatically log out users that are inactive for security reasons and allow for key reuse if needed. This key will need to be stored by the application so it can be passed as part of other requests. See the UUID section for format details.
- `username`
  - This is the value of the username field that was sent to the authentication system. If login failed we should use this value to repopulate the username field of the login form. If login succeeded we should temporarily store this value so that we can pass it as a part of other requests to the backend.
  - This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `redirect`
  - This is used to redirect the application to a specific page after the login process has completed. If the authentication failed this value should be empty. This is so that login can be attempted again.
  - This should be formatted as a string containing a URI to another webpage on our site.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "username": "DoeJ1970",
    "password": "QwertY123!",
    "ip": "75.103.1.21",
    "os": "Microsoft Windows (build 103)",
    "browser": "Mozilla Firefox (build 1.1.2)",
    "device": "Unknown",
    "location": "Milwaukee WI",
    "redirect": "example.com/index"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
    "username": "DoeJ1970",
    "redirect": "example.com/index"
  }
}
```

</details>

#### Logout User

<details>
<summary>


</summary>
This command should be used to logout the user manually. This command can be used to logout from just the one client that sent the request, or all connected clients. The different logout methods will be specified through a field in the payload.

**_Topic:_**\
A request to logout the user should be sent over the REST endpoint `fb/auth/out`. ~~The response to this request should be sent back over `bf/auth/cID`.~~

**_Request Payload Components:_**

- `username`: The account to log out. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `token`
  - This is the authorization token of the currently active user cached in the application. See the UUID section for format details.
- `all`: a boolean field. true denotes logging out from all devices. false denotes logging out from only one device.

**_Response Payload Components:_**

- `username`: The account logged out of devices. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `count`
  - The number of devices that the user was logged out from
  - This is a positive integer that includes 0.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "username": "DoeJ1970",
    "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
    "all": false
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "count": 1
  }
}
```

</details>

#### Password Reset

<details>
<summary>


</summary>
This command should be used in order to initiate the password reset process. In the future we may want to add logic for security questions. This method will not authenticate the specified account into the system. Instead the user will be required to login with their new password through the normal login portal.

**_Topic:_**\
A request to initiate the password reset process should be sent over the REST endpoint `fb/auth/exchange`. ~~The response to this request should be sent back over the topic `bf/auth/cID`.~~

**_Request Payload Components:_**

- `username`: The account to reset the password for. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `email`
  - This is the email of the account to send a password reset link to. This email address must match the one stored in the backend for the link to be sent.
  - This field is formatted as a string. It should follow proper email address syntax as defined in [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322).
- `phone`
  - This is the phone number of the account to send a password reset link to. This phone number must match the one stored in the backend for the link to be sent.
  - This should be an 11 digit number as defined by [RFC 3966](https://www.ietf.org/rfc/rfc3966.txt). Thus it can be formatted as an integer.

**_Response Payload Components:_**

- `username`: The account the password was reset for. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "username": "DoeJ1970",
    "email": "example@mail.net",
    "phone": 12345678901
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970"
  }
}
```

</details>

### Account Information Topics

These topics relate to information about the given user account.

#### Get Device History List

<details>
<summary>


</summary>
This command should be used in order to request a list of all of the devices that the user has logged into since the last time the device history was cleared. It may also be a good idea to return if the user was logged out due to inactivity or due to clicking the logout button if possible.

**_Topic:_**\
A request to list all of the devices the user has logged into should be sent over the REST endpoint `fb/acc/list`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**

- `num`
  - The number of entries to get in the device history list. A value of -1, or a value that exceeds the total number of entries, will return all entries associated with the account. All other positive values will return the specified number of most recent entries.
  - This is an integer

**_Response Payload Components:_**

- `username`: The account the history list is for. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `list`
  - This is the list of device histories. Each device history should be formatted as a JSON object. The below list of keys should be present in each of the JSON objects. This is the same information that is recorded as a part of the `Login User` endpoint.
    - `IP`
      - The IP address of the client that requested the login. This should be recorded as IPv6 if possible, otherwise it should be recorded as IPv4. This will follow [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) for IPv4 and [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291.html) for IPv6.
      - This is a string that contains a IPv4 or IPv6 address.
    - `OS`
      - The operating system of the device the client that requested the login was running on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `Browser`
      - The web browser name and version the client that requested the login was running on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `Device`
      - The type of device the client that request the login was on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `Location`
      - The geolocation of the client that requested the login.
      - This should be a string. It should be in the format of CITY, REGION OR STATE, COUNTRY. As such it should be a sanitized string that includes alphanumeric, spaces, underscores, hyphens, parentheses, and commas.
    - `ts`
      - The timestamp of when the login request was made. This is the number of milliseconds since epoch in UNIX standard time.
      - formatted as a long. This should be the time since epoch in milliseconds according to UNIX standard time.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "num": -1
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "list": [
      {
        "ip": "75.103.1.21",
        "os": "Microsoft Windows (build 103)",
        "browser": "Mozilla Firefox (build 1.1.2)"
        "device": "Unknown",
        "location": "Milwaukee WI",
        "ts": 1666818622000
      },
      {
        "ip": "75.103.1.21",
        "os": "Microsoft Windows (build 103)",
        "browser": "Mozilla Firefox (build 1.1.2)"
        "device": "Unknown",
        "location": "Milwaukee WI",
        "ts": 1666818622000
      },
    ]
  }
}
```

</details>

#### Clear Device History List

<details>
<summary>


</summary>
This command should be used in order to clear the history list of all devices the user has logged into. Different amounts of history can be cleared based on a parameter in the request.

**_Topic:_**\
A request to clear the list of all of the devices the user has logged into should be sent over the REST endpoint `fb/acc/clear`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**

- `num`
  - The number of entries to clear from the device history list. A value of -1, or a value that exceeds the total number of entries, will clear all entries associated with the account. All other positive values will clear the specified number of most recent entries.
  - This is an integer

**_Response Payload Components:_**

- `num`
  - The number of entries that were cleared from the device history list
  - This is an integer

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "num": -1
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "num": 4
  }
}
```

</details>

#### Get Connected Devices

<details>
<summary>


</summary>
This command should be used in order to get a list of all the devices that are currently logged into this users account.

**_Topic:_**\
A request to get a list of all devices that are currently logged into this user's account should be sent over the REST endpoint `fb/acc/connected`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**\
There is no payload required for the request message for this topic.

**_Response Payload Components:_**

- `username`: The account the logged in devices list is for. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `list`
  - This is the list of logged in devices. Each device should be formatted as a JSON object. The below list of keys should be present in each of the JSON objects. This is the same information that is recorded as a part of the `Login User` endpoint.
    - `ip`
      - The IP address of the client that requested the login. This should be recorded as IPv6 if possible, otherwise it should be recorded as IPv4. This will follow [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) for IPv4 and [RFC 4291](https://www.rfc-editor.org/rfc/rfc4291.html) for IPv6.
      - This is a string that contains a IPv4 or IPv6 address.
    - `os`
      - The operating system of the device the client that requested the login was running on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `browser`
      - The web browser name and version the client that requested the login was running on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `device`
      - The type of device the client that request the login was on.
      - This should be a string. It should be sanitized to include alphanumeric, spaces, underscores, hyphens, periods, and parentheses.
    - `location`
      - The geolocation of the client that requested the login.
      - This should be a string. It should be in the format of CITY, REGION OR STATE, COUNTRY. As such it should be a sanitized string that includes alphanumeric, spaces, underscores, hyphens, parentheses, and commas.
    - `ts`
      - The timestamp of when the login request was made. This is the number of milliseconds since epoch in UNIX standard time.
      - formatted as a long. This should be the time since epoch in milliseconds according to UNIX standard time.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "list": [
      {
        "ip": "75.103.1.21",
        "os": "Microsoft Windows (build 103)",
        "browser": "Mozilla Firefox (build 1.1.2)"
        "device": "Unknown",
        "location": "Milwaukee WI",
        "ts": 1666818622000
      },
      {
        "ip": "75.103.1.21",
        "os": "Microsoft Windows (build 103)",
        "browser": "Mozilla Firefox (build 1.1.2)"
        "device": "Unknown",
        "location": "Milwaukee WI",
        "ts": 1666818622000
      },
    ]
  }
}
```

</details>

#### Set Maximum Connections

<details>
<summary>


</summary>
This command should be used to set the value for the maximum number of concurrent users.

**_Topic:_**\
A request to set the maximum number of concurrent users for this account should be sent over the REST endpoint `fb/acc/max`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**

- `max`
  - This is the value for the maximum number of users allowed to be logged into this account at the same time. It is recommended to leave this value at 2 if you frequently use the application on different devices. This number must be positive and less than 8.
  - This is a positive integer.

**_Response Payload Components:_**

- `username`: Account the maximum concurrent sessions was set for. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `max`
  - This is the current maximum number of concurrent sessions allowed for the user.
  - This is a positive integer.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "max": 2
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "max": 2
  }
}
```

</details>

#### Get Stored Information

<details>
<summary>


</summary>
This command should be used to get all of the information that is stored for the current user. This will not include the device history list since that information is gathered through a separate API endpoint.

**_Topic:_**\
A request to get all of the information that is stored and logged for a given account should be sent over the REST endpoint `fb/acc/info`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**\
There is no payload required for the request message for this topic.

**_Response Payload Components:_**

- `email`
  - The account email address.
  - This field is formatted as a string. It should follow proper email address syntax as defined in [RFC 5322](https://www.rfc-editor.org/rfc/rfc5322).
- `birthday`
  - The account birthday. This is formatted as MM/DD/YYYY
  - This is formatted as a string. Values for the months should be in the range \[0, 12\]. Values for the days should be in the range \[0, 31\]. Values for the year should not exceed the current year, nor precede 1900.
- `org`
  - This is the name of the organization the client is affiliated with.
  - This is formatted as a string. This should be a sanitized input. It likely should only allow alphanumeric, spaces, and hyphens.
- `first`
  - This is the first name associated with the account.
  - This is a string. It likely should only allow alphanumeric, spaces, and hyphens.
- `last`
  - This is the last name associated with the account.
  - This is a string. It likely should only allow alphanumeric, spaces, and hyphens.
- `gender`
  - This is the gender associated with the account. This should be an enumerator of values as specified in the Create New User endpoint.
  - This is an enumerator of possible values. See the sign up endpoint for more information.
- `phone`
  - This is the phone number associated with the account.
  - This should be an 11 digit number as defined by [RFC 3966](https://www.ietf.org/rfc/rfc3966.txt). Thus it can be formatted as an integer.
- `job`
  - This is the tile of the clients job associated with the account. This should be an enumerator of possible values as specified in the Create New User endpoint.
  - This is an enumerator of possible values. See the sign up endpoint for more information.
- `nUniqueIP`
  - This should return the number of unique IP addresses the account has logged in from based on the current device history associated with the account.
  - This is an integer.
- `nUniqueOS`
  - This should return the number of unique operating systems the account has logged in from based on the current device history associated with the account.
  - This is an integer.
- `nUniqueBrowser`
  - This should return the number of unique browsers (including versions) that the account has logged in from based on the current device history associated with the account.
  - This is an integer.
- `nUniqueDevice`
  - This should return the number of unique devices that the account has logged in from based on the current device history associated with the account.
  - This is an integer.
- `nUniqueLocation`
  - This should return the number of unique locations that the account has logged in from based on the current device history associated with the account. This measures the unique locations based by city and or zip code.
  - This is an integer.
- `nStoredFiles`
  - This should return the number of files that are currently stored for the user
  - This is an integer.
- `StorageSize`
  - This should return the amount of space in bytes that the user's files take up
  - This should be a long or an int64 depending on the language.
- `CreationDate`
  - This should return the date the account was created. This will be formatted as MM/DD/YYYY
  - This is formatted as a string. Values for the months should be in the range \[0, 12\]. Values for the days should be in the range \[0, 31\]. Values for the year should not exceed the current year, nor precede 1900.
- `days`
  - This should return the number of days that the account has existed for.
  - This is an integer.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "email": "example@mail.net",
    "birthday": "12/25/1970",
    "org": "MSOE",
    "first": "Jane",
    "last": "Doe",
    "gender": 3,
    "phone": 12345678901,
    "job": 0,
    "nUniqueIP": 5,
    "nUniqueOS": 4,
    "nUniqueBrowser": 27,
    "nUniqueLocation": 33,
    "nStoredFiles" 102,
    "StorageSize": 123456,
    "CreationDate": "01/01/1970",
    "days": 359
  }
}
```

</details>

#### Delete Account

<details>
<summary>


</summary>
This command should be used to delete the entire user account and all of the information that is stored for that account. This will include deleting all files and device history.

**_Topic:_**\
A request to delete the user's account and all of the stored information on file should be sent over the REST endpoint `fb/acc/delete`. ~~The response to this request should be sent back over the topic `bf/acc/cID`.~~

**_Request Payload Components:_**\
There is no payload required for the request message for this topic.

**_Response Payload Components:_**

- `redirect`
  - This is the uri to redirect the user to upon success of deleting the account. This should likely be the home or index page of the application.
  - This should be a string containing a valid link to a non-protected webpage on our site.
- `username`
  - This is a string representing which account was deleted
- `n_login_logs`
  - This is an integer representing how many login logs were deleted during account deletion
- `n_user_files`
  - This is an integer representing how many user files were deleted during account deletion.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "username": "DoeJ1970",
    "n_login_logs": 123,
    "n_user_files": 12,
    "redirect": "example.com/goodbye"
  }
}
```

</details>

### File Management Topics

This section contains commands that relate to the management and manipulation of files in the user account backend.

#### Upload Folders & Files

<details>
<summary>


</summary>
This command should be used to upload a file or folder of files to the user's account in the backend. Either should be accepted using this same command. Note that user's will be limited based on the size of the files they upload as well as the types of the files. Files will attempt to be uploaded in order. Files will likely be stored in an object store in the backend. This means that all directories would be simulated as the paths would actually be URIs. Each uploaded file will be converted into a JSON file for the backend. Information about the file will be stored under that JSON document. Review the section at the end of the document specifying stored file format.

**_Topic:_**\
A request to upload folders and or files to the users directory in the backend should be sent over the REST endpoint `fb/file/up`. ~~The response to this request should be sent back over the topic `bf/file/cID`.~~

**_Request Payload Components:_**

- `files`
  - This is a list of JSON objects. Each object represents a single file to attempt to upload to the backend. Each object should contain the following information:
    - `path`: The file to attempt to upload. This field should follow the constraints at the bottom of the document in the Username And File Path section.
    - `data`
      - This is the data of the file to create. This should likely be base64 encoded text in order to preserve size.
      - This is a base64 encoded string.
    - `overwrite`
      - This parameter is used to specify if the file should be overwritten if a file at that path already exists.
      - This is a boolean value. A value of `true` specifies the file data will be overwritten.
    - `preprocess`
      - This parameter is used to specify if the file text data should be preprocessed on import or not.
      - This is a boolean value. A value of `true` specifies that the text will be preprocessed.

**_Response Payload Components:_**

- `success`
  - This is a list of JSON objects. Each object represents a file that succeeded in being uploaded to the backend. Each object will have the following information:
    - `path`: The file that was uploaded. This field should follow the constraints at the bottom of the document in the Username And File Path section.
    - `size`
      - This returns the new size of the file in bytes as it is stored in the account backend.
      - This is formatted as a long or an int64 depending on the language.
    - `processed`
      - This is a boolean value specifying if the file data went through preprocessing or not. A value of `true` specifies that the text was preprocessed.
- `info` field in `err` object:
  - This is a list of JSON objects. Each object represents a file that failed being uploaded to the backend for various reasons. Each object will have the following information:
    - `path`: The file that failed to upload. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "files": [
      {
        "path": "user/texts/sample_b64.txt",
        "data": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdCwgc2VkIGRvIGVpdXNtb2QgdGVtcG9yIGluY2lkaWR1bnQgdXQgbGFib3JlIGV0IGRvbG9yZSBtYWduYSBhbGlxdWEu",
        "overwrite": true,
        "preprocess": false
      },
      {
        "path": "user/texts/sample_raw.txt",
        "data": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "overwrite": false,
        "preprocess": true
      },
      {
        "path": "user/texts/sample_ted.txt",
        "data": "Good morning. How are you?(Laughter)It's been great, hasn't it? I've been blown away by the whole thing. In fact, I'm leaving.(Laughter)There have been three themes running through the conference which are relevant to what I want to talk about. One is the extraordinary evidence of human creativity in all of the presentations that we've had and in all of the people here. Just the variety of it and the range of it. The second is that it's put us in a place where we have no idea what's going to happen, in terms of the future. No idea how this may play out.I have an interest in education. Actually, what I find is everybody has an interest in education. Don't you? I find this very interesting. If you're at a dinner party, and you say you work in education — Actually, you're not often at dinner parties, frankly.(Laughter)If you work in education, you're not asked.(Laughter)And you're never asked back, curiously. That's strange to me. But if you are, and you say to somebody, you know, they say, \"What do you do?\" and you say you work in education, you can see the blood run from their face. They're like, \"Oh my God,\" you know, \"Why me?\"(Laughter)\"My one night out all week.\"(Laughter)But if you ask about their education, they pin you to the wall. Because it's one of those things that goes deep with people, am I right? Like religion, and money and other things. So I have a big interest in education, and I think we all do. We have a huge vested interest in it, partly because it's education that's meant to take us into this future that we can't grasp. If you think of it, children starting school this year will be retiring in 2065. Nobody has a clue, despite all the expertise that's been on parade for the past four days, what the world will look like in five years' time. And yet we're meant to be educating them for it. So the unpredictability, I think, is extraordinary.And the third part of this is that we've all agreed, nonetheless, on the really extraordinary capacities that children have — their capacities for innovation. I mean, Sirena last night was a marvel, wasn't she? Just seeing what she could do. And she's exceptional, but I think she's not, so to speak, exceptional in the whole of childhood. What you have there is a person of extraordinary dedication who found a talent. And my contention is, all kids have tremendous talents. And we squander them, pretty ruthlessly.So I want to talk about education and I want to talk about creativity. My contention is that creativity now is as important in education as literacy, and we should treat it with the same status.(Applause) Thank you.(Applause)That was it, by the way. Thank you very much.(Laughter)So, 15 minutes left.(Laughter)Well, I was born... no.(Laughter)I heard a great story recently — I love telling it — of a little girl who was in a drawing lesson. She was six, and she was at the back, drawing, and the teacher said this girl hardly ever paid attention, and in this drawing lesson, she did. The teacher was fascinated. She went over to her, and she said, \"What are you drawing?\" And the girl said, \"I'm drawing a picture of God.\" And the teacher said, \"But nobody knows what God looks like.\" And the girl said, \"They will, in a minute.\"(Laughter)When my son was four in England — Actually, he was four everywhere, to be honest.(Laughter)If we're being strict about it, wherever he went, he was four that year. He was in the Nativity play. Do you remember the story?(Laughter)No, it was big, it was a big story. Mel Gibson did the sequel, you may have seen it.(Laughter)\"Nativity II.\" But James got the part of Joseph, which we were thrilled about. We considered this to be one of the lead parts. We had the place crammed full of agents in T-shirts: \"James Robinson IS Joseph!\" (Laughter) He didn't have to speak, but you know the bit where the three kings come in? They come in bearing gifts, gold, frankincense and myrrh. This really happened. We were sitting there and I think they just went out of sequence, because we talked to the little boy afterward and we said, \"You OK with that?\" And he said, \"Yeah, why? Was that wrong?\" They just switched. The three boys came in, four-year-olds with tea towels on their heads, and they put these boxes down, and the first boy said, \"I bring you gold.\" And the second boy said, \"I bring you myrrh.\" And the third boy said, \"Frank sent this.\"(Laughter)What these things have in common is that kids will take a chance. If they don't know, they'll have a go. Am I right? They're not frightened of being wrong. I don't mean to say that being wrong is the same thing as being creative. What we do know is, if you're not prepared to be wrong, you'll never come up with anything original — if you're not prepared to be wrong. And by the time they get to be adults, most kids have lost that capacity. They have become frightened of being wrong. And we run our companies like this. We stigmatize mistakes. And we're now running national education systems where mistakes are the worst thing you can make. And the result is that we are educating people out of their creative capacities.Picasso once said this, he said that all children are born artists. The problem is to remain an artist as we grow up. I believe this passionately, that we don't grow into creativity, we grow out of it. Or rather, we get educated out of it. So why is this?I lived in Stratford-on-Avon until about five years ago. In fact, we moved from Stratford to Los Angeles. So you can imagine what a seamless transition that was.(Laughter)Actually, we lived in a place called Snitterfield, just outside Stratford, which is where Shakespeare's father was born. Are you struck by a new thought? I was. You don't think of Shakespeare having a father, do you? Do you? Because you don't think of Shakespeare being a child, do you? Shakespeare being seven? I never thought of it. I mean, he was seven at some point. He was in somebody's English class, wasn't he?(Laughter)How annoying would that be?(Laughter)\"Must try harder.\"(Laughter)Being sent to bed by his dad, you know, to Shakespeare, \"Go to bed, now! And put the pencil down.\"(Laughter)\"And stop speaking like that.\"(Laughter)\"It's confusing everybody.\"(Laughter)Anyway, we moved from Stratford to Los Angeles, and I just want to say a word about the transition. My son didn't want to come. I've got two kids; he's 21 now, my daughter's 16. He didn't want to come to Los Angeles. He loved it, but he had a girlfriend in England. This was the love of his life, Sarah. He'd known her for a month.(Laughter)Mind you, they'd had their fourth anniversary, because it's a long time when you're 16. He was really upset on the plane, he said, \"I'll never find another girl like Sarah.\" And we were rather pleased about that, frankly —(Laughter)Because she was the main reason we were leaving the country.(Laughter)But something strikes you when you move to America and travel around the world: Every education system on Earth has the same hierarchy of subjects. Every one. Doesn't matter where you go. You'd think it would be otherwise, but it isn't. At the top are mathematics and languages, then the humanities, and at the bottom are the arts. Everywhere on Earth. And in pretty much every system too, there's a hierarchy within the arts. Art and music are normally given a higher status in schools than drama and dance. There isn't an education system on the planet that teaches dance everyday to children the way we teach them mathematics. Why? Why not? I think this is rather important. I think math is very important, but so is dance. Children dance all the time if they're allowed to, we all do. We all have bodies, don't we? Did I miss a meeting?(Laughter)Truthfully, what happens is, as children grow up, we start to educate them progressively from the waist up. And then we focus on their heads. And slightly to one side.If you were to visit education, as an alien, and say \"What's it for, public education?\" I think you'd have to conclude, if you look at the output, who really succeeds by this, who does everything that they should, who gets all the brownie points, who are the winners — I think you'd have to conclude the whole purpose of public education throughout the world is to produce university professors. Isn't it? They're the people who come out the top. And I used to be one, so there.(Laughter)And I like university professors, but you know, we shouldn't hold them up as the high-water mark of all human achievement. They're just a form of life, another form of life. But they're rather curious, and I say this out of affection for them. There's something curious about professors in my experience — not all of them, but typically, they live in their heads. They live up there, and slightly to one side. They're disembodied, you know, in a kind of literal way. They look upon their body as a form of transport for their heads.(Laughter)Don't they? It's a way of getting their head to meetings.(Laughter)If you want real evidence of out-of-body experiences, get yourself along to a residential conference of senior academics, and pop into the discotheque on the final night.(Laughter)And there, you will see it. Grown men and women writhing uncontrollably, off the beat.(Laughter)Waiting until it ends so they can go home and write a paper about it.(Laughter)Our education system is predicated on the idea of academic ability. And there's a reason. Around the world, there were no public systems of education, really, before the 19th century. They all came into being to meet the needs of industrialism. So the hierarchy is rooted on two ideas.Number one, that the most useful subjects for work are at the top. So you were probably steered benignly away from things at school when you were a kid, things you liked, on the grounds that you would never get a job doing that. Is that right? Don't do music, you're not going to be a musician; don't do art, you won't be an artist. Benign advice — now, profoundly mistaken. The whole world is engulfed in a revolution.And the second is academic ability, which has really come to dominate our view of intelligence, because the universities designed the system in their image. If you think of it, the whole system of public education around the world is a protracted process of university entrance. And the consequence is that many highly-talented, brilliant, creative people think they're not, because the thing they were good at at school wasn't valued, or was actually stigmatized. And I think we can't afford to go on that way.In the next 30 years, according to UNESCO, more people worldwide will be graduating through education than since the beginning of history. More people, and it's the combination of all the things we've talked about — technology and its transformation effect on work, and demography and the huge explosion in population.Suddenly, degrees aren't worth anything. Isn't that true? When I was a student, if you had a degree, you had a job. If you didn't have a job, it's because you didn't want one. And I didn't want one, frankly. (Laughter) But now kids with degrees are often heading home to carry on playing video games, because you need an MA where the previous job required a BA, and now you need a PhD for the other. It's a process of academic inflation. And it indicates the whole structure of education is shifting beneath our feet. We need to radically rethink our view of intelligence.We know three things about intelligence. One, it's diverse. We think about the world in all the ways that we experience it. We think visually, we think in sound, we think kinesthetically. We think in abstract terms, we think in movement. Secondly, intelligence is dynamic. If you look at the interactions of a human brain, as we heard yesterday from a number of presentations, intelligence is wonderfully interactive. The brain isn't divided into compartments. In fact, creativity — which I define as the process of having original ideas that have value — more often than not comes about through the interaction of different disciplinary ways of seeing things.By the way, there's a shaft of nerves that joins the two halves of the brain called the corpus callosum. It's thicker in women. Following off from Helen yesterday, this is probably why women are better at multi-tasking. Because you are, aren't you? There's a raft of research, but I know it from my personal life. If my wife is cooking a meal at home — which is not often, thankfully.(Laughter)No, she's good at some things, but if she's cooking, she's dealing with people on the phone, she's talking to the kids, she's painting the ceiling, she's doing open-heart surgery over here. If I'm cooking, the door is shut, the kids are out, the phone's on the hook, if she comes in I get annoyed. I say, \"Terry, please, I'm trying to fry an egg in here.\"(Laughter)\"Give me a break.\"(Laughter)Actually, do you know that old philosophical thing, if a tree falls in a forest and nobody hears it, did it happen? Remember that old chestnut? I saw a great t-shirt recently, which said, \"If a man speaks his mind in a forest, and no woman hears him, is he still wrong?\"(Laughter)And the third thing about intelligence is, it's distinct. I'm doing a new book at the moment called \"Epiphany,\" which is based on a series of interviews with people about how they discovered their talent. I'm fascinated by how people got to be there. It's really prompted by a conversation I had with a wonderful woman who maybe most people have never heard of, Gillian Lynne. Have you heard of her? Some have. She's a choreographer, and everybody knows her work. She did \"Cats\" and \"Phantom of the Opera.\" She's wonderful. I used to be on the board of The Royal Ballet, as you can see. Anyway, Gillian and I had lunch one day and I said, \"How did you get to be a dancer?\" It was interesting. When she was at school, she was really hopeless. And the school, in the '30s, wrote to her parents and said, \"We think Gillian has a learning disorder.\" She couldn't concentrate; she was fidgeting. I think now they'd say she had ADHD. Wouldn't you? But this was the 1930s, and ADHD hadn't been invented at this point. It wasn't an available condition.(Laughter)People weren't aware they could have that.(Laughter)Anyway, she went to see this specialist. So, this oak-paneled room, and she was there with her mother, and she was led and sat on this chair at the end, and she sat on her hands for 20 minutes while this man talked to her mother about the problems Gillian was having at school. Because she was disturbing people; her homework was always late; and so on, little kid of eight. In the end, the doctor went and sat next to Gillian, and said, \"I've listened to all these things your mother's told me, I need to speak to her privately. Wait here. We'll be back; we won't be very long,\" and they went and left her.But as they went out of the room, he turned on the radio that was sitting on his desk. And when they got out, he said to her mother, \"Just stand and watch her.\" And the minute they left the room, she was on her feet, moving to the music. And they watched for a few minutes and he turned to her mother and said, \"Mrs. Lynne, Gillian isn't sick; she's a dancer. Take her to a dance school.\"I said, \"What happened?\" She said, \"She did. I can't tell you how wonderful it was. We walked in this room and it was full of people like me. People who couldn't sit still. People who had to move to think.\" Who had to move to think. They did ballet, they did tap, jazz; they did modern; they did contemporary. She was eventually auditioned for the Royal Ballet School; she became a soloist; she had a wonderful career at the Royal Ballet. She eventually graduated from the Royal Ballet School, founded the Gillian Lynne Dance Company, met Andrew Lloyd Webber. She's been responsible for some of the most successful musical theater productions in history, she's given pleasure to millions, and she's a multi-millionaire. Somebody else might have put her on medication and told her to calm down.(Applause)What I think it comes to is this: Al Gore spoke the other night about ecology and the revolution that was triggered by Rachel Carson. I believe our only hope for the future is to adopt a new conception of human ecology, one in which we start to reconstitute our conception of the richness of human capacity. Our education system has mined our minds in the way that we strip-mine the earth: for a particular commodity. And for the future, it won't serve us. We have to rethink the fundamental principles on which we're educating our children.There was a wonderful quote by Jonas Salk, who said, \"If all the insects were to disappear from the Earth, within 50 years all life on Earth would end. If all human beings disappeared from the Earth, within 50 years all forms of life would flourish.\" And he's right.What TED celebrates is the gift of the human imagination. We have to be careful now that we use this gift wisely and that we avert some of the scenarios that we've talked about. And the only way we'll do it is by seeing our creative capacities for the richness they are and seeing our children for the hope that they are. And our task is to educate their whole being, so they can face this future. By the way — we may not see this future, but they will. And our job is to help them make something of it.Thank you very much.(Applause)",
        "overwrite": true,
        "preprocess": true
      }
    ]
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": "", "info": []},
  "p": {
    "success": [
      {
        "path": "user/texts/sample_b64.txt",
        "size": 256,
        "processed": false
      },
      {
        "path": "user/texts/sample_ted.txt",
        "size": 739,
        "processed": true
      },
      {
        "path": "user/texts/sample_raw.txt",
        "size": 155,
        "processed": true
      }
    ]
  }
}
```

</details>

#### Download Folders & Files

<details>
<summary>


</summary>
This command should be used to download a file or groups of files from the user's account in the backend to their local machine. Either should be accepted using this same command.

**_Topic:_**\
A request to download folders and or files to the users directory in the backend should be sent over the REST endpoint `fb/file/down`. ~~The response to this request should be sent back over the topic `bf/file/cID`.~~

**_Request Payload Components:_**

- `files`
  - This is a list of JSON objects. Each object represents a single file to attempt to download from the backend. Each object should contain the following information:
    - `path`: The file to attempt to retrieve data for. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `success`
  - This is a list of JSON objects. Each object represents a file that succeeded in being downloaded from the backend. Each object will have the following information:
    - `path`: The file the retrieved data is for. This field should follow the constraints at the bottom of the document in the Username And File Path section.
    - `data`
      - This is the data stored for the given file in the backend.
      - This should be a JSON object. See the section at the end of this document on the custom backend file format for more details.
- `info` field in `err` object:
  - This is a list of JSON objects. Each object represents a file that failed being downloaded from the backend for various reasons. Each object will have the following information:
    - `path`: The file data retrieval failed for. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "files": [
      {
        "path": "user/texts/sample.txt"
      },
      {
        "path": "user/texts/sample.txt"
      }
    ]
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": "", "info": []},
  "p": {
    "success": [
      {
        "path": "user/texts/sample.txt",
        "data": {...}
      },
      {
        "path": "user/texts/sample.txt",
        "data": {...}
      }
    ]
  }
}
```

</details>

#### Get Storage Size

<details>
<summary>


</summary>
This command should be used to check how much storage space is in use and how much is available for the current user account in the backend.

**_Topic:_**\
A request to get storage information should be sent over the REST endpoint `fb/file/space`. ~~The response to this request should be sent back over the topic `bf/file/cID`.~~

**_Request Payload Components:_**\
There is no payload required for the request message for this topic.

**_Response Payload Components:_**

- `used`
  - The amount of space in bytes in use for the current user in the account backend.
  - This is formatted as a long or an int64 depending on the language.
- `total`
  - The total amount of space in bytes available to store user files in the account backend.
  - This is formatted as a long or an int64 depending on the language.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "used": 123456
    "total": 1024000
  }
}
```

</details>

#### Get User Files / Directory Information

<details>
<summary>


</summary>
This command should be used to obtain a listing of files that are in the users account in the backend. All of the users files will be returned at once from the backend. This means that any sorting or filtering will need to be done by the frontend.

**_Topic:_**\
A request to list the folders and or files that are in the users directory in the backend should be sent over the REST endpoint `fb/file/list`. ~~The response to this request should be sent back over the topic `bf/file/cID`.~~

**_Request Payload Components:_**\
There is no payload required for the request message for this topic.

**_Response Payload Components:_**

- `files`
  - This is a list of JSON objects. Each object represents a single file stored in the backend for the current account. Each object should contain the following information:
    - `path`: The file found in the user directory. This field should follow the constraints at the bottom of the document in the Username And File Path section.
    - `size`
      - This is the size, in bytes, of the file stored in the backend.
      - This is formatted as a long or an int64 depending on the language.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "files": [
      "path": "user/texts/sample.txt",
      "size": 736
    ]
  }
}
```

</details>

#### Delete / Remove Folders & Files

<details>
<summary>


</summary>
This command should be used to delete files or groups of files that are stored in the backend for the current account.

**_Topic:_**\
A request to delete folders and or files that are in the users directory in the backend should be sent over the REST endpoint `fb/file/remove`. ~~The response to this request should be sent back over the topic `bf/file/cID`.~~

**_Request Payload Components:_**

- `files`
  - This is a list of JSON objects. Each object represents a single file to attempt to remove from the backend. Each object should contain the following information:
    - `path`: The file to attempt to remove. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `success`
  - This is a list of JSON objects. Each object represents a file that succeeded in being deleted from the backend. Each object will have the following information:
    - `path`: The file that was removed. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `info` field in `err` object:
  - This is a list of JSON objects. Each object represents a file that failed being removed from the backend for various reasons. Each object will have the following information:
    - `path`: The file that failed to be removed. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "files": [
      {
        "path": "user/texts/sample.txt"
      }
    ]
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "14", "msg": "File Deletion Failed", "info": [{"path": "user/texts/sample.txt"}]},
  "p": {
    "success": []
  }
}
```

</details>

### Data Processing Topics

This section includes topics that relate to the processing of information and files that are stored in the account backend. This includes actions like summarizing text, extracting topics, and creating questions.

#### Process Video Transcript & Clean

<details>
<summary>


</summary>
This command should be used to run the preprocessing pipeline over a given file.

**_Topic:_**\
A request to process and clean a video transcript should be sent over the REST endpoint `fb/proc/clean`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file to attempt to process. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `inplace`
  - This is a variable representing if the cleaning pipeline should be run inplace. If this is set to true, then the pipeline will overwrite the current text of the file with the cleaned text.
  - This is a Boolean value.

**_Response Payload Components:_**

- `Acronyms`
  - This is a list of JSON objects. It contains a listing of the acronyms that were found in the text during cleaning. It also contains what each acronym stands for if it was found in the text. Each object should contain the following information:
    - `acronym`
      - This is the acronym.
      - This is a string. It is sanitized and should likely contain only alphanumeric.
    - `expanded`
      - This is the expanded form of the acronym if it was able to be found.
      - This is a string. It is sanitized and should likely contain only alphanumeric, spaces, hyphens, and underscores.
- `Equations`
  - This is a list of JSON objects. It contains a listing of the equations that were found in the text during cleaning. Each object should contain the following information:
    - `equation`
      - This is an equation that was found in the text.
      - This is a string of text that allows for math characters and Greek letters.
- `data`
  - This is the cleaned text data for the file that was processed. It should be encoded as base64.
  - This is a base64 encoded string of text.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/sample.txt",
    "inplace": true
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "Acronyms": [{
      "acronym": "MSOE",
      "expanded": "Milwaukee School Of Engineering"
    }],
    "Equations": [],
    "data": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4="
  }
}
```

</details>

#### Get Transcript Summary

<details>
<summary>


</summary>
This command should be used to generate a summary for a given document in the account backend.

**_Topic:_**\
A request to summarize a video transcript should be sent over the REST endpoint `fb/proc/summary`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file to attempt to summarize. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `data`
  - This is the summary of the text file. It is encoded in base64.
  - This is a base64 encoded string.
- `accuracy`
  - This is the accuracy of the given summary.
  - This is represented as a floating point number.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/sample.txt"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "data": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4=",
    "accuracy": 0.883
  }
}
```

</details>

#### Get Transcript Topics

<details>
<summary>


</summary>
This command should be used to generate a listing of topics as well as the keywords that are associated with that topic for a given document in the account backend.

**_Topic:_**\
A request to extract the topics and keywords from a video transcript should be sent over the REST endpoint `fb/proc/topics`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file to attempt to generate topics for. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `topics`
  - This is a list of JSON objects. It contains a listing of topics in order of prevalence in the document from largest to smallest. Each topic will also contain a set of keywords that make up and represent that topic. Each object should include the following:
    - `prevalence`
      - This represents the prevalence of the given topic as a numerical value.
      - This is formatted as a floating point number.
    - `keywords`
      - This contains a listing of the top keywords that make up a topic.
      - This is formatted as a list of strings. Each string must be sanitized but keep a broad range of possible values due to equations being allowed in text.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/sample.txt"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "topics": [
      {
        "prevalence": 0.112,
        "keywords": ["MSOE", "student", "commitment", "learning", "value", "best", "engineering"]
      }
    ]
  }
}
```

</details>

#### Get Q&A

<details>
<summary>


</summary>
This command should be used to answer a question a user has about the contents of a lecture.

**_Topic:_**\
A request to answer a question from the content of a video transcript should be sent over the REST endpoint `fb/proc/qa`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file including the context lecture the question is about. This field should follow the constraints at the bottom of the document in the Username And File Path section.
- `question`
  - The question asked by the user about the lecture in the given file path

**_Response Payload Components:_**

- `score`
  - The score returned by the extractive model
  - This is a floating point number between 0-1
- `start`
  - The start index in the context transcript where the extractive model gets its answer
  - This is an integer
- `end`
  - The end index in the context transcript where the extractive models gets its answer
  - This is an integer
- `extractive_answer`
  - The answer generated by the extractive question-answering model
  - This is a base64 encoded string.
- `abstractive_answer`
  - The answer generated by the abstractive question-answering model
  - This is a base64 encoded string.       

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/khan1.txt",
    "question": "When did the Byzantine Empire end?"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
        "score": 0.7027844786643982,
        "start": 2142,
        "end": 2146,
        "extractive_answer": "MTQ1Mw==",
        "abstractive_answer": "VGhlIEJ5emFudGluZSBFbXBpcmUgZW5kZWQgaW4gMTQ1Mw=="
    }
}
```

</details>

#### [DEPRECATED] ~~Get Sentences By Keyword~~

<details>
<summary>


</summary>

[DEPRECATED] ~~This command should be used to generate a listing of sentences in a given document in the account backend. The returned sentences will be related to some keyword that is passed in to the command. The returned sentences should be ordered based on how important and or related they are to the keyword. This may be able to be evaluated using TextRank, LexRank, or LDA metrics.~~    


**_Topic:_**  
~~A request to get sentences from the video transcript by keyword should be sent over the REST endpoint `fb/proc/sentences`.~~ ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- ~~`path`: The file to generate sentences for. This field should follow the constraints at the bottom of the document in the Username And File Path section.~~
- ~~`keyword`~~
  - ~~This is the keyword to use to get sentences.~~
  - ~~This is formatted as a string. This input must be sanitized but has a broader range of possible values due to equations being allowed in text.~~
- ~~`num`~~
  - ~~The number of sentences to return that are associated with the given keyword. A value of -1, or a value that exceeds the total number of sentences, will return all sentences associated with the given keyword. All other positive values will return the specified number of most prevalent sentences.~~
  - ~~This is formatted as an integer.~~

**_Response Payload Components:_**

- ~~`sentences`~~
  - ~~This is a list of JSON objects. It contains a list of sentences and a measurement of how related they were to the given keyword. Each object should include the following:~~
    - ~~`prevalence`~~
      - ~~A numeric value representing the prevalence of how related the keyword and the sentence are.~~
      - ~~This is formatted as a floating point number~~
    - ~~`sentence`~~
      - ~~The sentence the keyword is related to. This is encoded as a base64.~~
      - ~~This is formatted as a string.~~

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/sample.txt",
    "keyword": "Lorem",
    "num": -1
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "sentences": [
      {
        "prevalence": 0.113,
        "sentence": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4="
      },
      {
        "prevalence": 0.101,
        "sentence": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4="
      },
      {
        "prevalence": 0.006,
        "sentence": "TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4="
      }
    ]
  }
}
```

</details>

#### Get Audio Transcription

<details>
<summary>


</summary>
This command should be used to generate a transcript of an audio file

**_Topic:_**\
A request to transcribe an audio file should be sent over the REST endpoint `fb/proc/transcribe`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file to attempt to transcribe. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `data`
  - This is the generated transcript, encoded in base64

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/audio/sample.wav"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
    "data": "VGhlIGJpcmNoIGNhbiB1c2UgbGlkIG9uIHRoaXMgc21vb3RoIHBsYW5rcy4gR2x1ZSB0aGUgc2hlZXQgdG8gdGhlIGRhcmsgYmx1ZSBiYWNrZ3JvdW5kLiBJdCBpcyBlYXN5IHRvIHRlbGwgdGhlIGRlcHRoIG9mIGEgd2VsbC4gVGhlc2UgZGF5cywgdGhlIGNoaWNrZW4gbGVnIGlzIGEgcmFyZSBkaXNoLiBSaWNlIGlzIG9mdGVuIHNlcnZlZCBpbiByb3VuZCBib3dscy4gVGhlIGp1aWNlIG9mIGxlbW9uIG1ha2VzIGZpbmUgcHVuY2guIFRoZSBib3ggd2FzIHRocm93biBiZXNpZGUgdGhlIHBvcmsgdHJ1Y2suIFRoZSBob2dzIHdlcmUgZmVkIGNob3BwZWQgY29ybiBhbmQgZ2FyYmFnZS4gRm91ciBob3VycyBvZiBzdGVhZHkgd29yayBmYWNlZCB1cy4gQSBsYXJnZSBzaXplIG9mIHN0b2NraW5ncyBpcyBoYXJkIHRvIHNlbGwu"
  }
}
```

</details>

#### Get Generated Questions

<details>
<summary>


</summary>
This command should be used to generate questions from a transcript document.

**_Topic:_**\
A request to generate questions about a transcript should be sent over the REST endpoint `fb/proc/qg`. ~~The response to this request should be sent back over the topic `bf/proc/cID`.~~

**_Request Payload Components:_**

- `path`: The file to generate questions about. This field should follow the constraints at the bottom of the document in the Username And File Path section.

**_Response Payload Components:_**

- `questions`
  - This is a list of the questions generated.
  - Each entry is a base64 encoded string.

**_Example Request Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "username": "DoeJ1970",
  "token": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "p": {
    "path": "user/texts/khan1.txt"
  }
}
```

**_Example Response Message:_**

```
{
  "ts": 1666818622000,
  "cId": "f81d4fae-7dec-11d0-a765-00a0c91e6bf6",
  "err": {"code": "0", "msg": ""},
  "p": {
	"questions": [
		"V2hhdCB3YXMgdGhlIEJ5emFudGluZSBFbXBpcmUgY29uc2lkZXJlZD8=",
		"V2hhdCBpcyB0aGUgbmFtZSBvZiB0aGUgQnl6YW50aW5lIEVtcGlyZT8=",
		"V2hhdCBpcyB0aGUgbmFtZSBvZiB0aGUgUm9tYW4gRW1waXJlPw==",
		"V2hhdCBkaWQgSGVyYWNsaXVzIG1ha2UgR3JlZWsgdGhlIG9mZmljaWFsIGxhbmd1YWdlPw=="
	]
  }
}
```

</details>

---

---

---

## Error Code List

<details>
<summary>


</summary>
This section lists out all of the error codes and their causes.

### General Error Codes

The errors in this section are general errors. These errors are usually caused as a result of invalid information or missing information in the request message body.

| Error Code | Cause of Error | Default Message |
|------------|----------------|-----------------|
| 0 | No Error | `""` |
| 1 | Missing Required Field | `"A required JSON key was missing from the request"` |
| 2 | Invalid Data Format | `"The input data does not match the expected type. Expected type <x>. Found type <y>"` |
| 3 | Invalid Data Input | `"The value for the input data was different from expected. <description>"` |
| 4 | Invalid Login Information | `"The username and/or password used to login to the account is incorrect."` |
| 5 | Invalid Login Token | `"The login token does not match the expected username or it has expired. Please sign out and login again."` |
| 6 | Password Changed | `"The password you are attempting to use has been changed. Please sign in with the new password."` |
| 7 | Unsupported Device | `"The browser and/or the device you are attempting to access the application from is not supported. Please switch browsers and try again."` |
| 8 | Invalid Time | `"The user device time in the request message exceeds the server time. Please make sure your clock is set correctly and try again."` |
| 9 | Account Locked | `"The specified account has been locked. Too many failed login attempts."` |
| 10 | Account Does Not Exist | `"No account with the specified username was found in the system."` |
| 11 | Invalid Filepath | `"The specified file at <location> does not exist."` |
| 12 | Out of Space | `"There is not enough space in the user's account to perform this operation. Required size <size> bytes. Available space <size> bytes. Please clear some files to make space or consider <action>."` |
| 13 | Download Failed | `"The download operation failed for <amount> files. This could be due to a permissions error with your browser."` |
| 14 | File Modification Failed | `"The specified file could not be modified/deleted. This could be due to another operation modifying this file still. Please wait a moment and retry."` |
| 15 | User Create Failed | `"The specified user could not be created"` |
| 16 | Device Logout Failed | `"Failed to logout from all devices. Attempted <amount> Failed <amount>."` |
| 17 | Size Limit Exceeded | `"The response message exceeds the size limit allowed. Please shorten the amount of requested data and retry."` |
| 18 | History Deletion Failed | `"Deletion of account device history failed for <reasons>. Please try again."` |
| 19 | Information Retrieval Failed | `"Failed to acquire all of the account information."` |
| 20 | Connected Devices Not Found | `"Failed to find all connected devices."` |
| 21 | Path Too Long Error | `"The file path is too long. Please rename files and directories to be shorter."` |
| 22 | Username Invalid Error | `"The specified user does not currently have any sessions in the system. This means they are not logged in anywhere."` |
| 23 | Token Invalid Error | `"The specified token is not valid for the specified user. This means you are not authenticated. Please sign out and sign back in before trying again."` |
| 24 | General Error | `"<Explanation>"` |
| 25 | Too Many Connections Error | `"Login failed. The specified account already has the maximum number of concurrent sessions active."` |
| 26 | Incorrect Username or Password | `"The username or password did not match"` |


### PROG Error Codes

The errors in this section are PROG errors. PROG errors are errors caused by the programmer. These are errors in the logic and or processing steps and as such are deemed unavoidable by the user if these do occur. As such, the messages for these errors should include information about the file and line number that the error occurred at as well as a notice to contact the developers with a redirect to a contact information page.

| Error Code | Cause of Error | Default Message |
|------------|----------------|-----------------|
| 501 | PROG Preprocessing Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 502 | PROG Transcription Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 503 | PROG Summarization Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 504 | PROG Topic Generation Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 505 | PROG Question Generation Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 506 | PROG Sentence Generation Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |
| 507 | PROG General Error | `"Programmer Error Occurred. <encoded location information>. Please contact developers with the above error code and message."` |

</details>

 --- --- ---

## Supported File Extensions

<details>
<summary>


</summary>
This section lists out the file types that are supported by the upload function. It will also list the expected behavior upon uploading each type of file.

| File Extension | Type Name | Behavior |
|----------------|-----------|----------|
| `.txt` | Text File | Stored with metadata in JSON |
| `.vtt` | Microsoft Teams Transcript File | Extracts text by removing speaker and timestamp tags. Stored with metadata in JSON |
| `.*` | Other | Stored as raw bytes (no metadata JSON) |

</details>

---

---

---

## Endpoint List

<details>
<summary>


</summary>
This section lists out all of the topic endpoints in the above sections with their names in a simple table.

| Topic Endpoint | Topic Name |
|----------------|------------|
| `fb/auth/new` | Create new user |
| `fb/auth/in` | Login user |
| `fb/auth/out` | Logout user for one or all clients |
| `fb/auth/exchange` | Password Reset |
| ~~`bf/auth/cID`~~ | ~~Authorization Topic Responses~~ |
| `fb/acc/list` | Get device history list |
| `fb/acc/clear` | Clear device history list |
| `fb/acc/connected` | Get Connected Concurrent Users List |
| `fb/acc/max` | Set Maximum Concurrent Users |
| `fb/acc/info` | Get stored information for user |
| `fb/acc/delete` | Delete current user account |
| ~~`bf/acc/cID`~~ | ~~Account Management Topic Responses~~ |
| `fb/file/up` | Upload Files |
| `fb/file/down` | Download Files |
| `fb/file/space` | Get Account Storage Space Size |
| `fb/file/list` | List User Files |
| `fb/file/remove` | Delete Files |
| ~~`bf/file/cID`~~ | ~~File Management Topic Responses~~ |
| ~~`fb/proc/data`~~ | ~~Get File Text Data~~ |
| `fb/proc/clean` | Preprocess and clean a file |
| `fb/proc/summary` | Get summary of file text data |
| `fb/proc/topics` | Get topics and keywords in file text data |
| `fb/proc/qa` | Get questions and answers from file text data |
| `fb/proc/sentences` | Get sentences by keyword from file text data |
| `fb/proc/transcribe` | Generate transcript of audio file |
| ~~`bf/proc/cID`~~ | ~~File Processing Topic Responses~~ |

</details>

---

---

---

## Object Store File Format

<details>
<summary>


</summary>
This section describes the format used to store user uploaded files in the backend. Files will likely be stored in an object store.

User text-based files are to be uploaded as JSON objects as a part of the `fb/file/up` endpoint. The endpoint currently supports uploading of `.txt` and `.vtt` files. If a VTT file is uploaded, the timestamp and speaker tags will be automatically removed and only the raw text will be stored as specified below.

This endpoint contains options to preprocess files. Because we do not want to have files preprocessed multiple times we need to record this information. Hence the need for a special format. The entire JSON file object should be converted to a string and then base64 encoded. The file data will be stored as JSON with the below components:

- `filename`
  - This is the name of the file that was uploaded to the backend. It does not contain the file extension.
  - This is formatted as a string. This string should not include forbidden ASCII characters such as less than, greater thn, colon, double quote, pipes, question marks, asterisks, null bytes, or other control characters.
- `original_extension`
  - This is the original file extension associated with the file when it was uploaded.
  - This is formatted as a string. It should be sanitized to only contain alphanumerics, periods, underscores, and hyphens.
- `processed`
  - This is a flag denoting if the text data for the file has been run through the preprocessor or not yet.
  - This is a boolean variable. A value of `true` deontes the text being processed already.
- `text`
  - This is the text data for the file.
  - This text likely needs to be sanitized.

**_Example File Before Encoding:_**

```
{
	"filename": "sample_raw",
	"original_extension": "txt",
	"processed": false,
	"text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
}
```

**_Example File After Encoding:_**

```
ew0KCSJmaWxlbmFtZSI6ICJzYW1wbGVfcmF3IiwNCgkib3JpZ2luYWxfZXh0ZW5zaW9uIjogInR4dCIsDQoJInByb2Nlc3NlZCI6IGZhbHNlLA0KCSJ0ZXh0IjogIkxvcmVtIGlwc3VtIGRvbG9yIHNpdCBhbWV0LCBjb25zZWN0ZXR1ciBhZGlwaXNjaW5nIGVsaXQsIHNlZCBkbyBlaXVzbW9kIHRlbXBvciBpbmNpZGlkdW50IHV0IGxhYm9yZSBldCBkb2xvcmUgbWFnbmEgYWxpcXVhLiINCn0=
```
  
**_Non Text Files_**  
Non text-based files such as audio, video, or images, can also be uploaded through this endpoint. These will simply be put in the object store as raw bytes - it is *not* stored in a JSON with additional metadata. Currently, it only makes sense to upload audio files (the audio transcriber can handle `.mp3` and `.wav` files). While it is technically possible to upload any file type, there would not be much use in doing so.

</details>

---

---

---

## Usernames And File Paths

<details>
<summary>


</summary>
This section describes how both usernames, and file paths, are formatted. These are both under this same section as the file path is closely related to the username. As such this section will describe how the two interact.

`username`:\
The username field serves two purposes. The primary purpose is for account identification. This means that it must be able to be used to login to the account. The secondary purpose is for file identification. Every uploaded file should be associated with a specific user. We do not want to allow users to access eachothers documents. This means that every user will have their own directory in the backend. These directories will be generated and named based on the username.

The two purposes of usernames, as defined above, lead to a set of constraints on the username field.

1. The username must be formatted as a string.
2. The username must not include characters that are forbidden from paths in any language. This includes ASCII characters such as less than, greater than, colon, double quote, pipes, question marks, asterisks, null bytes, and other ASCII control characters. See [this stack overflow post](https://stackoverflow.com/a/31976060) for further details. This means that usernames should likely be locked to only alphanumerics, spaces, and hyphens.
3. Usernames must be unique.
4. Usernames must have a maximum length of 32 characters. This is in order to not exceed path limits on certain operating systems.
5. Usernames must be case specific. This is to prevent running out of possible usernames as defined by their uniqueness.

`path`:\
The file path field primarily serves one purpose. To find and identify files in the backend object store. Due to the backend being an object store we can use the path to simulate folders.

The simulation of folders based on file paths, when combined with the username constraints, lead to a number of constraints for the path field.

1. Paths must be uniqe. Only one file can exist at a single file path. Due to the simulation of directories a path can point to a directory which 'contains' multiple files though. In reality this is more akin to performing a 'starts_with(path)' comparison against the files in the object store.
2. The path cannot include characters that are forbidden from paths or filenames in any language. This includes ASCII characters such as less than, greater than, colon, double quote, pipes, question marks, asterisks, null bytes, and other ASCII control characters. See [this stack overflow post](https://stackoverflow.com/a/31976060) for further details.
3. Paths cannot contain '.', '..', or symbolic links. This is because we want to prevent navigation of the file system based on relative pathing.
4. Paths can contain '/'. A '/' character is used to denote another layer of directories.
5. Paths will always be based off of the associated username folder. For example, if a file were to be uploaded to `texts/sample.txt` the file would actually be placed at `<username>/texts/sample.txt`.
6. Paths have a total size limit of 230 characters.
7. Paths pointing to files should be formatted as `<directories>/<file name>.<file extension>`. There can be multiple directories defined such as `users/texts/english`. This would simulate a 'users' folder. That folder would then contain a folder called 'texts' which would in turn contain a folder called 'english'.

</details>

---

---

---

## UUIDs

<details>
<summary>


</summary>

UUIDs are commonly used in this project for the `cID` and `token` fields. Any UUID in this project should be formatted as a string. It should be populated with a [RFC version 4 UUID](https://www.rfc-editor.org/rfc/rfc4122.html). We are using a RFC version 4 UUID so it generates a mostly random sequence. This will be fast, secure, and more than enough for our purposes.

</details>

---

---

---
