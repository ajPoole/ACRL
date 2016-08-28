from flask import Flask,render_template,request
import weather_preset_creator as wp
import cfgparser as cp
app = Flask(__name__)
print app



@app.route('/')
def handler():
    tracknames=[]
    for i in range(len(wp.trackdetails)):
        tracknames.append(wp.trackdetails[i]['name'])
    details = cp.getcfgDetails()
    details['TIME'] = details.pop('SUN_ANGLE')
    details
    keys = ['TIME','SESSION_START','SESSION_TRANSFER','LAP_GAIN']
    return render_template('handle.html',tracks=tracknames,details=details,keys=keys)


@app.route('/upload',methods=['POST'])
def file_upload():
    if request.method=="POST":
            f = request.files['file']
            f.save('server_cfg.ini')

    return 'File uploaded!'

@app.route('/create',methods=['POST'])
def create_config():
    angle = "something went wrong :("
    if request.method=="POST":
        angle = request.form.get("TIME")
    return angle
