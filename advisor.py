
import boto3

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

def get_architecture(idea):
    # Send the app idea to Amazon Bedrock and return architecture recommendation
    response = bedrock.converse(
        modelId="us.amazon.nova-micro-v1:0",
        messages=[{
            "role": "user",
            "content": [{"text": f"""You are an AWS Solutions Architect.
For this app idea, recommend:
1. AWS services needed and why (choose ONE service per layer, keep the design minimal, justify any tradeoffs, do not list alternatives)
2. Architecture flow (how services connect)
3. Estimated monthly cost (note: these are rough estimates, not AWS Pricing Calculator figures)
4. Architecture diagram in text format

App idea: {idea}"""}]
        }]
    )
    return response["output"]["message"]["content"][0]["text"]

print("=" * 50)
print("  AI Cloud Architecture Advisor")
print("=" * 50)
print("Describe your app idea (type 'quit' to exit)\n")

while True:
    idea = input("Your app idea: ").strip()
    if idea.lower() == "quit":
        print("Goodbye!")
        break
    print("\nAnalyzing...\n")
    try:
        print(get_architecture(idea))
    except Exception as e:
        print(f"\nError: {e}\n")
    print("\n" + "=" * 50 + "\n")

