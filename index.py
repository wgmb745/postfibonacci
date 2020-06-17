import json
import datetime


def handler(event, context):
    n = int(9)
    lista = 'Vacio'
    data = {
        'numero':n,
        'fibonacci':lista,
        'timestamp':datetime.datetime.utcnow().isoformat()
    }
    
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}
    }
