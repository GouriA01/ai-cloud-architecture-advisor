
## Sample Outputs

### Example 1: Real-time Chat App

Input: Real-time chat app for 1000 users

AI Recommendation:

#### 1. AWS Services Needed and Why

- **Amazon DynamoDB** — Fully managed NoSQL database for storing chat messages and user data
- **Amazon API Gateway** — Create and manage RESTful APIs to route requests to backend
- **AWS Lambda** — Serverless compute to handle business logic and interact with DynamoDB
- **Amazon Cognito** — User authentication, sign-up, sign-in, and access control
- **API Gateway WebSockets** — Real-time bidirectional communication between clients and server
- **Amazon S3** — Store static assets like images and media shared in chat
- **Amazon CloudFront** — CDN for fast global content delivery
- **Amazon Route 53** — Domain name routing with high availability

#### 2. Architecture Flow

1. Users interact via web or mobile client
2. CloudFront serves static content from S3
3. API Gateway routes RESTful requests to Lambda
4. Cognito manages authentication and provides temporary AWS credentials
5. Lambda handles business logic and interacts with DynamoDB
6. DynamoDB stores chat messages and user data
7. API Gateway WebSockets enables real-time communication
8. S3 stores media files referenced in chat

#### 3. Estimated Monthly Cost

| Service | Cost |
|---------|------|
| DynamoDB | $100/month |
| API Gateway | $10/month |
| Lambda | $5/month |
| Cognito | $0.50/month |
| CloudFront | $5/month |
| S3 | $2/month |
| Route 53 | $0.50/month |
| **Total** | **~$127.50/month** |

#### 4. Architecture Diagram

```
Client App (Web/Mobile)
        |
        v
   CloudFront (CDN)
        |
        v
   API Gateway (REST + WebSocket)
        |
        v
   Cognito (Auth) --> Lambda (Business Logic)
                          |
                          v
                      DynamoDB (Chat Messages, Users)
                          |
                          v
                       S3 (Media Storage)
```

---

### Example 2: Food Delivery App

Input: Food delivery app with live tracking

AI Recommendation:**

- **Frontend:** CloudFront + S3 for web app hosting
- **Backend:** API Gateway + Lambda for serverless APIs
- **Database:** DynamoDB for orders and menus
- **Tracking:** Amazon Location Service for live GPS
- **Notifications:** SNS for order status updates
- **Auth:** Cognito for user login
- **Estimated cost:** ~$200/month for 10K users

---

### Example 3: Try These Prompts


python3 advisor.py 

Your app idea: E-commerce site with payments
Your app idea: Video streaming platform like Netflix
Your app idea: ML model serving API
Your app idea: IoT dashboard for 10K devices

