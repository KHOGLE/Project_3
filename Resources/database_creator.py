from numpy import genfromtxt
from sqlalchemy import Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', skip_header=1, converters={0: lambda s: str(s)})
    return data.tolist()

Base = declarative_base()

class Business_Data(Base):
    #Tell SQLAlchemy what the table name is and if there's any table-specific arguments it should know about
    __tablename__ = 'business_data'
    __table_args__ = {'sqlite_autoincrement': True}
    #tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False) 
    business_name = Column(String)
    street_address = Column(String)
    city = Column(String)
    zip_code = Column(String)
    naics_sector = Column(Float)
    industry = Column(String)
    location_start_date = Column(String)
    coordinates = Column(String)
    lat = Column(Float)
    lng = Column(Float)

if __name__ == "__main__":

    #Create the database
    engine = create_engine('sqlite:///business_data.db')
    Base.metadata.create_all(engine)

    #Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        file_name = "BusinessData_Final.csv" 
        data = Load_Data(file_name) 

        for i in data:
            record = Business_Data(**{
                'id': i[0],
                'business_name' : i[1],
                'street_address' : i[2],
                'city' : i[3],
                'zip_code' : i[4],
                'naics_sector' : i[5],
                'industry' : i[6],
                'location_start_date': i[7],
                'coordinates' : i[8],
                'lat': i[9],
                'lng' : i[10]
            })
            s.add(record) #Add all the records

        s.commit() #Attempt to commit all the records
    except:
        s.rollback() #Rollback the changes on error
    finally:
        s.close()