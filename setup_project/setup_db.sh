#!/bin/bash
echo "Creating db and db user..."
cat setup_db.sql | mysql -u root -p
echo "Restoring dump..."
mysql -u root -p iw_db < ../dumps/iw_db_dump.sql
