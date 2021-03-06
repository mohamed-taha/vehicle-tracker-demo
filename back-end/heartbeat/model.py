from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

from .app import db


# NOTE: Consider using view for date representations.
# NOTE: Consider Creating an internal data access micorservice.
class Vehicle(db.Model):
    __tablename__ = 'vehicle'

    id = db.Column(db.String(17), primary_key=True)
    reg_no = db.Column(db.String(6))
    customer_id = db.Column(db.Integer, ForeignKey('customer.id'))
    customer = relationship("Customer", back_populates="vehicles")
    heartbeat_ts = db.Column(db.DateTime())


class Customer(db.Model):
    __tablename__ = 'customer'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    vehicles = relationship("Vehicle", back_populates="customer")


class EventRecord(db.Model):
    sequence_id = db.Column(UUIDType(), nullable=False, primary_key=True)
    position = db.Column(db.BigInteger(), nullable=False)
    topic = db.Column(db.String(255), nullable=False)
    state = db.Column(db.Text(), nullable=False)
    __table_args__ = db.Index('index', 'sequence_id', 'position', unique=True),
