from flask import Flask,render_template,request,url_for,redirect
app = Flask(__name__)
@app.route('/ram/')
def rama():
    return redirect(url_for('dem01'))
@app.route('/redirected_page')
def dem01():
    return render_template('index.html')
app.run(use_reloader=True,debug=True)
