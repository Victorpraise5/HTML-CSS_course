from sqlalchemy import Table, Column, Integer, String, Float, ForeignKey, DateTime, create_engine, MetaData
from eralchemy import render_er

metadata = MetaData()

user = Table('user', metadata,
             Column('user_id', Integer, primary_key=True),
             Column('username', String),
             Column('email', String),
             Column('password_hash', String),
             Column('created_at', DateTime))

property = Table('property', metadata,
                 Column('property_id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String),
                 Column('location', String),
                 Column('price_per_night', Float),
                 Column('property_type', String),
                 Column('owner_id', Integer, ForeignKey('user.user_id')),
                 Column('created_at', DateTime))

booking = Table('booking', metadata,
                Column('booking_id', Integer, primary_key=True),
                Column('user_id', Integer, ForeignKey('user.user_id')),
                Column('property_id', Integer, ForeignKey('property.property_id')),
                Column('check_in_date', DateTime),
                Column('check_out_date', DateTime),
                Column('total_price', Float),
                Column('status', String),
                Column('created_at', DateTime))

payment = Table('payment', metadata,
                Column('payment_id', Integer, primary_key=True),
                Column('booking_id', Integer, ForeignKey('booking.booking_id')),
                Column('user_id', Integer, ForeignKey('user.user_id')),
                Column('amount', Float),
                Column('payment_method', String),
                Column('payment_status', String),
                Column('created_at', DateTime))

review = Table('review', metadata,
               Column('review_id', Integer, primary_key=True),
               Column('user_id', Integer, ForeignKey('user.user_id')),
               Column('property_id', Integer, ForeignKey('property.property_id')),
               Column('rating', Integer),
               Column('comment', String),
               Column('created_at', DateTime))

attraction = Table('attraction', metadata,
                   Column('attraction_id', Integer, primary_key=True),
                   Column('name', String),
                   Column('location', String),
                   Column('description', String),
                   Column('property_id', Integer, ForeignKey('property.property_id')),
                   Column('distance', Float),
                   Column('created_at', DateTime))

car = Table('car', metadata,
            Column('car_id', Integer, primary_key=True),
            Column('make', String),
            Column('model', String),
            Column('price_per_day', Float),
            Column('availability', String),
            Column('location', String),
            Column('owner_id', Integer, ForeignKey('user.user_id')),
            Column('created_at', DateTime))

# Generate the ERD
render_er(metadata, 'stayinn_erd.png')