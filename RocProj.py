from flask import Flask, jsonify, render_template, redirect, request, url_for, g
from dblayer import DBlayer
from flaskext.auth import Auth, AuthUser, login_required, logout, get_current_user_data


db = DBlayer()
app = Flask(__name__, static_folder='web/static', static_url_path='')
app.template_folder = "web"
auth = Auth(app)
app.secret_key = 'N4BUdSXUzHxNoO8g'

@app.before_request
def init_users():
    admin = AuthUser(username='admin')
    admin.set_and_encrypt_password('password')
    g.users = {'admin': admin}

@app.route("/")
def feed():
    user = get_current_user_data()
    print user
    return render_template('feed.html', user=user)

    
@app.route("/login",methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in g.users:
            # Authenticate and log in!
            if g.users[username].authenticate(request.form['password']):
                print 'USER '+username+' LOGGED IN'
                return redirect('/admin')
        return redirect('/login')
    return '''
            <form method="POST">
                Username: <input type="text" name="username"/><br/>
                Password: <input type="password" name="password"/><br/>
                <input type="submit" value="Log in"/>
            </form>
        '''

@app.route("/post")
@login_required()
def post():
    user = get_current_user_data()
    return render_template('newpost.html', user=user)
    
@app.route("/admin")
@login_required()
def admin():
    user = get_current_user_data()
    return render_template('admin.html', user=user)

@app.route("/logout")
def signout():
    logout()
    print "logging out"
    return redirect("/")

@app.errorhandler(401)
def custom_401(error):
    return redirect("/login")

if __name__ == '__main__':
    app.run(debug=True)


