ef lambda_handler(event, context):
    name = event.get("name", "Student")

    return {
        "statusCode": 200,
        "body": f"Salem, {name}! Lambda code is running."
    }


if __name__ == "__main__":
    result = lambda_handler({"name": "GitHub"}, None)
    print(result)
