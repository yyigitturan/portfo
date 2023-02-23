from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

print(__name__)
@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data["email"]
        subject= data["subject"]
        message = data["message"]
        file = database.write(f'\n{email}, {subject}, {message}')
def write_to_csv(data):
    with open('database.csv',newline='', mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',   quotechar=';', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #Ｅｍａｉｌ ａｄｄｒｅｓ ｉｓ ｒｅｑｕｉｒｅｄ
    if request.method == 'POST':
        if request.method == 'POST':
            email = request.form['email']
            if not email:
                return render_template('error.html', message='Ｅｍａｉｌ ａｄｄｒｅｓ ｉｓ ｒｅｑｕｉｒｅｄ')
            else:
                # email address is not empty, process the form
                # ...
                return render_template('contact.html')
        else:
            return render_template('index.html')
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou.html')
        except:
            return 'did not save database'
    else:
        return 'Something went wrong. Please try again. '
