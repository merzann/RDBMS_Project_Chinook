from sqlalchemy import (
    create_engine, Column, Float, Integer, String
)
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()

# create "Downloadable Images" table
class DownloadableImage(base):
    __tablename__ = "Downloadedable Images"
    id = Column(Integer, primary_key=True)
    image = Column(String)
    category = Column(String)
    size = Column(String)
    price = Column(Float)

# ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens a session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)

# creating records on Downloadable Images table
imageSmall = DownloadableImage(
    image="Sunset at Waterville beach, Co. Kerry",
    category="sunset",
    size="600x400px",
    price=0.99,
)

imageMedium = DownloadableImage(
    image="Sunset at Waterville beach, Co. Kerry",
    category="sunset",
    size="800x600px",
    price=1.99,
)

imageLarge = DownloadableImage(
    image="Sunset at Waterville beach, Co. Kerry",
    category="sunset",
    size="1024x768x",
    price=2.99,
)

imageSmall2 = DownloadableImage(
    image="Sunset at Derrynane beach, Co. Kerry",
    category="sunset",
    size="600x400px",
    price=0.99,
)

imageMedium2 = DownloadableImage(
    image="Sunset at Derrynane beach, Co. Kerry",
    category="sunset",
    size="800x600px",
    price=1.99,
)

imageLarge2 = DownloadableImage(
    image="Sunset at Derrynane beach, Co. Kerry",
    category="sunset",
    size="1024x768x",
    price=2.99,
)

imageSmall3 = DownloadableImage(
    image="Storm at Waterville beach, Co. Kerry",
    category="sunset",
    size="600x400px",
    price=0.99,
)

imageMedium3 = DownloadableImage(
    image="Storm at Waterville beach, Co. Kerry",
    category="sunset",
    size="800x600px",
    price=1.99,
)

imageLarge3 = DownloadableImage(
    image="Storm at Waterville beach, Co. Kerry",
    category="sunset",
    size="1024x768x",
    price=2.99,
)

# add each instance of downloadable image to session
session.add(imageSmall)
session.add(imageMedium)
session.add(imageLarge)
session.add(imageSmall2)
session.add(imageMedium2)
session.add(imageLarge2)
session.add(imageSmall3)
session.add(imageMedium3)
session.add(imageLarge3)

# commit session to the database
session.commit()

# query the database to find all Downloadable Images
downloadable_images = session.query(DownloadableImage).all()  # Get all records
for image in downloadable_images:
    print(
        image.id,
        image.image,
        image.category,
        image.size,
        image.price,
        sep=" | "
    )
