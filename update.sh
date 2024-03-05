#!/bin/sh

# Check if the script is being run as root
if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 1>&2
    exit 1
fi

# Update package lists
echo "Updating package lists..."
apt-get update

# Perform system upgrade
echo "Upgrading system..."
apt-get upgrade -y

# Clean up
echo "Cleaning up..."
apt-get autoclean
apt-get autoremove

echo "System update complete!"
