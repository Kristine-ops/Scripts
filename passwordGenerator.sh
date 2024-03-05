#!/bin/sh

length=12
password=$(LC_ALL=C tr -dc '[:alnum:]' < /dev/urandom | head -c "$length")

echo "Generated password: $password"

