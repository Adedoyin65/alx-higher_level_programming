#!/bin/bash

# MySQL credentials
MYSQL_USER="Eden65"
MYSQL_PASSWORD="Hazard6509035379295*"
DATABASE_NAME="hbtn_0c_0"

# Command to create database (if not exists)
CREATE_DATABASE_CMD="CREATE DATABASE IF NOT EXISTS $DATABASE_NAME;"

# Execute MySQL command to create the database
mysql -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" -e "$CREATE_DATABASE_CMD"
