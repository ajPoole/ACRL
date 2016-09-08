from flask import Flask,render_template,request,send_from_directory,jsonify,url_for
import weather_preset_creator as wp
import cfgparser as cp
import weather_editor as we
app = Flask(__name__,static_url_path='/static')
print app


@app.route('/')
def handler():
    tracknames=sorted(getTracks())
    details =cp.getcfgDetails()
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
        print form
    return 'Config created! find it here: <a href="static/server_cfg.ini">Download</a>'

@app.route('/weather')
def serve_weditor():
    request.script_root = url_for('serve_weditor', _external=True)
    tracks=sorted(getTracks())
    keys = we.getWeatherDictKeys()
    keys = sorted(keys)
    return render_template('weditor.html',title="Add an ACRL Weather Template",keys=keys,tracks=tracks)

@app.route('/weather/create',methods=['POST'])
def add_weather_template():
    if request.method=="POST":
        values = request.form

        if values['action']=="Add":
            if (not we.checkDuplicate(str(values['name']))):
                status = we.addRealisticWeather(str(values['track']),str(values['layout']),str(values['name']),str(values['ambient']),str(values['track_relative']),str(values['ambient_r']),str(values['track_r']),str(values['type']))
                return status+ 'go <a href"/weather">back</a>'
            else:
                return 'Duplicate track!'
        
        elif values['action']=="Edit":
            status = we.editRealisticWeather(str(values['track']),str(values['layout']),str(values['name']),str(values['ambient']),str(values['track_relative']),str(values['ambient_r']),str(values['track_r']),str(values['type']),False)
            return status+ 'go <a href"/weather">back</a>'

        elif values['action']=="Remove":
            status = we.editRealisticWeather(str(values['track']),str(values['layout']),str(values['name']),str(values['ambient']),str(values['track_relative']),str(values['ambient_r']),str(values['track_r']),str(values['type']),True)
            return status+ 'go <a href"/weather">back</a>'
        else:
            return "Something wrong happened."



@app.route('/weather/get_edit')
def get_json_track():
    name = request.args.get('trackname',"NaN",type=str)
    print name
    for i in range(len(wp.trackdetails)):
        if wp.trackdetails[i]['name']==name:
            details=wp.trackdetails[i]
            break
    
    return jsonify(details)





def getTracks():
    tracknames=[]
    for i in range(len(wp.trackdetails)):
        tracknames.append(wp.trackdetails[i]['name'])
    return tracknames
