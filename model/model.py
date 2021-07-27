from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, session
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, select
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql://root:dimitrou@127.0.0.1:3306/stupidity",encoding='latin1', echo=True)

class Child(Base):
    __tablename__ = 'child'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    children = relationship("Stupidity")   

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name



class Stupidity(Base):
    __tablename__ = 'stupidity'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('child.id'))

    def __init__(self,parent_id):
        self.parent_id = parent_id

    def __str__(self):
        return self.parent_id        


def connexion():
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine) 
    try:
        child1 = Child(name = 'clarence')  
        child2 = Child(name = 'william')   
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add_all([child1,child2])
        session.commit()
    except:
        print("child already exist")    




def getChild():
     Session = sessionmaker(bind=engine)
     session = Session()
     listChild = []
     childs = session.query(Child).all()
     for index,child in enumerate(childs):         
         listChild.append({'id':child.id, 'name':  child.name})         
     return listChild



def getCountStupidityById(id):
         Session = sessionmaker(bind=engine)
         session = Session()
         result = session.query(Stupidity).filter_by(parent_id = id).all()
         data = []
         return len(result)
    
   
         
        
def setStupidity(id):
    try:
        Session = sessionmaker(bind=engine)
        session = Session()
       
        stupidity = Stupidity(parent_id =  id)
        session.add(stupidity)
        session.commit()
        return {'res': 'enregistrement réussi'}   
    except:
        return {'res': 'error d\'enregistrement'}    
        



     
     


