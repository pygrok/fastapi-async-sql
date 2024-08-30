# AsyncSQLModelMiddleware
The `AsyncSQLModelMiddleware` class is a FastAPI middleware that provides an asynchronous SQLModel session (`AsyncSession`) for each request. It ensures that each request has a database session available via `request.state.db`.

::: fastapi_async_sql.middlewares.AsyncSQLModelMiddleware
    options:
        show_root_heading: true
        merge_init_into_class: false
        group_by_category: false
        members:
          - __init__
          - dispatch
