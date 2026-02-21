# GitHub to Jira Automation

Automatically creates a Jira ticket when a GitHub issue comment starts with `/jira`.

## Architecture
GitHub Issue Comment → GitHub Webhook → EC2 (Flask App) → Jira REST API

## Tech Stack
- Python
- Flask
- GitHub Webhooks
- AWS EC2
- Jira REST API

## Secret Management
**EC2:** Add to `~/.bashrc` and source it
```bash
export JIRA_TOKEN=yourtoken
export JIRA_EMAIL=youremail@gmail.com
```
**Local:** Create a `.env` file (never pushed to GitHub)

## Setup
1. Clone the repo
2. Set environment variables
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`

## Proof of Working
Screenshots in `docs/` folder:
- Webhook delivery (200 OK)
- EC2 terminal logs
- Jira dashboard ticket creation