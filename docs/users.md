# Users API

## Overview

The users API provides functionality for managing user accounts and profiles in the CoreTwin Platform.

## Endpoints

### GET /api/v1/users/

Get list of all users (admin only).

**Headers:**
```
Authorization: Bearer <admin_access_token>
```

**Query Parameters:**
- `skip` (optional): Number of records to skip (default: 0)
- `limit` (optional): Maximum number of records to return (default: 100)

**Response (200 OK):**
```json
[
  {
    "id": "uuid",
    "email": "user1@example.com",
    "full_name": "John Doe",
    "phone": "+1234567890",
    "position": "Software Engineer",
    "is_active": true,
    "is_admin": false,
    "created_at": "2025-06-27T14:17:00Z"
  }
]
```

**Error Responses:**
- `401 Unauthorized` - Invalid or missing token
- `403 Forbidden` - User is not admin

### GET /api/v1/users/{user_id}

Get specific user information.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Path Parameters:**
- `user_id`: UUID of the user

**Response (200 OK):**
```json
{
  "id": "uuid",
  "email": "user@example.com",
  "full_name": "John Doe",
  "phone": "+1234567890",
  "position": "Software Engineer",
  "is_active": true,
  "is_admin": false,
  "created_at": "2025-06-27T14:17:00Z"
}
```

**Error Responses:**
- `401 Unauthorized` - Invalid or missing token
- `403 Forbidden` - User can only access their own profile (unless admin)
- `404 Not Found` - User not found

## Related Documentation

- [Authentication API](authentication.md)
- [Companies API](companies.md)
- [Security Architecture](../architecture/security.md)
- [Development Setup](../development/setup.md)
