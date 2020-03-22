# Cloud Alarm Notifier

The objective of this project is to create a simple and easy to use alarm system that is compatible with popular chat communication systems such as Discord, Slack, etc.

For running this software we currently support:

- AWS Lambda

Future planned support platforms:

- Google Functions
- Azure Functions

For outputting the alarms we currently support:

- Discord

Future planned output destinations:

- Slack

## Where to Download

If you want to download a copy of this software, then simply go to the Releases section and download the appropriate zip file you are looking for.

## How to install developer dependencies

### AWS Lambda

Install requirements locally for AWS Testing

`pip install -e .[aws-lambda]`