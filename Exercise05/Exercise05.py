from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from flask import Flask, request, jsonify

engine = create_engine('sqlite:///test.db', echo=True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customer'

    id = Column(Integer, primary_key=True)
    CustomerName = Column(String(50))
    ContactName = Column(String(50))
    Address = Column(String(100))
    City = Column(String(100))
    PostalCode = Column(String(50))
    Country = Column(String(50))

    def __repr__(self):
        data = {
            'id': self.id,
            'CustomerName': self.CustomerName,
            'ContactName': self.ContactName,
            'Address': self.Address,
            'City': self.City,
            'PostalCode':self.PostalCode,
            'Country': self.Country
        }
        return data

Base.metadata.create_all(engine)

app = Flask(__name__)

@app.route("/createCustomer", methods = ['POST'])
def create_customer():
    Session = sessionmaker(bind=engine)
    session = Session()
    data = request.form
    customer = Customer(**data)
    session.add(customer)
    output = {
        'success':True
    }
    session.commit()
    return jsonify(output)

@app.route("/updateCustomer", methods = ['PUT'])
def update_customer():
    Session = sessionmaker(bind=engine)
    session = Session()
    data = request.form
    param = request.args

    result = session.query(Customer)
    for key, value in param.items():
        result = result.filter(getattr(Customer, key)==value)
    result.update(data)
    session.commit()
    output = {
        'success': True
    }
    return jsonify(output)

@app.route("/getCustomer", methods = ['GET'])
def get_customer():
    Session = sessionmaker(bind=engine)
    session = Session()
    param = request.args
    result = session.query(Customer)
    for key, value in param.items():
        result = result.filter(getattr(Customer, key)==value)
    result = [i.__repr__() for i in result]
    
    data = {
        'data': result
    }
    return jsonify(data)

@app.route("/deleteCustomer", methods = ["POST"])
def delete_customer():
    Session = sessionmaker(bind=engine)
    session = Session()
    param = request.args

    result = session.query(Customer)
    for key, value in param.items():
        result = result.filter(getattr(Customer, key)==value)
    result.delete()
    session.commit()
    output = {
        'success': True
    }
    return jsonify(output)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6123, debug=True) 