from flask import render_template 
from flask import make_response 
from flask import request
from flask import current_app as app
from flask import flash
from flask import session

# Local library
from .reportConfig import Configurator
from .reportConfig import MongoDB
from .reportAnalysis import TweetAnalyzer

@app.route('/', methods=['GET'])
def root():
      return render_template('home.j2')

@app.route('/config', methods=['GET', 'POST'])
def config():
      if request.method == 'POST':
            try:
                  key_word = request.form.get('key_word').lower()
                  reportType = request.form.get('reportType')
                  numTweets = request.form.get('numTweets')
            except:
                  make_response('Unsupported request', 400)
            else:
                  conf = Configurator(
                        key_word=key_word, 
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
            try:                                    
                  rtype = request.form.get('rtype')
                  if rtype == '1':
                        kword = request.form.get('profile_report')
                  elif rtype == '0':
                        kword = request.form.get('hashtag_report')
            except:
                  make_response('Unsupported request', 400)
            else:
                  ana = TweetAnalyzer(rtype=rtype, kword=kword)
                  ana.analyze()
                  return render_template('dashboard.j2', kword=kword.replace('#', ''), rtype=rtype)
      else:            
            reports = MongoDB().get_reports()
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