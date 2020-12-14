FROM alpine:3.12.2
MAINTAINER sadanori.okamura@freestyleiot.com

RUN apk --update add --no-cache rsyslog logrotate sudo

COPY rsyslog.conf /etc/
COPY rsyslog.d /etc/rsyslog.d

COPY logrotate.d /etc/logrotate.d
COPY logrotate.sh /etc/periodic/hourly/
# don't let logrotate complain about missing file
#RUN touch /var/log/messages


RUN mkdir /code
WORKDIR /code
COPY docker-entrypoint.sh /code

RUN	adduser -s /bin/ash -D rsyslog rsyslog \
	&& echo "rsyslog ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/rsyslog \
    && chmod 0440 /etc/sudoers.d/rsyslog \
    && mkdir /syslog \
    && chown -R rsyslog:adm /syslog \
    && chown -R rsyslog:adm /var/log

#USER rsyslog


CMD ["/usr/sbin/rsyslogd", "-n"]
ENTRYPOINT ["/code/docker-entrypoint.sh"]
