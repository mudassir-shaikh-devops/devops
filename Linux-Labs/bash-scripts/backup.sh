#!/bin/bash

# Simple backup script

SOURCE_DIR="/home/user/data"
BACKUP_DIR="/home/user/backup"

DATE=$(date +%Y-%m-%d)

echo "Starting backup..."

cp -r $SOURCE_DIR $BACKUP_DIR/backup-$DATE

echo "Backup completed successfully!"