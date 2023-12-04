from App.database import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from App.models import *

class Department(db.Model):
    departmentCode = Column(db.String(10), primary_key=True)
    departmentName = Column(db.String(100), nullable=False)

    programs = relationship('Program', backref='department')
    staffMembers = relationship('Staff', backref='staffDepartment')

    def __repr__(self):
        return f"<Department {self.departmentCode} - {self.departmentName}>"
