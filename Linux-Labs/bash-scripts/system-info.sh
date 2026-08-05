#!/bin/bash

echo "System Information"
echo "-------------------"

echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "Current User: $(whoami)"
echo "CPU Info:"
lscpu | head -5

echo "Memory Info:"
free -h

echo "Disk Usage:"
df -h