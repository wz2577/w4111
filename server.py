from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, g
from sqlalchemy import *
app = Flask(__name__)
DATABASEURI = "postgresql://wz2577:9863@34.75.94.195/proj1part2"
engine = create_engine(DATABASEURI)

@app.before_request
def before_request():
  """
  This function is run at the beginning of every web request
  (every time you enter an address in the web browser).
  We use it to setup a database connection that can be used throughout the request.

  The variable g is globally accessible.
  """
  try:
    g.conn = engine.connect()
  except:
    print("uh oh, problem connecting to database")
    import traceback; traceback.print_exc()
    g.conn = None

@app.teardown_request
def teardown_request(exception):
  """
  At the end of the web request, this makes sure to close the database connection.
  If you don't, the database could run out of memory!
  """
  try:
    g.conn.close()
  except Exception as e:
    pass

# ROUTES
@app.route('/')
def welcome():
    recommended = []
    cursor = g.conn.execute("SELECT * FROM game G ORDER BY G.rating desc")
    columns = ["game_id", "name", "genra", "release_date", "about_this_game", "rating"]
    for i in range(3):
        game_info = cursor.fetchone()
        if not game_info:
            break
        recommended.append(dict(zip(columns, game_info)))
    cursor.close()
    print(recommended)
    return render_template('welcome.html', data = recommended)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = str(request.form['query'])
    result = []
    cursor = g.conn.execute("SELECT * FROM game")
    columns = ["game_id", "name", "genra", "release_date", "about_this_game", "rating"]
    for game in cursor:
        if query.lower() in game["name"].lower():
           result.append(dict(zip(columns, game)))
    print(result)
    cursor.close()
    return render_template('search.html', query=query, data=result)   


@app.route('/display/<id>', methods=['GET', 'POST'])
def display(id=None):
    game_data=None
    comment_data=[]
    cursor = g.conn.execute("SELECT * FROM game WHERE game_id::int = " + id)
    game_columns = ["game_id", "name", "genra", "release_date", "about_this_game", "rating"]
    game_info = cursor.fetchone()
    if game_info:
        game_data = dict(zip(game_columns, game_info))
    cursor.close()

    comment_cursor = g.conn.execute("SELECT C.user_id, C.game_id, C.content, C.since, G.name FROM game_user G, comment_make_under C WHERE C.user_id = G.user_id AND C.game_id::int = " + id)
    comment_columns = ["user_id", "game_id", "content", "since", "name"]
    for row in comment_cursor:
        comment_data.append(dict(zip(comment_columns, row)))
    comment_cursor.close()
    if comment_data:
        game_data["comments"] = comment_data
    return render_template('display.html', data=game_data)

@app.route('/patch/<id>', methods=['GET', 'POST'])
def patch(id=None):
    patches = []
    cursor = g.conn.execute("SELECT * FROM have_patch H WHERE H.game_id::int = " + id)
    columns = ["patch_id", "patch_name", "game_id", "patch_notes", "release_date"]
    for row in cursor:
        if not row["patch_name"]:
            row["patch_name"] = "This patch doesn't have a name"
        patches.append(dict(zip(columns, row)))
    cursor.close()
    return render_template('patch.html', data=patches)

@app.route('/userhomepage/<id>', methods=['GET', 'POST'])
def userhomepage(id=None):
    user_data = None
    game_data = []
    user_cursor = g.conn.execute("SELECT GU.name FROM game_user GU WHERE GU.user_id::int = " + id)
    user_columns = ["user_name"]
    user_info = user_cursor.fetchone()
    if user_info:
        user_data = dict(zip(user_columns, user_info))
    user_cursor.close()
    game_cursor = g.conn.execute("SELECT B.game_id, G.name, B.score FROM buy B, game G WHERE B.game_id = G.game_id AND B.user_id::int = " + id)
    game_columns = ["game_id", "game_name", "score"]
    for row in game_cursor:
        game_data.append(dict(zip(game_columns, row)))
    game_cursor.close()
    if game_data:
        user_data["buys"] = game_data
    print(user_data)
    return render_template('userhomepage.html', data=user_data)

if __name__ == '__main__':
    import click
    @click.command()
    @click.option('--debug', is_flag=True)
    @click.option('--threaded', is_flag=True)
    @click.argument('HOST', default='0.0.0.0')
    @click.argument('PORT', default=8111, type=int)
    def run(debug, threaded, host, port):
        HOST, PORT = host, port
        print("running on %s:%d" % (HOST, PORT))
        app.run(host=HOST, port=PORT, debug=debug, threaded=threaded)

run()

