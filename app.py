from flask import *
import pymysql
 
app = Flask(__name__)

@app.route("/api/signup" , methods=["POST"] )
def signup():
    username= request.form['username']
    email=request.form['email']
    phone=request.form['phone']
    password=request.form['password']

    print(username,email,phone,password)
    #create connection to db
    connection=pymysql.connect(host="localhost",user="root",password="",database="austine_sokogarden")

    #create cursor to handle sql queries
    cursor=connection.cursor()

    #create the sql query

    sql="insert into users (username,email,phone,password) values(%s,%s,%s,%s)"

    #data to be saved
    data=(username,email,phone,password)
    print(data)

    # execute the sql query
    cursor.execute(sql,data)

    #save the data
    connection.commit()
    return jsonify({"message":"Sign up successfully"})




# LOGIN

@app.route("/api/login", methods=["POST"])
def login():
    email=request.form["email"]
    password=request.form["password"]

    print(email,password)

    connection=pymysql.connect(host='localhost',user='root',database='austine_sokogarden',password='')

    cursor=connection.cursor(pymysql.cursors.DictCursor)

    sql=("select user_id,username,email,phone from users where email=%s and password=%s")
    data=(email,password)
    cursor.execute(sql,data)

    #check resulting rows

    if cursor.rowcount==0:
        return jsonify({"message":"Invalid Credentials"})
    else:
        #get the user data
        user=cursor.fetchone()
        return jsonify({"message":"Login successful","user":user})


    




if __name__ == "__main__":
    app.run(debug=True)