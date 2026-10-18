import boto3, json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def get_architecture(idea):
    response = bedrock.converse(
        modelId="us.amazon.nova-micro-v1:0",
        messages=[{
            "role": "user",
            "content": [{"text": f"""You are an AWS Solutions Architect.
For this app idea, recommend:
1. AWS services needed and why
2. Architecture flow (how services connect)
3. Estimated monthly cost
4. Architecture diagram in text format

App idea: {idea}"""}]
        }]
    )
    return response["output"]["message"]["content"]["text"]

print("=" * 50)
print("  AI Cloud Architecture Advisor")
print("=" * 50)
print("Describe your app idea (type 'quit' to exit)
")

while True:
    idea = input("Your app idea: ").strip()
    if idea.lower() == "quit":
        print("Goodbye!")
        break
    print("
Analyzing...
")
    print(get_architecture(idea))
    print("
" + "=" * 50 + "
")
