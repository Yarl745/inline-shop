from decimal import Decimal

from sqlalchemy import sql, Column, Sequence, Numeric

from utils.db_api.database import db


class BaseModel(db.Model):
    __abstract__ = True

    created_at = Column(db.DateTime(True), server_default=db.func.now())


class Item(BaseModel):
    __tablename__ = "items"

    query: sql.Select

    id = Column(db.Integer, Sequence("item_id_seq"), primary_key=True)
    name = Column(db.String(20))
    photo_id = Column(db.String(100))
    small_photo = Column(db.String(50))
    description = Column(db.String(250))
    price: Decimal = Column(Numeric(precision=9, scale=2, decimal_return_scale=2))

    def __repr__(self):
        return \
            f"""
            Товар №{self.id} - {self.name}
            Цена: {self.price}
            """


class User(BaseModel):
    __tablename__ = 'users'

    query: sql.Select

    user_id = Column(db.BigInteger, primary_key=True)
    username = Column(db.String(20))
    full_name = Column(db.String(40))
    balance = Column(db.Numeric(precision=9, scale=2, decimal_return_scale=2), default=0)

    phone = Column(db.String(15), default=None)
    shipping_info = Column(db.String(100))

    referral = Column(db.BigInteger)

