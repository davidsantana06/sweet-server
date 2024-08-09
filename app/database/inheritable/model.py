from datetime import datetime
from flask_sqlalchemy.model import Model as SQLAlchemyModel
from re import findall
from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import declared_attr
from typing import Dict

from app.extensions import database


class Model(SQLAlchemyModel):
    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=datetime.now())

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            nullable=False,
            default=datetime.now(),
            onupdate=datetime.now()
        )

    @declared_attr
    def __tablename__(cls):
        cls_name_words = findall(r'[A-Z][a-z]*', cls.__name__)
        table_name = '_'.join(cls_name_words).lower()
        return table_name

    @staticmethod
    def save(model: 'Model') -> None:
        try:
            database.session.add(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    @staticmethod
    def delete(model: 'Model') -> None:
        try:
            database.session.delete(model)
            database.session.commit()
        except Exception as e:
            database.session.rollback()
            raise e

    def to_dict(self) -> Dict[str, object]:
        return {
            column.name: getattr(self, column.name)
            for column in self.__table__.columns
            if column.name not in ['created_at', 'updated_at']
        }
