from flask import render_template 
from flask import make_response 
from flask import request
from flask import current_app as app
from flask import flash
from flask import session

# Local library
from twitterAnalytics.reportConfig import Configurator
from twitterAnalytics.reportConfig import MongoDB

@app.route('/', methods=['GET'])
def root():
      return render_template('home.j2')

@app.route('/config', methods=['GET', 'POST'])
def config():
      if request.method == 'POST':
            try:
                  lword = request.form.get('lword').lower()
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
            try:                                    
                  rtype = request.form.get('rtype')
                  if rtype == '1':
                        rname = request.form.get('profile_report').replace('#', '')
                  elif rtype == '0':
                        rname = request.form.get('hashtag_report').replace('#', '')
            except:
                  make_response('Unsupported request', 400)
            else:                                    
                  return render_template('dashboard.j2', rname=rname, rtype=rtype)
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