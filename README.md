# 📌 API for a Link Shortener Website with Registration and Authorization

## 🔐 User Registration and Profile

### Features:
- User registration
- Authorization and authentication
- Profile updates:
  - Username
  - Email
  - Name
  - Password
- Account deletion

## 🔗 Link Creation

### For authorized users:
- Custom short link creation
- Creating a chat linked to the short link

### For all users (including unauthorized):
- Creating a link with a random code

## 💬 Chat Linked to a Short Link

### Each message displays:
- Timestamp
- Author name
- Delete message
- Edit message

## 🧹 Link Management

### Only for authorized users:
- Delete a specific link
- Bulk delete all links
- Delete user account

<!-- DOCS_START -->
# 📘 API Documentation

**Title:** FastAPI

**Version:** 0.1.4

**Description:** This is a API for creating and managing short links.

---

## `GET /{short_code}`

**Summary:** Get Original Link

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| short_code | path | string | Yes |  |

**Responses:**

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **url_origin** (N/A) **(required)**: Url Origin

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error


---

## `POST /short`

**Summary:** Create Short Link

**Request Body:**

Content-Type: `application/json`

- **url_origin** (string) **(required)**: Url Origin

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **url_short** (N/A) **(required)**: Url Short

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `GET /user/check-username`

**Summary:** Check Username

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| username | query | string | Yes |  |

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **msg** (string) **(required)**: Msg
    - **exist** (boolean) **(required)**: Exist

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `GET /user/check-email`

**Summary:** Check Email

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| email | query | string | Yes |  |

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **msg** (string) **(required)**: Msg
    - **exist** (boolean) **(required)**: Exist

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/reg`

**Summary:** Create User

**Request Body:**

Content-Type: `application/json`

- **name** (string) **(required)**: Name
- **email** (string) **(required)**: Email
- **username** (string) **(required)**: Username
- **password** (string) **(required)**: Password

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message
    - **access_token** (string) **(required)**: Access Token

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/login`

**Summary:** Login User

**Request Body:**

Content-Type: `application/json`

- **email_or_username** (string) **(required)**: Email Or Username
- **password** (string) **(required)**: Password

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message
    - **access_token** (string) **(required)**: Access Token

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/logout`

**Summary:** Logout User

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message


---

## `POST /user/logout-all`

**Summary:** Logout All User

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message


---

## `POST /user/change-password`

**Summary:** Change Password

**Request Body:**

Content-Type: `application/json`

- **old_password** (string) **(required)**: Old Password
- **new_password** (string) **(required)**: New Password

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/change-username`

**Summary:** Change Username

**Request Body:**

Content-Type: `application/json`

- **username** (string) **(required)**: Username

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message
    - **access_token** (string) **(required)**: Access Token

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/change-email`

**Summary:** Change Email

**Request Body:**

Content-Type: `application/json`

- **email** (string) **(required)**: Email

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/change-name`

**Summary:** Change Name

**Request Body:**

Content-Type: `application/json`

- **name** (string) **(required)**: Name

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/refresh-tokens`

**Summary:** Refresh Tokens

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message
    - **access_token** (string) **(required)**: Access Token


---

## `POST /user/create-link`

**Summary:** Create Link

**Request Body:**

Content-Type: `application/json`

- **alias** (N/A) : Alias
- **original_url** (string) **(required)**: Original Url
- **has_room** (N/A) : Has Room

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **url_short** (string) **(required)**: Url Short
    - **short_code** (string) **(required)**: Short Code
    - **web_socket** (N/A) : Web Socket

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /user/my-links`

**Summary:** Get All Links

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - Array of:
      - **url_short** (string) **(required)**: Url Short
      - **link** (string) **(required)**: Link


---

## `DELETE /user/link/{identifier}`

**Summary:** Delete Link

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| identifier | path | string | Yes |  |

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `DELETE /user/links`

**Summary:** Delete Links

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message


---

## `DELETE /user/`

**Summary:** Delete User

**Responses:**

- **HTTP 401**: Unauthorized
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Authorization token missing || Invalid or expired token 

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **username** (string) : Username
    - **message** (N/A) : Message


---

## `DELETE /m/{room_id}/{message_id}`

**Summary:** Delete Message

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| message_id | path | string | Yes |  |
| room_id | path | string | Yes |  |
| user_id | query | string | No |  |

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **message** (N/A) **(required)**: Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `POST /m/{room_id}/{message_id}`

**Summary:** Change Message

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| message_id | path | string | Yes |  |
| room_id | path | string | Yes |  |
| new_content | query | string | Yes |  |
| user_id | query | string | No |  |

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - **message** (N/A) **(required)**: Message

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---

## `GET /m/{room_id}`

**Summary:** Get History Of Chat

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| room_id | path | string | Yes |  |
| first_date | query | string | Yes |  |
| last_date | query | string | Yes |  |

**Responses:**

- **HTTP 500**: Internal Server Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : Internal Server Error

- **HTTP 400**: Bad request
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (string) : This is BAD REQUEST

- **HTTP 200**: Successful Response
  - **Content-Type**: `application/json`
  **Schema**:
    - Array of:
      - **id** (N/A) **(required)**: Id
      - **content** (N/A) **(required)**: Content
      - **sender** (N/A) **(required)**: Sender
      - **created_at** (N/A) **(required)**: Created At

- **HTTP 422**: Validation Error
  - **Content-Type**: `application/json`
  **Schema**:
    - **detail** (array) : Detail
      - Array items:
        - **loc** (array) **(required)**: Location
          - Array items:
        - **msg** (string) **(required)**: Message
        - **type** (string) **(required)**: Error Type


---


<!-- DOCS_END -->