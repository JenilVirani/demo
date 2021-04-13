from flask import *

app = Flask(__name__)

@app.route('/')
def Register1():
    return render_template("Registrationform.html")

@app.route('/login', methods=['POST', 'GET'])
def Register():
    if request.method == "POST":
        fname = request.form["fn"]

        lname = request.form["ln"]

        pno = request.form["pn"]

        uname = request.form["email"]

        pword = request.form["pass"]

        gender = request.form["gen"]

        date = request.form["dt"]
        country = request.form["cou"]

        address = request.form["address"]

        hobby = request.form.getlist("hobby")
        h1 = "-".join(hobby)

        # ------------HERE thre are two ways to give o/p on browser see lname  and f
        #  name is print
        # in one line n rest is print individually-----------

        return "Your  Name is : {}  {}<br>".format(fname, lname) + \
               "    Your Phone no is is  : {} <br> ".format(pno) + \
               "  Your Username is : {}  <br>".format(uname) + \
               "  Your Username is : {} <br>".format(pword) + \
               " Your Gender is : {}  <br>".format(gender) + \
               "Your DOB is : {} <br>".format(date) + \
               "  Your Country is is : {}  <br>".format(country) + \
               "Your address is : {} <br> ".format(address) + \
               "Your Hobby are : {}  <br>".format(hobby) + \
               "Your Hobby are : {}  <br>".format(h1)


app.run(port"9009" threaded=True)
