
# AI Cloud Architecture Advisor

An AI-powered tool that recommends AWS architectures for your app ideas in seconds, using Amazon Bedrock and Amazon Nova Micro.

## What It Does

Describe your app idea in plain English. The AI recommends:
- The right AWS services and **why** each one fits
- Architecture flow (how services connect)
- Estimated monthly cost (rough ballpark, not Pricing Calculator figures)
- A text-based architecture diagram

## Prerequisites

- An AWS account with an EC2 instance (Amazon Linux) or any environment with Python 3
- An IAM role attached to your EC2 instance (or configured credentials)
- **Amazon Nova Micro enabled** in your region under **Bedrock → Model access**

> **Important:** Model access is not always auto-enabled. Go to the Amazon Bedrock console → Model access → ensure `Amazon Nova Micro` is enabled in your region before running the script.

## Setup (5 Steps)

### Step 1 — Install Python packages

```bash
sudo yum install python3-pip -y
pip3 install boto3
```

> **Note:** These are two separate commands. Run them one at a time.

### Step 2 — Add IAM permissions

Go to IAM Console → Roles → Select your EC2 instance role → Attach the `AmazonBedrockFullAccess` policy.

### Step 3 — Create the Python script

```bash
vi advisor.py
```

Paste the contents of `advisor.py` from this repo.

### Step 4 — Run it

```bash
python3 advisor.py
```

### Step 5 — Ask anything

Try prompts like:
- "E-commerce site with payments"
- "ML model serving API"
- "Video streaming platform"
- "IoT dashboard for 10K devices"

## Tech Stack

| Component | Purpose |
|-----------|---------|
| **Amazon Bedrock** | AI inference engine |
| **Amazon Nova Micro** | Language model (fast, lightweight) |
| **Python 3 + Boto3** | Script and AWS SDK |
| **IAM Role** | Permissions for Bedrock access |
| **Converse API** | Sends prompts to Bedrock |

## Model ID Note

The script uses `us.amazon.nova-micro-v1:0`, which is a **cross-region inference profile**. This is different from `amazon.nova-micro-v1:0` (single-region). If you are retyping the model ID, make sure to use the exact form shown in the code to avoid validation errors.

## Important Caveats

- **Cost estimates are illustrative.** The AI returns rough ballpark numbers (e.g., "~$200/month for 10K users"). These are not based on the AWS Pricing Calculator. Always verify with the [AWS Pricing Calculator](https://calculator.aws/) for real estimates.
- **Always verify service names.** Small models like Nova Micro may occasionally reference services that don't exist (e.g., "Amazon Web Sockets" instead of "API Gateway WebSocket API"). Double-check every recommendation.
- **AI doesn't know your context.** It doesn't know your budget, compliance requirements, team size, or existing infrastructure. Treat recommendations as a starting point, not a final architecture.

## Example Output

**Input:** "Build a food delivery app with live tracking"

**Output:**
- **Frontend:** CloudFront + S3 for web app hosting
- **Backend:** API Gateway + Lambda for serverless compute
- **Database:** DynamoDB for orders and menus
- **Tracking:** Amazon Location Service for live GPS
- **Notifications:** SNS for order updates
- **Auth:** Cognito for user login
- **Estimated cost:** ~$200/month for 10K users

> The actual model output may vary. The prompt is tuned to pick one service per layer, but results depend on the model's interpretation.

## License

MIT
