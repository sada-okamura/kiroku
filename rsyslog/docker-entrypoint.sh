#!/bin/sh
set -e

# If RSYSLOG_CONF is empty, we want to default to /etc/rsyslog.conf
# This allows the user to overwrite what configuration file is being used
if [ -z "$RSYSLOG_CONF" ]; then
        export RSYSLOG_CONF="/etc/rsyslog.conf"
fi

echo "Using rsyslog configuration file: $RSYSLOG_CONF"

exec  "$@"

