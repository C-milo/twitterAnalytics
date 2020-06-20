from flask import Flask, jsonify, render_template, make_response, request
from tweets_collector import run_search, read_users_collection, read_db_and_analyze

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
      if  request.method == 'POST':
            try:
                  twitterUser = request.form.get('twitterUser')
                  saveUser = request.form.get('saveUser')
                  run_search(twitterUser, saveUser)
                  tweets_df = read_db_and_analyze(twitterUser)
                  likes = list(tweets_df['likes'].values)
                  date  = list(tweets_df['date'].values)
                  tweet_len = list(tweets_df['len'].values)
                  data  = {"likes":likes, "date":date, "len":tweet_len}
                  return render_template('index.html', data=data)
            except:
                  make_response('Unsupported request', 400)            
      else:
            data = {"likes": 0, "date": 0}
            return render_template('index.html', data=data)

@app.route('/api/automatic_search', methods=['GET'])
def automatic_search():
      user_list = read_users_collection()
      for x in user_list:
            run_search(x, "False")
      return make_response(str(user_list), 200)

if __name__ == '__main__':
	app.run()
