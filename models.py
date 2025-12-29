import sqlalchemy as db
from sqlalchemy import CheckConstraint, ForeignKey, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker, relationship

engine = db.create_engine('postgresql+psycopg2://me:secret@localhost:5432/learning_tracker')

SessionFactory = sessionmaker(bind=engine, autoflush=False) # фабрика сессий - создает сессии. Один раз настроил и все
# session = Session(engine) # одна сессия

class Model(DeclarativeBase): pass

# таблица тегов
class Tags(Model):
    __tablename__ = 'tags'

    tag_id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)

    resources = relationship('Resources', secondary='resource_tags', back_populates='tags')

# таблица ресурсов
class Resources(Model):
    __tablename__ = 'resources'

    res_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    url: Mapped[str] = mapped_column(db.Text(), nullable=False)
    duration: Mapped[int] = mapped_column(db.Integer(), nullable=False)
    type: Mapped[str] = mapped_column(db.String(20))
    priority: Mapped[int] = mapped_column(db.Integer)
    status: Mapped[str] = mapped_column(db.String(20))
    note_text: Mapped[str] = mapped_column(db.Text(), default='')

    __table_args__ = (
        CheckConstraint(type.in_(('видео', 'статья', 'курс', 'книга', 'сайт', 'подкаст')), name='check_in_type'),
        CheckConstraint(priority.in_((1, 2, 3, 4, 5)), name='check_in_priority')
    )

    tags = relationship('Tags', secondary='resource_tags', back_populates='resources')

# связывающая таблица для отношения "многие ко многим"
class ResourceTags(Model):
    __tablename__ = 'resource_tags'

    # первичный ключ - это составной ключ из таблицы ресурсов и тегов
    tag: Mapped[int] = mapped_column(db.Integer, ForeignKey('tags.tag_id'), primary_key=True)
    res_id: Mapped[int] = mapped_column(db.Integer, ForeignKey('resources.res_id'), primary_key=True)

def create_tables():
    with SessionFactory() as session:
        Model.metadata.create_all(engine)

def delete_tables():
    with SessionFactory() as session:
        Model.metadata.drop_all(engine)
