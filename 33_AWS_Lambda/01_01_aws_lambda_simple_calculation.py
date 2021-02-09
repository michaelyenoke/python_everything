import json

def lambda_handler(event, context):
    print(event)
    first_num = 10
    second_num = 20
    result = first_num + second_num
    return {
        'statusCode': 200,
        'body': json.dumps(result)  
        # dumps是将dict转化成str格式，loads是将str转化成dict格式
    }
    
    
    
