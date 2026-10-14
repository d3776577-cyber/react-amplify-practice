
import json

def lambda_handler(event, context):
    name = event.get("name", "Student")

    result = {
        "statusCode": 200,
        "body": {
            "message": f"Salem, {name}!",
            "service": "AWS Lambda",
            "status": "Success"
        }
    }

    return result


if __name__ == "__main__":
    event = {"name": "Student"}

    response = lambda_handler(event, None)

    print("=== AWS Lambda жауабы ===")
    print("Status Code:", response["statusCode"])
    print("Message:", response["body"]["message"])
    print("Service:", response["body"]["service"])
    print("Status:", response["body"]["status"])


