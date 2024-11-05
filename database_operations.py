from fastapi import FastAPI, Depends, HTTPException, Query
from typing import Annotated
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int = Field(default=None)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


class HeroPublic(HeroBase):
    id: int


class HeroCreate(HeroBase):
    secret_name: str


class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


sqlite_db = 'database.db'
sqlite_url = f'sqlite:///{sqlite_db}'

connect_args = {'check_same_thread': False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


session_start = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event('startup')
def on_startup():
    create_db_and_tables()


@app.post('/heroes', response_model=HeroPublic, status_code=201)
def create_heroes(hero: HeroCreate, session: session_start):
    db_hero = Hero.model_validate(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.get('/heroes', response_model=list[HeroPublic], status_code=200)
def get_heroes(session: session_start, offset: int = 0, limit: int = 100):
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes


@app.get('/hero/{hero_id}', response_model=HeroPublic, status_code=200)
def get_heroes(hero_id: int, session: session_start):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.patch('/hero/{hero_id}', response_model=HeroPublic, status_code=200)
def update_hero(hero_id: int, hero: HeroUpdate, session: session_start):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.model_dump(exclude_unset=True)
    hero_db.sqlmodel_update(hero_data)
    session.add(hero_db)
    session.commit()
    session.refresh(hero_db)
    return hero_db


@app.delete('/heroes/{hero_id}', status_code=204)
def delete_hero(hero_id: int, session: session_start):
    hero_db = session.get(Hero, hero_id)
    if not hero_db:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero_db)
    session.commit()
    return {'Ok': True}
