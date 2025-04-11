"""Tests for models."""

from datetime import timezone
from uuid import uuid4

import pytest
import sqlalchemy as sa
from sqlmodel import Session

from .models.hero_model import Hero
from .models.item_model import Item
from .models.team_model import Team


async def test_create_hero(db: Session, team: Team, item: Item):
    """Test creating a hero."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    assert hero.id is not None
    assert hero.created_at is not None
    assert hero.updated_at is None


async def test_create_team(db: Session):
    """Test creating a team."""
    team = Team(name="Test Team", headquarters="Test HQ")
    db.add(team)
    await db.commit()
    await db.refresh(team)
    assert team.id is not None
    assert team.created_at is not None
    assert team.updated_at is None


async def test_create_item(db: Session):
    """Test creating an item."""
    item = Item(name="Test Item", created_by_id=uuid4())
    db.add(item)
    await db.commit()
    await db.refresh(item)
    assert item.id is not None
    assert item.created_at is not None
    assert item.updated_at is None


async def test_hero_relationships(db: Session):
    """Test hero relationships."""
    team = Team(name="Test Team", headquarters="Test HQ")
    item = Item(name="Test Item", created_by_id=uuid4())
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    assert hero.awaitable_attrs.team is not None
    assert hero.awaitable_attrs.item is not None


async def test_timestamp_update(db: Session, team: Team, item: Item):
    """Test timestamp update."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    hero.name = "Updated Hero"
    await db.commit()
    await db.refresh(hero)
    assert hero.updated_at is not None


async def test_unique_constraint(db: Session, team: Team, item: Item):
    """Test unique constraint violation."""
    hero1 = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    hero2 = Hero(
        name="Test Hero",
        secret_identity="Another Identity",  # nosec:B106
        age=25,
        team=team,
        item=item,
    )
    db.add(hero1)
    await db.commit()
    db.add(hero2)
    with pytest.raises(sa.exc.IntegrityError):
        await db.commit()


async def test_foreign_key_constraint(db: Session):
    """Test foreign key constraint violation."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team_id=uuid4(),
    )
    db.add(hero)
    with pytest.raises(sa.exc.IntegrityError):
        await db.commit()


async def test_invalid_uuid(db: Session):
    """Test invalid UUID."""
    with pytest.raises(ValueError):
        Hero(
            name="Test Hero",
            secret_identity="Test Identity",  # nosec:B106
            age=30,
            team_id="invalid-uuid",
        )


async def test_implicit_io(db: Session, team: Team, item: Item):
    """Test implicit I/O prevention."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    with pytest.raises(sa.exc.MissingGreenlet):
        _ = hero.team.name  # Accessing relationship without await


async def test_aware_datetime(db: Session, team: Team, item: Item):
    """Test aware datetime fields."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    assert hero.created_at.tzinfo is not None
    assert hero.created_at.tzinfo == timezone.utc


async def test_model_config(db: Session, team: Team, item: Item):
    """Test model configuration."""
    hero = Hero(
        name="Test Hero",
        secret_identity="Test Identity",  # nosec:B106
        age=30,
        team=team,
        item=item,
    )
    db.add(hero)
    await db.commit()
    await db.refresh(hero)
    assert hero.model_dump(by_alias=True)["secretIdentity"] == "Test Identity"
