from flask import Flask, render_template, request, url_for, flash, redirect
import friends
import map
import urllib

app = Flask(__name__)
app.config['SECRET_KEY'] = '1e21885e0fbc0f7b7bbe1a49996639411a44124d2d45f679'

messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/map/')
def maper():
    return render_template('map.html', messages=messages)

@app.route('/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        nickname = request.form['title']
        count = request.form['content']
        if not nickname:
            flash('Nickname is required!')
        if not count.isnumeric():
            flash('Right count is required!')
        else:
            try:
                messages = []
                data = friends.search(nickname, count)
                friends_list = {}
                locations_with_friends = {}
                for elem in data['users']:
                    friends_list[elem['screen_name']] = elem['location']
                    try:
                        locations_with_friends[elem['screen_name']] = map.coordinate_finder(elem['location'])
                        messages.append({'title': elem['screen_name'], 'content': elem['location']})
                    except:
                        pass
                map.map(locations_with_friends)
                return redirect(url_for('maper'))
            except urllib.error.HTTPError:
                flash('Try other nickname or try later!')
    return render_template('index.html')
