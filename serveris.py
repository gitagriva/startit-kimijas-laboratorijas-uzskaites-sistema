from flask import Flask


app = Flask(__name__)

#sakuma lapa 
@app.route('/')
def index():
    return "Labrīt!!!"

@app.route('/sveiki')
def sveiki():
  return "Nav vairs nekāds rīts!"

@app.route('/sveiki/<vards>')
def sveikiPersona(vards):
  return f"Sveiki {vards} !"  #'sveiki{}'.format(vards)


@app.route('/cik2/<reizinamais>')
def cik2Reizinajums(reizinamais):
  reizinamais = int(reizinamais)
  print(type(reizinamais))
  return str(reizinamais * 2)

@app.route('/cik/<sk1>/<sk2>')
def cik2Summa(sk1,sk2):
  sk1 = int(sk1)
  sk2 = int(sk2)
  return str(sk1 + sk2)

if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)



  