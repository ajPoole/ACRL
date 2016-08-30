from flask import Flask,render_template,request,send_from_directory
import weather_preset_creator as wp
import cfgparser as cp
import weather_editor as we
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
    return render_template('handle.html',tracks=tracknames,details=details,keys=keys,title="ACRL Server CFG Creator")


@app.route('/upload',methods=['POST'])
def file_upload():
    if request.method=="POST":
        f = request.files['file']
        f.save('static/server_cfg.ini')
        return 'File uploaded!<a href="/">Go back.</a>'
    else:
        return 'Something went wrong :('

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
    keys = we.getWeatherDictKeys()
    return render_template('weditor.html',title="Add an ACRL Weather Template",keys=keys)

@app.route('/weather/create',methods=['POST'])
def add_weather_template():
    if request.method=="POST":
            values = request.form
            for key,value in values.iteritems():
                print key,value
            return we.addRealisticWeather(values['track'],values['layout'],
            values['name'],values['ambient'],values['track_relative'],
            values['ambient_r'],values['track_r'],values['type'])
