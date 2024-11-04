import asyncio
import logging

import yaml
from aiohttp import ClientSession, ClientTimeout
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Load the configuration from the config.yaml file
def load_config():
    with open("config.yaml", "r") as file:
        return yaml.safe_load(file)


# Setup SQLAlchemy database model and connection
Base = declarative_base()


class DataEntry(Base):
    __tablename__ = "data_entries"
    id = Column(Integer, primary_key=True)
    movie = Column(String)
    rating = Column(String)
    imdb_url = Column(String)


def setup_database(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session


# Set up logging
def setup_logging(level):
    logging.basicConfig(level=getattr(logging, level.upper()),
                        format="%(asctime)s - %(levelname)s - %(message)s")


# Async function to fetch data from the API
async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
    except Exception as e:
        logging.error(f"Error fetching data: {e}")
        return None


# Main function to orchestrate fetching and storing data
async def main():
    # Load config and set up logging
    config = load_config()
    setup_logging(config["logging"]["level"])

    # setting the database connection
    db_session = setup_database(config["database"]["url"])

    # fetching and processing data asynchronously
    async with ClientSession(timeout=ClientTimeout(config["api"]["timeout"])) as session:

        # fetching the data from the api with url configured in the config.yaml
        data = await fetch_data(session, config["api"]["url"])

        if data:
            for item in data:
                print(item)
                entry = DataEntry(id=item["id"], movie=item["movie"], rating=str(item["rating"]), imdb_url=item["imdb_url"])
                try:
                    # store the data entry in the database
                    with db_session() as session:
                        session.add(entry)
                        session.commit()
                    logging.info(f"Stored entry: {item['id']} {item['movie']}{item['rating']}{item['imdb_url']}")
                except SQLAlchemyError as e:
                    logging.error(f"Database error: {e}")
        else:
            logging.error("No data retrieved from API.")


if __name__ == "__main__":
    asyncio.run(main())
