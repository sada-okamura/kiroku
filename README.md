# kiroku

Example implementation of centralized log collection system in docker based deployments.
This example exhibits the interaction between an app (Django) sending logs to remote rsyslog server.

rsyslog protocol can be consumed by other log collectors such as [fluentd](https://www.fluentd.org/) or [LogStash](https://www.elastic.co/logstash) where logs need to be stored in databases.


## How to run a demo?

### Prerequisite
* docker and docker-compose must be installed in the demo machine
* port 8000 must be open on the demo machine

### Run the demo

```
./demo.sh
```

### What just happens if successful?
`demo.sh` would launch 2 docker containers defined in `docker-compose.yml`. The first container is kiroku (rsyslog server), the second is django (rsyslog client).
Once contaiers are up, the script would call an API within the api container which then would trigger log enties to be created in `/var/log/remote` directory inside the kiroku container.
