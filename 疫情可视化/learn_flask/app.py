from flask import render_template
from flask import Flask
from flask import jsonify
import add

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("main.html")


@app.route("/warning")
def warning():
    return render_template("warning.html")


@app.route("/c1")
def c1data():
    data=add.visit().run()
    return jsonify({"newconfirm":data[0],"confirm":data[1],"No":data[2],"heal":data[3],"dead":data[4],'newtime':f'数据更新截止至:{data[5]}'})


@app.route("/c2")
def c2data():
    data=[]
    target=add.C2().Run()
    for i in target:
        data.append({"name":i[0],"value":i[1]})
    return jsonify({"data":data})


@app.route("/l1")
def l1data():
    data=add.Left().RunUp()
    confirm,heal,no,dead,day=[],[],[],[],[]
    for i in data:
        confirm.append(i[0])
        heal.append(i[1])
        no.append(i[2])
        dead.append(i[3])
        day.append(i[4])
    return jsonify({"day":day[::-1],"confirm":confirm[::-1],"suspect":no[::-1],"heal":heal[::-1],"dead":dead[::-1]})


@app.route("/l2")
def l2data():
    data=add.Left().RunDown()
    confirm,heal,no,dead,day=[],[],[],[],[]
    for i in data:
        confirm.append(i[0])
        heal.append(i[1])
        no.append(i[2])
        dead.append(i[3])
        day.append(i[4])
    return jsonify({"day":day[::-1],"confirm":confirm[::-1],"suspect":no[::-1],"heal":heal[::-1],"dead":dead[::-1]})


@app.route("/r1")
def r1data():
    data=add.R1().Run()
    city,number=[],[]
    for i in data:
        city.append(i[0])
        number.append(i[1])
    return jsonify({"city":city,"number":number})


@app.route("/r2")
def r2data():
    data=add.R2().Run()
    ans=[]
    for i in range(len(data)):
        ans.append({"name":data[i][0],"value":data[i][1]})
    return jsonify({"data":ans})


if __name__=="__main__":
    app.run(port=80)
    # r2data()