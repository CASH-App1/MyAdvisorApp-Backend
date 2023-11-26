from App.database import db
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Department(db.Model):
    __tablename__ = 'departments'

    departmentCode = Column(String(10), primary_key=True)
    departmentName = Column(String, nullable=False)

    programs = relationship('Program', backref='department')
    staffMembers = relationship('Staff', backref='department')

    def __repr__(self):
        return f"<Department {self.departmentCode} - {self.departmentName}>"
