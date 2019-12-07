from  DLMS import db
from datetime import datetime

class User_t1(db.Model):
    UID=db.Column(db.String(10),primary_key=True)
    First_Name= db.Column(db.String(20), nullable=False )
    Middle_Name = db.Column(db.String(20), nullable=False)
    Last_Name = db.Column(db.String(20), nullable=False)
    E_Mail = db.Column(db.String(120), unique=True, nullable=False)
    Password=db.Column(db.String(60),nullable=False)
    Gender=db.Column(db.String(15),nullable=False)
    DOB=db.Column(db.Date(),nullable=False)
    Blood_Group=db.Column(db.String(10),nullable=True)
    Branch=db.Column(db.String(30),nullable=False)
    Programme=db.Column(db.String(10),nullable=False)
    Hostler_or_not=db.Column(db.Boolean(),nullable=False,default=True)
    Address_Line=db.Column(db.String(150),nullable=False)
    District=db.Column(db.String(30),nullable=False)
    State=db.Column(db.String(35),nullable=False)
    Country=db.Column(db.String(35),nullable=False)
    Pincode=db.Column(db.Integer,nullable=False)
    LID=db.Column(db.String(10),db.ForeignKey('librarian_t1.LID'))
    log=db.relationship('Log')
    phoneNumber=db.relationship('User_t2')

    def __repr__(self):
        return "User_t1('{self.UID},{self.First_Name},{self.Middle_Name},{self.Last_Name},{self.E_mail},{self.Password},{self.Gender},{self.DOB},{self.Bloog_Group},{self.Branch},{self.Programme},{self.Hostler_or_not},{self.Address_Line},{self.District},{self.State},{self.Country},{self.Pincode},{self.LID}')"

class User_t2(db.Model):
    UID=db.Column(db.String(10),db.ForeignKey('user_t1.UID'),primary_key=True)
    PhoneNumber=db.Column(db.Integer,primary_key=True)
    def __repr__(self):
        return "User_t2('{self.UID},{self.PhoneNumber}')"

class Librarian_t1(db.Model):
    LID = db.Column(db.String(10), primary_key=True)
    First_Name = db.Column(db.String(20), nullable=False)
    Middle_Name = db.Column(db.String(20), nullable=False)
    Last_Name = db.Column(db.String(20), nullable=False)
    E_Mail = db.Column(db.String(120), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    Gender = db.Column(db.String(15), nullable=False)
    DOB = db.Column(db.Date(), nullable=False)
    Blood_Group = db.Column(db.String(10), nullable=True)
    Branch = db.Column(db.String(30), nullable=False)
    Education_Qualification = db.Column(db.String(10), nullable=False)
    Address_Line = db.Column(db.String(150), nullable=False)
    District = db.Column(db.String(30), nullable=False)
    State = db.Column(db.String(35), nullable=False)
    Country = db.Column(db.String(35), nullable=False)
    Pincode = db.Column(db.Integer, nullable=False)
    User=db.relationship('User_t1')
    Book=db.relationship('Book_t1')
    log = db.relationship('Log')
    phoneNumber = db.relationship('Librarian_t2')

    def __repr__(self):
        return "Librarian_t1('{self.LID},{self.First_Name},{self.Middle_Name},{self.Last_Name},{self.E_mail},{self.Password},{self.Gender},{self.DOB},{self.Blood_Group},{self.Branch},{self.Education_Qualification},{self.Address_Line},{self.District},{self.State},{self.Country},{self.Pincode}')"

class Librarian_t2(db.Model):
    LID=db.Column(db.String(10),db.ForeignKey('librarian_t1.LID'),primary_key=True)
    PhoneNumber=db.Column(db.Integer,primary_key=True)

    def __repr__(self):
        return "User_t2('{self.UID},{self.PhoneNumber}')"


class Admin_t1(db.Model):
    User_Name=db.Column(db.String(20),primary_key=True,nullable=True)
    E_Mail = db.Column(db.String(120), unique=True, nullable=False)
    Password = db.Column(db.String(60), nullable=False)
    phoneNumber=db.relationship('Admin_t2')

    def __repr__(self):
        return "Admin_t1('{self.User_Name},{self.Email},{self.Password}')"


class Admin_t2(db.Model):
    User_Name = db.Column(db.String(10), db.ForeignKey('admin_t1.User_Name'), primary_key=True)
    PhoneNumber = db.Column(db.Integer,primary_key=True, nullable=False)

    def __repr__(self):
        return "Admin_t2('{self.User_Name},{self.PhoneNumber}')"

class Book_t1(db.Model):
    BID = db.Column(db.String(10), primary_key=True)
    ISBN = db.Column(db.String(20), nullable=False)
    Title = db.Column(db.String(20), nullable=False)
    Language = db.Column(db.String(20), nullable=False,default='English')
    Publisher = db.Column(db.String(120), nullable=False)
    Publisher_year = db.Column(db.String(10), nullable=False)
    Publisher_Place = db.Column(db.String(15), nullable=False)
    Total_No_Of_Pages = db.Column(db.Integer, nullable=False)
    Price = db.Column(db.Integer, nullable=True)
    Status = db.Column(db.Boolean(), nullable=False, default=True)
    LID = db.Column(db.String(10), db.ForeignKey('librarian_t1.LID'))
    author = db.relationship('Book_t2')
    subject = db.relationship('Book_t3')
    keywords=db.relationship('Book_t4')
    log = db.relationship('Log')

    def __repr__(self):
        return "Book_t1('{self.BID},{self.ISBN},{self.Title},{self.Language},{self.Publisher},{self.Publisher_year},{self.Publisher_Place},{self.Total_No_Of_Pages},{self.Price},{self.Status},{self.LID}')"

class Book_t2(db.Model):
    BID = db.Column(db.String(10), db.ForeignKey('book_t1.BID'), primary_key=True)
    Author = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "Book_t2('{self.BID},{self.Author}')"

class Book_t3(db.Model):
    BID = db.Column(db.String(10), db.ForeignKey('book_t1.BID'), primary_key=True)
    Subject = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "Book_t2('{self.BID},{self.Subject}')"

class Book_t4(db.Model):
    BID = db.Column(db.String(10), db.ForeignKey('book_t1.BID'), primary_key=True)
    Keywords = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return "Book_t2('{self.BID},{self.Keywords}')"

class Log(db.Model):
    LID = db.Column(db.String(10), db.ForeignKey('librarian_t1.LID'), primary_key=True)
    UID = db.Column(db.String(10), db.ForeignKey('user_t1.UID'), primary_key=True)
    BID = db.Column(db.String(10), db.ForeignKey('book_t1.BID'), primary_key=True)
    Issue_Date = db.Column(db.DateTime,nullable=False, default=datetime.utcnow())
    Actual_Date = db.Column(db.DateTime,nullable=False)
    Original_Date = db.Column(db.DateTime,nullable=True)
    Fine = db.Column(db.Integer,nullable=False, default=0)

    def __repr__(self):
        return "Log('{self.LID},{self.UID},{self.BID},{self.Issue_Date},{self.Actual_Date},{self.Original_Date},{self.Fine}')"
