
# -- TABLA categories: id, name, description
# CREATE TABLE IF NOT EXISTS `categories` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `name` varchar(50) NOT NULL,
#   `description` varchar(255) NOT NULL,
#   PRIMARY KEY (`id`)
# ) ENGINE = InnoDB DEFAULT CHARSET = utf8;

# Abstract class
# Name: Category
# Description: Category entity
# Attributes: id, name, description
# Methods: __init__, __str__, save, update, delete, get_all, get_by_id, get_by_name

from .entities.Category import Category
from .entities.User import User


class ModelCategory:

    # Save, only admins can do this
    @classmethod
    def save(self, db, category: Category, user: User):

            if category.save(db):
                return 200
            else:
                return 409


    # Update, only admins can do this

    @classmethod
    def update(self, db, category: Category, user: User):

        if category.update(db):
            return 200
        else:
            return 409


    # Delete, only admins can do this

    @classmethod
    def delete(self, db, category: Category, user: User):

            if category.delete(db):
                return 200
            else:
                return 409


    # Get all categories

    @classmethod
    def get_all(self, db):
        try:
            return Category.get_all(db)
        except Exception as ex:
            raise Exception(ex)

    # Get category by id

    @classmethod
    def get_by_id(self, db, id):
        try:
            return Category.get_by_id(db, id)
        except Exception as ex:
            raise Exception(ex)

    # Get category by name

    @classmethod
    def get_by_name(self, db, name):
        try:
            return Category.get_by_name(db, name)
        except Exception as ex:
            raise Exception(ex)


# Abstract class
# Name: ModelCategory
# Description: Category model
# Attributes: None
# Methods:
"""
+ save(self, db, category, user)
+ update(self, db, category, user)
+ delete(self, db, category, user)
+ get_all(self, db)
+ get_by_id(self, db, id)
+ get_by_name(self, db, name)
"""
