from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import extcolors
import pyperclip


app = Flask(__name__)
Bootstrap(app)
UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "FNP-'?VKXU(6Uk#q_W!^Snz"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def home():
    limit = 10
    path=f"{app.config['UPLOAD_FOLDER']}example.jpg"
    if request.method == "POST":
        f = request.files['file']
        limit = request.form['limit']
        filename = secure_filename(f.filename)
        if filename != "" and request.form['limit'] != "":
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            path = f"{app.config['UPLOAD_FOLDER']}{filename}"

    colors, pixel_count = extcolors.extract_from_path(path, limit=limit)
    colors_to_display = [['#%02x%02x%02x' % rgb, round((pixels_of_colors)/pixel_count*100, 2)] for rgb, pixels_of_colors in colors]

    return render_template('index.html', image=path, colors=colors_to_display)



if __name__ == '__main__':
    app.run(debug=True)