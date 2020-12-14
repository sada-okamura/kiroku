# kiroku

Example implementation of centralized log collection system in docker based deployments.
This example exhibits the interaction between an app (Django) sending logs to remote rsyslog server.

rsyslog protocol can be consumed by other log collectors such as [fluentd](https://www.fluentd.org/) or [LogStash](https://www.elastic.co/logstash) where logs need to be stored in databases.


