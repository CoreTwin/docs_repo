[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# Authentication API

## Overview

The authentication system provides secure user registration, login, and JWT token management for the CoreTwin Platform.

## Endpoints

### POST /api/v1/auth/register

Register a new user account.

**Request Body:**
```json
{
  "email": "user@example.com",
  "full_name": "John Doe",
  "password": "secure_password",
  "phone": "+1234567890",
  "position": "Software Engineer"
}
```

**Response (201 Created):**
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
- `400 Bad Request` - Validation error or email already exists
- `422 Unprocessable Entity` - Invalid request data

### POST /api/v1/auth/login

Authenticate user and receive JWT tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "secure_password"
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

**Error Responses:**
- `401 Unauthorized` - Invalid credentials
- `422 Unprocessable Entity` - Invalid request data

### POST /api/v1/auth/refresh

Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```

**Response (200 OK):**
```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 1800
}
```

**Error Responses:**
- `401 Unauthorized` - Invalid or expired refresh token

### GET /api/v1/auth/me

Get current authenticated user information.

**Headers:**
```
Authorization: Bearer <access_token>
```

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

### POST /api/v1/auth/change-password

Change user password.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "current_password": "old_password",
  "new_password": "new_secure_password"
}
```

**Response (200 OK):**
```json
{
  "message": "Password changed successfully"
}
```

**Error Responses:**
- `400 Bad Request` - Current password is incorrect
- `401 Unauthorized` - Invalid or missing token
- `422 Unprocessable Entity` - Invalid request data

### POST /api/v1/auth/logout

Logout user (invalidate tokens).

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
{
  "message": "Successfully logged out"
}
```

## Authentication Flow

1. **Registration**: User creates account with email and password
2. **Login**: User authenticates and receives access/refresh tokens
3. **API Access**: Include access token in Authorization header for protected endpoints
4. **Token Refresh**: Use refresh token to get new access token when expired
5. **Logout**: Invalidate tokens when user logs out

## Security Features

- **Password Hashing**: Uses bcrypt for secure password storage
- **JWT Tokens**: Stateless authentication with configurable expiration
- **Token Refresh**: Separate refresh tokens for enhanced security
- **Input Validation**: Comprehensive validation using Pydantic schemas
- **Error Logging**: Structured logging with authentication error categorization

## Related Documentation

- [User Management API](users.md)
- [Security Architecture](../architecture/security.md)
- [Development Setup](../development/setup.md)
