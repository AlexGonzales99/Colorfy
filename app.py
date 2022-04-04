import os.path
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import color

app = Flask(__name__)
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/')
def hello_world():  # put application's code here
    #process()
    return render_template('home.html')

@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    filterType = request.form.get('filters')  # Gets the fiter type from the dropdown menu
    if request.method == 'POST':
            upFile = request.files['file']
            filename = secure_filename(upFile.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)[1]
            upFile.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    filter(upFile, filterType)
    return render_template('uploader.html')

@app.route("/filter")
def filteredFile(f):
        #print(f.filename)
        return render_template("filtered.html")

def filter(f, filtertype):  # Do filter stuff <--- return a new filtered file
        print(f.filename)
        print(filtertype)
        color.colorDetection(filtertype, f.filename)

if __name__ == '__main__':
    app.run()
