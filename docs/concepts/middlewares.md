# Middlewares

This module provides middleware for integrating SQLModel with FastAPI using asynchronous SQLAlchemy sessions. The main class in this module is `AsyncSQLModelMiddleware`.

## `AsyncSQLModelMiddleware`
??? api "API Documentation"

    [fastapi_async_sql.middlewares.AsyncSQLModelMiddleware](../api_doc/async_sql_model_middleware.md)
The `AsyncSQLModelMiddleware` class is a FastAPI middleware that provides an asynchronous SQLModel session (`AsyncSession`) for each request.
It ensures that each request has a database session available via `request.state.db`.

### Usage Example
Here’s how you can integrate `AsyncSQLModelMiddleware` into your FastAPI application:


```python hl_lines="15 25-26 34"
{!./docs_src/middlewares/middleware.py!}
```

### How It Works
1. Initialization: The middleware is initialized with either a db_url or a custom_engine. It creates an async engine and an async session maker bound to the engine.
2. Request Handling: During request handling, the middleware creates an async session and attaches it to the request.state.db. This session is used throughout the request and is automatically disposed of after the request is processed.
3. Dependency Injection: You can access the session in your route handlers by extracting it from request.state.db using FastAPI's dependency injection system.

### Example Configuration
To use `AsyncSQLModelMiddleware`, you can either pass a database URL or a custom SQLAlchemy async engine. Here’s an example configuration:

```python hl_lines="11 15"
{!./docs_src/middlewares/main.py!}
```

With this setup, every request will have access to an async SQLAlchemy session, making it easy to interact with your database using SQLModel in an async manner.
