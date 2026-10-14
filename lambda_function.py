
import json

def lambda_handler(event, context):
    name = event.get("name", "Student")

    result = {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"Salem, {name}!",
            "service": "AWS Lambda practice",
            "status": "Success"
        })
    }

    return result


# GitHub Actions арқылы тексеру
if __name__ == "__main__":
    event = {"name": "Student"}
    response = lambda_handler(event, None)

    print("Lambda function result:")
    print(json.dumps(response, indent=4))
