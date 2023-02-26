from flask import Flask, render_template, request,jsonify
import pandas as pd
app = Flask(__name__)
import mysql.connector
import datetime
connection = mysql.connector.connect(host='localhost',
                                         database='phone',
                                         user='testuser',
                                         password='test123')

@app.route('/', methods=['GET', 'POST'])
def home():
      return render_template('index.html')
  
@app.route('/initiate-call',methods=['POST'])
def call():
    if request.method == "POST":
        details=request.json
        from_number= details['from_number']
        to_number = details['to_number']
        dateinfo=datetime.datetime.utcnow().isoformat()
        cur = connection.cursor()
        cur.execute("INSERT INTO phonedb VALUES (%s, %s,%s)", (from_number, to_number,dateinfo))
        connection.commit()
        cur.close()
        return 'success' 
    
@app.route('/callreport',methods=['GET'])
def report():
    if request.method == "GET":
        num=request.args.get("phone")
        page=request.args.get("pagenumber")
        limit =2
        offset=limit*(int(page)-1)
        cur = connection.cursor()
        cur.execute("select * from phonedb WHERE SenderNumber=%s OR ReceverNumber=%s LIMIT %s,%s;", (num,num,offset,limit))
        result = cur.fetchall()
        connection.commit()
        df = pd.DataFrame(result, columns = ['from_number','to_number','start_time','id'])
        cur.close()  
        x=df.to_dict('records')
        return jsonify({'data':x,'success':True })
        
        

if __name__ == '__main__':
    app.run()