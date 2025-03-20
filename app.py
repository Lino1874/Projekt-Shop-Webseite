from flask import Flask, render_template, request # type: ignore
 
app = Flask(__name__) 


@app.route('/add_book', methods=['GET', 'POST']) 

def add_book(): 

    

    if request.method == 'POST': 

        title = request.form['title'] 

        price = request.form['price'] 

        condition = request.form['condition'] 




         # Debug-Ausgabe 

        print(f"Titel: {title}, Preis: {price}, Zustand: {condition}") 


        

    

        return "Die Daten wurden erfolgreich übermittelt!" 
    
    

@app.route('/', methods=['GET', 'POST']) 

def home(): 

    return render_template ("index.html") 
 
if __name__ == '__main__':
    app.run(debug=True)  