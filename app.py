import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

#link del proyecto
#https://console.firebase.google.com/project/formulario-testing/database/formulario-testing/data?hl=es
#credenciales que debes descargar de firebase
cred = credentials.Certificate('./path/to/serviceAccountKey.json')

#identicas el url de la base de datos
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://formulario-testing.firebaseio.com/'
})


def consultar_firebase():
    ref = db.reference('')
    form = ref.get()
    print(json.dumps(form, indent=4, sort_keys=True))


def guardar_firebase():
    ref = db.reference('/')
    ref.set({
            'user': 
                {
                    'user1': {
                        'user_id': 'juan a',
                        'email': '@gmail',
                        'country':'Colombia'
                    },
                    'user2': {
                        'user_id': 'maria',
                        'email': '@gmail',
                        'country':'perú'
                    },
                }
            })

def actualizar_firebase():
    ref = db.reference('/')
    ref = ref.child('user')
    ref.update({
            'user3': {
                'user_id': 'juan',
                'email': '@gmail',
                'country':'Colombia'
            },
    })  


def guardar_UniqueKey_firebase():
    ref = db.reference('boxes')
    ref.push({
            'user': 
                {
                    'user1': {
                        'user_id': 'juan',
                        'email': '@gmail',
                        'country':'Colombia'
                    },
                    'user1': {
                        'user_id': 'juan',
                        'email': '@gmail',
                        'country':'Colombia'
                    },
                }
    })


if __name__ == '__main__':
   guardar_firebase()