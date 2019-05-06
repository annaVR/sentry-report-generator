#Sentry Report: Server issues weekly

This tool is created to facilitate creation of Weekly Server Issues Report.
When using the tool, several GET API calls made to Sentry's stats endpoint.
Calls made to retvieve errors from the previous week.
Collected json getting processed and calculations made to display the issue count for each day of the week.

## Getting started
First, login to your Sentry account and create an authentication token for the user with appropriate set of permissions.

Next, run issue_counter.py and on prompt input the authentication token - the issue count will be displayed for each day.

### Further reading
* [Sentry](https://sentry.io/welcome/ "Sentry's homepage") - Open source error tracking software

### Author
* [Anna Romanovskaia](anna.romanovskaia@gmail.com) - ([Github](https://github.com/annaVR))