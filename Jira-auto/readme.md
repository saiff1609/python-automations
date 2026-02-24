# GitHub → Jira Automation

> Trigger Jira ticket creation directly from a GitHub issue comment using `/jira`

---

## How It Works

A user comments `/jira` on any GitHub issue. GitHub fires a webhook to an EC2-hosted Flask server, which validates the comment, then calls the Jira REST API to create a ticket — all in seconds, no manual Jira interaction needed.

```
User types /jira in GitHub issue comment
            │
            ▼
   GitHub detects a comment event
   fires POST request (JSON payload)
            │
            ▼
   EC2 Flask server receives a request
   extracts comment body
            │
         /jira? ──── No ──→ Returns 200, ignored
            │
           Yes
            │
            ▼
   Calls Jira REST API (HTTPBasicAuth)
            │
            ▼
   Ticket created in the Jira project
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| 🐍 Language | Python 3 |
| 🌐 Web Framework | Flask |
| ☁️ Cloud | AWS EC2 (Ubuntu) |
| 🔗 Trigger | GitHub Webhooks |
| 🎫 Destination | Jira REST API v3 |
| 🔐 Auth | HTTPBasicAuth + API Token |

---

---

## Environment Variables

This project uses two secrets — never hardcoded, never pushed to GitHub.

| Variable | Description |
|----------|-------------|
| `JIRA_TOKEN` | Jira API token (generated from Atlassian account settings) |
| `JIRA_EMAIL` | Email linked to your Atlassian account |

### Setting up on EC2 (permanent)

SSH into your EC2 instance and add the variables to `.bashrc` so they persist across sessions:

```bash
nano ~/.bashrc
```

Add these lines at the bottom:

```bash
export JIRA_TOKEN="your-api-token-here"
export JIRA_EMAIL="your-email@gmail.com"
```

Save and apply:

```bash
source ~/.bashrc
```

Verify they're set:

```bash
echo $JIRA_TOKEN
echo $JIRA_EMAIL
```

### Setting up locally

Create a `.env` file in the project root (already in `.gitignore` so it won't be pushed):

```
JIRA_TOKEN=your-api-token-here
JIRA_EMAIL=your-email@gmail.com
```

---

## Setup & Run

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/python-automations.git
cd python-automations/jira-auto
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set environment variables**

Follow the environment variable setup above for your platform (EC2 or local).

**4. Run the server**
```bash
python app.py
```

Server starts on `http://0.0.0.0:6767`

**5. Configure GitHub Webhook**

Go to your GitHub repo → Settings → Webhooks → Add webhook:
- **Payload URL:** `http://your-ec2-ip:6767/createJira`
- **Content type:** `application/json`
- **Event:** Issue comments

**6. Trigger it**

Comment `/jira` on any issue in that repo. The ticket appears in Jira within seconds.

---

## Proof of Working

| Screenshot | What it shows |
|-----------|---------------|
| [Webhook Delivery](./docs/webhook-delivery.png) | GitHub received 200 OK — server processed the request |
| [EC2 Logs](./docs/ec2-logs.png) | Flask server received webhook and triggered Jira call |
| [Jira Dashboard](./docs/jira-dashboard.png) | Ticket created in Jira project |

---

## What I Learned

- How webhooks work — event-driven architecture vs polling
- Deploying a Python server on EC2 and keeping it accessible
- Calling REST APIs with token-based authentication
- Used environment variables properly for secret management
- Filtering webhook events with conditional logic to avoid noise
