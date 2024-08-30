# Models

The `models` module in the `fastapi-async-sql` package provides base classes that can be used to create SQLAlchemy models with asynchronous support in FastAPI applications.

These base classes include functionality for automatic table naming, timestamp fields, and UUID-based primary keys.

## Base Classes

### `BaseSQLModel`
??? api "API Documentation"

    [fastapi_async_sql.models.BaseSQLModel](../api_doc/base_sql_model.md)

The `BaseSQLModel` class is a base model that extends SQLModel and adds asynchronous capabilities via SQLAlchemy's `AsyncAttrs`.

It automatically generates the table name based on the class name and provides a configuration that supports camelCase aliasing, assignment validation, and strict field handling.

#### Example Usage

```python
{!./docs_src/models/model.py!}
```

#### Features
- Automatic Table Naming: The table name is automatically generated from the class name and converted to snake_case plural form.
- Pydantic Configuration: Configured to use camelCase for JSON serialization, validate field assignments, populate fields by name, and forbid extra fields.

#### How It Works
- Table Naming: The `__tablename__` attribute is generated using the `to_snake_plural` function, which converts the class name from PascalCase to snake_case and pluralizes it. For example, a class named Item would have a table name items.
- Pydantic Config: The `model_config` attribute defines how the model behaves with Pydantic, ensuring proper aliasing and validation.

### `BaseTimestampModel`
??? api "API Documentation"

    [fastapi_async_sql.models.BaseTimestampModel](../api_doc/base_timestamp_model.md)

The `BaseTimestampModel` class is a mixin that adds `created_at` and `updated_at` timestamp fields to your models. These fields are automatically populated with the current UTC time when a record is created or updated.
#### Example Usage
```python
{!./docs_src/models/timestamp_model.py!}
```
#### Features
- Automatically populates the `created_at` field with the current UTC time when a record is created.
- Automatically updates the `updated_at` field with the current UTC time when a record is updated.

#### How It Works
- `created_at`: Uses `default_factory` to set the current UTC time when the record is created.
- `updated_at`: Uses onupdate to set the current UTC time whenever the record is updated. If the record is not updated, the field remains None.

### `BaseUUIDModel`
??? api "API Documentation"

    [fastapi_async_sql.models.BaseUUIDModel](../api_doc/base_uuid_model.md)

The `BaseUUIDModel` class is a mixin that adds a UUID-based primary key field to your models. This field is automatically populated with a UUID4 value when a record is created.

#### Example Usage

```python
{!./docs_src/models/uuid_model.py!}
```

#### Features
- Automatically generates a UUID4 value for the `id` field when a record is created.
- Ensures that each record has a unique UUID as the primary key.

#### How It Works
- `UUID Generation`: The `id` field is set to use the `uuid4` function as the default value, ensuring a unique UUID is generated for each record.


## Combining Base Classes
You can combine the base classes to create models with multiple features. For example, you can create a model with both timestamp fields and a UUID-based primary key.

### Example Usage
```python
{!./docs_src/models/combined_model.py!}
```

### Features
This model would have the following features:

- Automatic table naming based on the class name.
- CamelCase aliasing and field validation.
- `created_at` and `updated_at` timestamp fields.
- `id` primary key field with UUID4 values.
- Automatic population of timestamp and UUID fields on record creation.
- Proper JSON serialization and validation behavior.
- Strict field handling and aliasing.

## Using Models with `AsyncAttrs` to Prevent Implicit I/O

### Understanding Implicit I/O

In asynchronous applications, it's crucial to avoid implicit I/O operations, especially when working with SQLAlchemy's ORM and lazy-loading relationships. Implicit I/O can occur when you access relationship attributes or deferred columns that haven't been loaded yet. Under traditional asyncio, accessing these attributes directly can lead to errors because the I/O operation needed to fetch the data is not allowed to occur implicitly.

### What is `AsyncAttrs`?

`AsyncAttrs` is a mixin provided by SQLAlchemy that helps manage these situations by enabling attributes to be accessed in an awaitable manner. When you use `AsyncAttrs`, any attribute that might trigger a lazy load or deferred column access can be accessed using the `awaitable_attrs` attribute. This ensures that any required I/O operation is explicitly awaited, thus avoiding implicit I/O errors.

### How to Use `AsyncAttrs` in `fastapi-async-sql`

The `BaseSQLModel` class in `fastapi-async-sql` includes the `AsyncAttrs` mixin, which makes it easy to work with asynchronous I/O when using SQLModel.

Here’s how you can use it:

1. **Define your Models**: Your models should inherit from `BaseSQLModel`, which already includes the `AsyncAttrs` mixin.

2. **Access Relationships**: When accessing a relationship attribute that is lazy-loaded, use the `awaitable_attrs` accessor to explicitly await the attribute.

#### Example Usage

```python hl_lines="31"
{!./docs_src/models/async_attrs_model.py!}
```

## Utility Functions
The models module relies on utility functions to handle string conversions and pluralization. These functions are used to generate table names and convert between different naming conventions.

- `to_camel`: Converts a string from snake_case to camelCase.
- `to_snake_plural`: Converts a string from PascalCase to snake_case plural form.
