from flask import Flask,render_template,request,send_from_directory
import weather_preset_creator as wp
import cfgparser as cp
app = Flask(__name__,static_url_path='/static')
print app



@app.route('/')
def handler():
    tracknames=[]
    for i in range(len(wp.trackdetails)):
        tracknames.append(wp.trackdetails[i]['name'])
    details = cp.getcfgDetails()
    details['TIME'] = details.pop('SUN_ANGLE')
    details['TIME'] = wp.sunAngleToTime(int(details.pop('TIME')),False)
    keys = ['TIME','SESSION_START','SESSION_TRANSFER','LAP_GAIN']
    return render_template('handle.html',tracks=tracknames,details=details,keys=keys)


@app.route('/upload',methods=['POST'])
def file_upload():
    if request.method=="POST":
            f = request.files['file']
            f.save('static/server_cfg.ini')

    return 'File uploaded!<a href="/">Go back.</a>'

@app.route('/create',methods=['POST'])
def create_config():
    form = ""
    if request.method=="POST":
        angle = request.form
        for key,value in angle.iteritems():
            form+=str(value)+" "
    return 'Config created! find it here: <a href="static/server_cfg.ini">Download</a>'

@app.route('/weather')
def serve_weditor():
    return render_template('weditor.html')
