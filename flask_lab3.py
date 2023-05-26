from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/number', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        a = int(request.form.get('a'))
        b = int(request.form.get('b'))
        c = int(request.form.get('c'))
        D= Diskriminant(a,b,c)
        x=roots(D,a,b,c)
    return render_template('index.html',x1=x[0],x2=x[1])


def Diskriminant(a,b, c):
        D=b*b-4*a*c
        return D

def roots(D,a,b,c):
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x2=(-b-math.sqrt(D))/(2*a)
        return x1, x2
    elif D==0:
        x=(math.sqrt(D))/(2*a)
        return x
    elif D<0:
        return 'корней нет'
    elif c==0:
        x1=0
        x2=-b/a
        return x1,x2
    elif b==0 and c<0:
        x1 = math.sqrt(abs(c))
        x2 = -math.sqrt(abs(c))
        return x1,x2










