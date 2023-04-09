from flask import Flask,render_template,request
import pickle

app=Flask(__name__)
model=pickle.load(open('linear_regresson_model.pkl','rb'))


@app.route("/")
def Home():
    return render_template('text.html')

@app.route("/predict", methods=['POST'])
def predict():
    Weight=0
    if request.method == 'POST':
        Weight=int(request.form['Weight'])
        prediction=model.predict([[Weight]])
        output=round(prediction[0])
        return render_template('text.html',prediction_text="Your Height is{}".format(output))
    else:
        return render_template('text.html',prediction_text="Failed! Try again")


if __name__ == '__main__':
    app.run(debug = True)
                