from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create instances
band1 = Band(name="Rockers", hometown="Nairobi")
venue1 = Venue(title="Kenya Stadium", city="Nairobi")

session.add_all([band1, venue1])
session.commit()

# Create concert
concert1 = Concert(date="2024-09-22", band=band1, venue=venue1)
session.add(concert1)
session.commit()

# Test methods
print(concert1.introduction())  # Example introduction
