[Домой](../README.md) | [Назад](../content/Description_for_agents.md)

# Companies API

## Overview

The companies API provides functionality for managing company information and organizational structures in the CoreTwin Platform.

## Endpoints

### GET /api/v1/companies/

Get list of companies.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response (200 OK):**
```json
[
  {
    "id": "uuid",
    "name": "Example Corp",
    "description": "A leading technology company",
    "industry": "Technology",
    "size": "large",
    "website": "https://example.com",
    "is_active": true,
    "created_at": "2025-06-27T14:17:00Z"
  }
]
```

**Error Responses:**
- `401 Unauthorized` - Invalid or missing token

### POST /api/v1/companies/

Create a new company.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Request Body:**
```json
{
  "name": "New Company",
  "description": "Company description",
  "industry": "Technology",
  "size": "medium",
  "website": "https://newcompany.com"
}
```

**Response (201 Created):**
```json
{
  "id": "uuid",
  "name": "New Company",
  "description": "Company description",
  "industry": "Technology",
  "size": "medium",
  "website": "https://newcompany.com",
  "is_active": true,
  "created_at": "2025-06-27T14:17:00Z"
}
```

## Related Documentation

- [Authentication API](authentication.md)
- [Users API](users.md)
- [Development Setup](../development/setup.md)
