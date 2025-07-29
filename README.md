# User Registration API with Duplicate Prevention

## Task Overview
A SaaS platform is launching a user registration service to onboard new customers. However, the current implementation allows users to register multiple accounts using the same email address, resulting in duplicate records and potential data integrity issues. The goal is to ensure that the registration system prevents duplicate user entries and provides clear feedback when a user attempts to register with an existing email. This is critical for maintaining a clean user database and delivering a reliable onboarding experience.

## Guidance
- The project uses FastAPI for building RESTful APIs and PostgreSQL for persistent data storage.
- User registration should validate input using Pydantic models and handle all database interactions asynchronously.
- Apply a unique constraint on the email field at the database level to enforce uniqueness.
- Implement error handling so that duplicate registration attempts return a clear and meaningful error response instead of a generic server error.
- Ensure environment variables are used for database credentials and that the system is containerized using Docker and Docker Compose for reproducibility.
- Maintain clear code structure by separating routers, models, services, and database/session management for better maintainability and readability.

## Objectives
- Implement a user registration endpoint that creates new users in the PostgreSQL database.
- Prevent duplicate user entries by enforcing a unique email constraint in both the database schema and application logic.
- Return appropriate HTTP responses: 201 on success, and 400 with a clear error message when a duplicate email is submitted.
- Use Pydantic models to validate registration input and serialize output.
- Ensure all database operations are asynchronous and properly managed via dependency injection.
- Containerize the backend application using Docker, with a separate service for the PostgreSQL database.

## How to Verify
- Attempt to register a new user with a unique email address and confirm a successful response is returned and the record is created in the database.
- Submit another registration request using the same email and verify that the API returns a 400 response with a clear error message about the duplicate entry.
- Check that the users table in PostgreSQL does not contain multiple records with the same email.
- Confirm the API service starts correctly, connects to the PostgreSQL database, and that all environment variables are respected.
- Review the API documentation (OpenAPI) to see the registration endpoint and its expected inputs/outputs.
