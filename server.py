from flask import Flask, render_template, session, redirect

app = Flask (__name__)
app.secret_key = 'secretcode'

@app.route('/', methods=['GET'])
def count(): 
    if 'num_times' in session:
        session['num_times'] = int(session['num_times']) + 1
    else:
        session['num_times'] = 1
    return render_template('index.html')

@app.route('/destroy_session', methods=['GET'])
def destroy():
    session.pop('num_times')
    return redirect('/')



if __name__ == ('__main__'):
    app.run(debug=True) 
