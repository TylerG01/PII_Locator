# README 
The goal of this repository is to create a series of easy-to-use utilities which find Personally Identifiable Information (PII) in large volumes of user data, stored in CSV format, using regex to search for patterns. When PII is located, the entire row is copied to an output file, with all subsequent rows appended to the same file. Currently, this includes:
1. Full Name
2. National ID (Generic)
3. Country-Specific National ID# for US, CA, AUS and 24 Euro countries
4. Phone number for any coutnry
5. Passport Numbers (by country) for the US, Canada, Australia and 24 European countries
6. Drivers License for US, CA, AUS and 24 Euro countries
7. Mailing address
8. IP address
9. MAC Address
10. IMEI
11. Race / Ethnicity
12. Gender
There is a lot of room for improvement, as I slapped this script together in a rush, for a project I was working on where a solution was needed to iterate through several Terabytes of data. Future version will use in-memory batch processing.

## Requirements
This script uses csv, re and os libraires....nothing special.

### Use
Change variable values in lines 6, 7 and 8 of this script to your desired directories, then execute the script. 

**Warning:** Tools in this repository are not recommended for use within cleaned breach-data sets.
## Future Development
1. Expanded PII fields
2.	Support for locating passwords by common policies.
3.	In-Memory version of PII_Main.py to iterated through a large file in chunks.
