from flask import render_template 
from flask import make_response 
from flask import request
from flask import current_app as app

# Local library
from .tweets_collector import run_search
from .tweets_collector import read_users_collection
from .tweets_collector import read_db_and_analyze

# @app.route('/', methods=['POST', 'GET'])
# def index():
#       if  request.method == 'POST':
#             try:
#                   twitterUser = request.form.get('twitterUser')
#                   saveUser = request.form.get('saveUser')
#                   run_search(twitterUser, saveUser)
#                   tweets_df = read_db_and_analyze(twitterUser)
#                   likes = list(tweets_df['likes'].values)
#                   date  = list(tweets_df['date'].values)
#                   tweet_len = list(tweets_df['len'].values)
#                   data  = {"likes":likes, "date":date, "len":tweet_len}
#                   return render_template('index.html', data=data)
#             except:
#                   make_response('Unsupported request', 400)            
#       else:
#             data = {"likes": 0, "date": 0}
#             return render_template('index.html', data=data)

@app.route('/', methods=['POST', 'GET'])
def home():
      return render_template('dashboard.html')

@app.route('/api/automatic_search', methods=['GET'])
def automatic_search():
      user_list = read_users_collection()
      for x in user_list:
            run_search(x, "False")
      return make_response(str(user_list), 200)