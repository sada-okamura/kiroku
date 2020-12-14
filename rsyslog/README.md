# rsyslog docker image

This service performs following functions

1. rsyslogd server listening on TCP Port 514 and accepts remote applications to send logs
1. logrotate that rotates remote log files monthly

## How to build an image

```
docker build -t $docker-registy/$image:$tag .
```

## Configurations for Deployments

### rsyslog configurations
Upload custom `rsyslog.conf` file with desired configuration into `/etc/` in the container.
Default configuration listens to TCP 514 and writes log messages to `/var/log/remote` direcotry.

### logrotate configurations
Upload custom logrotate configuration file into `/etc/logrotate.d/` in the container.
Default configuration rotates `/var/log/remote/*.log` monthly and keeps 12 histories.

### **IMPORTANT** Persisting log files
Do not forget to mount `/var/log/remote/` directory as docker volume otherwise log files will be lost when the container is destroyed or updated.

