# BaseRepository
The `BaseRepository` class is a generic repository that provides default methods for Create, Read, Update, and Delete (CRUD) operations. It works with any SQLModel model and an asynchronous database session.

::: fastapi_async_sql.repositories.BaseRepository
    options:
        show_root_heading: true
        merge_init_into_class: false
        group_by_category: false
        members:
          - __init__
          - get
          - get_by_ids
          - get_count
          - get_multi
          - get_multi_paginated
          - create
          - update
          - remove
