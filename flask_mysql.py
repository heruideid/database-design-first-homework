from connect_mysql import init, insert, delete,update,query,showall,end
from flask import Flask, request, redirect, url_for
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return showall()

@app.route('/before_insert', methods=['GET', 'POST'])
def before_insert():
    return render_template('before_insert.html')

@app.route('/after_insert', methods=['POST'])
def after_insert():
    value = []
    sno = request.form.get('sno')
    cno = request.form.get('cno')
    if sno!="":
        value.append(request.form.get('sno'))
        value.append(request.form.get('sname'))
        value.append(request.form.get('sex'))
        value.append(request.form.get('sage'))
        value.append(request.form.get('sdept'))
        return insert("student",value)
    elif cno!="":
        value.append(request.form.get('cno'))
        value.append(request.form.get('cname'))
        value.append(request.form.get('cpno'))
        value.append(request.form.get('ccredit'))
        return insert("course",value)
    else:
        return render_template("blank_operation.html")


@app.route('/before_delete', methods=['GET', 'POST'])
def before_delete():
    return render_template('before_delete.html')

@app.route('/after_delete', methods=['POST'])
def after_delete():
    sno = request.form.get('sno')
    cno = request.form.get('cno')
    if sno!="":
        return delete("student",sno)
    elif cno!="":
        return delete("course",cno)
    else:
        return render_template("blank_operation.html")
    

@app.route('/before_update', methods=['GET', 'POST'])
def before_update():
    return render_template('before_update.html')

@app.route('/after_update', methods=['POST'])
def after_update():
    dic={}
    sno = request.form.get('sno')
    cno = request.form.get('cno')
    if sno!="":
        sname=request.form.get('sname')
        sex=request.form.get('sex')
        sage=request.form.get('sage')
        sdept=request.form.get('sdept')
        if(sname!=""):
            dic['sname']=sname
        if(sex!=""):
            dic["sex"]=sex
        if(sage!=""):
            dic["sage"]=sage
        if(sdept!=""):
            dic["sdept"]=sdept
        if dic!={}:
            return update("student",dic,sno)
        else:
            return render_template("blank_update_content.html")


    elif cno!="":
        cname=request.form.get('cname')
        cpno=request.form.get('cpno')
        ccredit=request.form.get('ccredit')
        if cname!="":
            dic['cname']=cname
        if cpno!="":
            dic['cpno']=cpno
        if ccredit!="":
            dic['ccredit']=ccredit
        if dic!={}:
            return update("course",dic,cno)
        else:
            return render_template("blank_update_content.html")
    else:
        return render_template("blank_operation.html")

@app.route('/before_query', methods=['GET'])
def before_query():
    return render_template('before_query.html')

@app.route('/after_query', methods=['POST'])
def after_query():
    sno = request.form.get('sno')
    cno = request.form.get('cno')
    if sno!="":
        return query("student",sno)
    elif cno!="":
        return query("course",cno)
    else:
        return render_template("blank_operation.html")

@app.route('/end', methods=['GET', 'POST'])
def end_page():
    end()
    return "<h1>Terminated</h1>"

@app.route('/showall',methods=[ 'GET', 'POST'])
def showall_page():
    return showall()


if __name__ == '__main__':
    init();
    app.run(host='0.0.0.0', port=80)