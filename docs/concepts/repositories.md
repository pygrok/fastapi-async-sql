# Repositories

The `repositories` module in the `fastapi-async-sql` package provides a generic repository pattern implementation to simplify CRUD operations for SQLModel models in FastAPI applications. This module abstracts common database operations, allowing developers to focus on business logic rather than repetitive CRUD operations.

## BaseRepository
??? api "API Documentation"

    [fastapi_async_sql.repositories.BaseRepository](../api_doc/base_repository.md)

The `BaseRepository` class is a generic repository that provides default methods for Create, Read, Update, and Delete (CRUD) operations. It works with any SQLModel model and an asynchronous database session.


### Example Usage

Here’s an example of how to use the `BaseRepository` in a FastAPI application:
#### Create SQLModel models
The first step is to define your SQLModel models. These models represent the tables in your database and define the structure of your data.
```python
# Code above omitted 👆

{!./docs_src/repositories/repository.py[ln:7]!}


{!./docs_src/repositories/repository.py[ln:15-19]!}

# Code below omitted 👇
```
/// details | 👀 Full file preview
```python

{!./docs_src/repositories/repository.py!}
```
///

#### Create schemas (data models)
Next, create Pydantic schemas to validate and serialize your data. These schemas define the structure of the data that will be sent to and received from your FastAPI endpoints.
```python
# Code above omitted 👆

{!./docs_src/repositories/repository.py[ln:22-30]!}

# Code below omitted 👇
```
/// details | 👀 Full file preview
```python

{!./docs_src/repositories/repository.py!}
```
///

#### Create a repository
Finally, create a repository for your model by extending the `BaseRepository` class. This repository will handle all the CRUD operations for your model.
```python
# Code above omitted 👆

{!./docs_src/repositories/repository.py[ln:33-35]!}

# Code below omitted 👇
```
/// details | 👀 Full file preview
```python

{!./docs_src/repositories/repository.py!}
```
///

#### Create a dependency
To use the repository in your FastAPI application, you can create a dependency that initializes the repository with the database session.
```python
# Code above omitted 👆

{!./docs_src/repositories/repository.py[ln:37-41]!}

# Code below omitted 👇
```

/// details | 👀 Full file preview
```python

{!./docs_src/repositories/repository.py!}
```
///

#### Use the repository
You can now use the repository in your FastAPI application to interact with your database. The repository provides methods for creating, reading, updating, and deleting objects in the database.
```python
# Code above omitted 👆

{!./docs_src/repositories/repository.py[ln:44-]!}

```
/// details | 👀 Full file preview
```python

{!./docs_src/repositories/repository.py!}
```
///

## Exception Handling

The `repositories` module makes use of custom exceptions to handle specific error scenarios:

- `CreateObjectError`: Raised when there is an error creating an object in the database.
- `ObjectNotFoundError`: Raised when an object is not found in the database by its primary key.

These exceptions help provide more meaningful error messages and make it easier to debug issues in your application.

## Filtering and Pagination

The `get_multi` and `get_multi_paginated` methods support filtering and pagination through the `Filter` and `Params` classes, respectively. These features make it easier to manage large datasets and retrieve only the data you need.

## Additional resources
- [SQLModel documentation](https://sqlmodel.tiangolo.com/tutorial/fastapi/multiple-models/)
- [Pydantic documentation](https://docs.pydantic.dev/latest/)
- [FastAPI documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/)
- [FastAPI Pagination documentation](https://uriyyo-fastapi-pagination.netlify.app/)
- [FastAPI Filter documentation](https://fastapi-filter.netlify.app/)