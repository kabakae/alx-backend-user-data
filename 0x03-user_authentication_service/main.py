#!/usr/bin/env python3
"""
Main file to print table and column information for the User model.
"""

from user import User

def print_table_info() -> None:
    """
    Print the table name and column details for the User model.
    """
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))

if __name__ == "__main__":
    print_table_info()
