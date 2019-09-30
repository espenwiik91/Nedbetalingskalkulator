import requests
import json
import pandas as pd

#INPUT - bruker input til HTTP request
laanebelop = input("Lånebeløp: ")
rente = input("Rente i prosent (bare tall): ")
terminGebyr = input("Termin Gebyr: ")
utlopsDato = input("Utløpsdato (format: yyyy-mm-dd): ")
saldoDato = input("Saldo dato (format: yyyy-mm-dd): ")
forstInnbetalingDato = input("Første innbetalingsdato (format: yyyy-mm-dd): ")

# DIC med paramtre til JSON objektet
data = {
  "laanebelop": laanebelop,
  "nominellRente": rente,
  "terminGebyr":terminGebyr,
  "utlopsDato":utlopsDato,
  "saldoDato":saldoDato,
  "datoForsteInnbetaling":forstInnbetalingDato,
  "ukjentVerdi":"TERMINBELOP"
}

# JSON POST Request
url = 'https://visningsrom.stacc.com/dd_server_laaneberegning/rest/laaneberegning/v1/nedbetalingsplan'
r = requests.post(url, json=data)

json_data = r.json()

#DIC bestående av arrays
table_data = {
    'Restgjeld': [],
    'Dato': [],
    'Innbetaling':[],
    'Gebyr':[],
    'Renter':[],
    'Total':[]
}

#For loop som itererer gjennom JSON request og legger dataen inn i table_data dic
for each in json_data["nedbetalingsplan"]["innbetalinger"]:
        table_data['Restgjeld'].append(each["restgjeld"]),
        table_data['Dato'].append(each["dato"]),
        table_data['Innbetaling'].append(each["innbetaling"]),
        table_data['Gebyr'].append(each["gebyr"]),
        table_data['Renter'].append(each["renter"]),
        table_data['Total'].append(each["total"])

#Table_data DIC om til pandas dataFrame
df = pd.DataFrame (table_data)        

# Printer ut dataFrame og runder til 2 desimaler
print(df.round(2))
