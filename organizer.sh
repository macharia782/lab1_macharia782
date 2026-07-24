#!/usr/bin/env bash
# Archives grades.csv and logs the operation

ARCHIVE_DIR="archive"

CSV_FILE="grades.csv"

LOG_FILE="organizer.log"

mkdir -p "$ARCHIVE_DIR"

if [ ! -f "$CSV_FILE" ]; then
    echo "Error: $CSV_FILE not found."
    exit 1
fi

TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

ARCHIVED_FILE="${CSV_FILE%.csv}_${TIMESTAMP}.csv"

mv "$CSV_FILE" "$ARCHIVE_DIR/$ARCHIVED_FILE"

touch "$CSV_FILE"

echo "[$TIMESTAMP] Archived $CSV_FILE as $ARCHIVE_DIR/$ARCHIVED_FILE" >> "$LOG_FILE"

echo "Archive completed successfully."
echo "Archived file: $ARCHIVE_DIR/$ARCHIVED_FILE"
echo "A new empty grades.csv has been created."
echo "Log updated: $LOG_FILE"