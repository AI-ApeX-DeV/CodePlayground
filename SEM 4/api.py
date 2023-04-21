from flask import Flask,jsonify,request
from flask_cors import CORS;
import pymysql

app=Flask(__name__)
cors=CORS(app)
conn=pymysql.connect(host='localhost',user='root',password='Shahsai@2002',db='purchasetosales')
cur=conn.cursor()
@app.route('/',methods=['PUT'])
def insertrec():
    data=request.get_json()
    name=data['name']
    quantity=data['quantity']
    date=data['date']
    time=data['time']
    amount=data['amount']

    query=f"insert into purchases(name,quantity,date,time,amount) values ('{name}','{quantity}','{date}','{time}','{amount}')"

    #print(query)
    cur.execute(query)
    conn.commit()
    return jsonify({'message': f'Record successfully updated for {data}'})
if __name__=='__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0',port=int('1234'),debug=True)