#!/usr/bin/python3
"""This module defines a class to manage DB storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base


class DBStorage:
    '''defines a class to manage DB storage for hbnb clone'''
    __engine = None
    __session = None

    def __init__(self):
        '''initializes a new instance of DBStorage
        create the engine (self.__engine)
        linked to the MySQL database and user created before'''

        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_password = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_database = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                          MySQL_user,
                                          MySQL_password,
                                          MySQL_host,
                                          MySQL_database), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''query on the current database session (self.__session) all objects
        depending of the class name (argument cls)'''
        objects = {}
        if cls is None:
            from models.user import User
            from models.state import State
            from models.review import Review
            from models.place import Place
            from models.city import City
            from models.amenity import Amenity
            classes = {'user': User, 'place': Place,
                       'amenity': Amenity, 'state': State,
                       'review': Review, 'city': City}

            for c in classes.values():
                records = self.__session.query(c).all()
                for object in records:
                    objects.update(
                        {object.__class__.__name__ + '.' + object.id: object})

        else:
            records = self.__session.query(cls).all()

            for object in records:
                objects.update(
                    {object.__class__.__name__ + '.' + object.id: object})
        return objects

    def new(self, obj):
        '''add the object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete from the current database session obj if not None'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''create all tables in the database
        create the current database session
        from the engine by using a sessionmaker
        '''
        from models.user import User
        from models.state import State
        from models.review import Review
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.base_model import BaseModel, Base
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """all remove() method on the private session attribute"""
        self.__session.close()
