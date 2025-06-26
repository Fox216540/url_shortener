# url_shortener
Url shortener

<!-- DOCS_START -->
# 📘 API Documentation

**Title:** FastAPI

**Version:** 0.1.0

**Description:** 

---

## `GET /{short_code}`

**Summary:** Ge Original Link

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| short_code | path | string | True |  |

**Responses:**

- **200**: Successful Response
- **404**: Bad request
- **422**: Validation Error
- **500**: Internal Server Error
---

## `POST /short`

**Summary:** Create Short Link

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `GET /user/check-username`

**Summary:** Check Username

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| username | query | string | True |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `GET /user/check-email`

**Summary:** Check Email

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| email | query | string | True |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/reg`

**Summary:** Create User

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/login`

**Summary:** Login User

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/logout`

**Summary:** Logout User

**Responses:**

- **200**: Successful Response
---

## `POST /user/logout_all`

**Summary:** Logout All User

**Responses:**

- **200**: Successful Response
---

## `POST /user/change-password`

**Summary:** Change Password

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/change-username`

**Summary:** Change Username

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/change-email`

**Summary:** Change Email

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/change-name`

**Summary:** Change Name

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/refresh-tokens`

**Summary:** Refresh Tokens

**Responses:**

- **200**: Successful Response
---

## `POST /user/create-link`

**Summary:** Create Link

**Request Body:**

Content-Type: `application/json`


**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /user/my-links`

**Summary:** Get All Links

**Responses:**

- **200**: Successful Response
---

## `DELETE /user/link/{identifier}`

**Summary:** Delete Link

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| identifier | path | string | True |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `DELETE /user/links`

**Summary:** Delete Links

**Responses:**

- **200**: Successful Response
---

## `DELETE /user/`

**Summary:** Delete User

**Responses:**

- **200**: Successful Response
---

## `DELETE /m/{room_id}/{message_id}`

**Summary:** Delete Message

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| message_id | path | string | True |  |
| room_id | path | string | True |  |
| user_id | query | string | False |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `POST /m/{room_id}/{message_id}`

**Summary:** Change Message

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| message_id | path | string | True |  |
| room_id | path | string | True |  |
| new_content | query | string | True |  |
| user_id | query | string | False |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---

## `GET /m/{room_id}`

**Summary:** Get History Of Chat

**Parameters:**

| Name | In | Type | Required | Description |
|------|----|------|----------|-------------|
| room_id | path | string | True |  |
| first_date | query | string | True |  |
| last_date | query | string | True |  |

**Responses:**

- **200**: Successful Response
- **422**: Validation Error
---


<!-- DOCS_END -->
