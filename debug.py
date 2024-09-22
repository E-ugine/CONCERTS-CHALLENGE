from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Band, Venue, Concert

engine = create_engine('sqlite:///concerts.db')
Session = sessionmaker(bind=engine)
session = Session()


band1 = Band(name="Rockers", hometown="Nakuru")
venue1 = Venue(title="Kenya Stadium", city="Nairobi")

session.add_all([band1, venue1])
session.commit()

concert1 = Concert(date="2024-09-22", name="Rock Festival", band=band1, venue=venue1)
session.add(concert1)
session.commit()

print(concert1.introduction())  
 
