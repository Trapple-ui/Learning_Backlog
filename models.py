import sqlalchemy as db
from sqlalchemy import CheckConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

engine = db.create_engine('postgresql+psycopg2:///learning_tracker.db')

class Model(DeclarativeBase): pass

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

