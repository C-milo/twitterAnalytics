from flask import render_template 
from flask import make_response 
from flask import request
from flask import current_app as app
from flask import flash

# Local library
from .reportConfig import Configurator

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
# 
@app.route('/', methods=['GET'])
def root():
      return render_template('dashboard.j2')

@app.route('/config', methods=['GET', 'POST'])
def config():
      if request.method == 'POST':
            try:
                  lword = request.form.get('lword')
                  reportType = request.form.get('reportType')
                  numTweets = request.form.get('numTweets')
            except:
                  make_response('Unsupported request', 400)
            else:
                  conf = Configurator(
                        lword=lword, 
                        reportType=reportType,
                        numTweets=numTweets
                        )
                  conf.readParameters()
                  flash('Configuration saved!', category='alert alert-success')                  
                  return render_template('config.j2')
      else:
            return render_template('config.j2')

@app.route('/report', methods=['GET', 'POST'])
def report():
      if request.method == 'POST':
            return render_template('dashboard.j2')
      else:
            # Temporal value
            reports = ['petrogustavo', 'realDonaldTrump']
            return render_template('report.j2', reports=reports)

@app.route('/contact', methods=['GET'])
def contact():
      return render_template('contact.j2')
# 
# @app.route('/api/automatic_search', methods=['GET'])
# def automatic_search():
#       user_list = read_users_collection()
#       for x in user_list:
#             run_search(x, "False")
#       return make_response(str(user_list), 200)