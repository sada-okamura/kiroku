FROM alpine:3.12.2
MAINTAINER sada.okamura@gmail.com

RUN apk --update add --no-cache rsyslog logrotate sudo

COPY rsyslog.conf /etc/
COPY rsyslog.d /etc/rsyslog.d

COPY logrotate.d /etc/logrotate.d
COPY logrotate.sh /etc/periodic/hourly/

RUN mkdir /code
WORKDIR /code
COPY docker-entrypoint.sh /code

RUN	adduser -s /bin/ash -D rsyslog rsyslog \
	&& echo "rsyslog ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/rsyslog \
    && chmod 0440 /etc/sudoers.d/rsyslog \
    && mkdir /syslog \
    && chown -R rsyslog:adm /syslog \
    && chown -R rsyslog:adm /var/log

CMD ["/usr/sbin/rsyslogd", "-n"]
ENTRYPOINT ["/code/docker-entrypoint.sh"]
