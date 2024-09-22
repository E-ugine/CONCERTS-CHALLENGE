from lib.models import Band, Venue, Concert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///lib/db/concerts.sqlite')
Session = sessionmaker(bind=engine)
session = Session()

new_band = Band(name="Imagine Dragons", hometown="Las Vegas, Nevada")
session.add(new_band)
session.commit()

new_venue = Venue(title="Allegiant Stadium", city="Las Vegas")
session.add(new_venue)
session.commit()

new_concert = Concert(date="2024-02-11", name="Super Bowl LVIII", band_id=new_band.id, venue_id=new_venue.id)
session.add(new_concert)
session.commit()

bands = session.query(Band).all()
venues = session.query(Venue).all()
concerts = session.query(Concert).all()

for band in bands:
    print(band.name)

for venue in venues:
    print(venue.title)

for concert in concerts:
    print(concert.name)