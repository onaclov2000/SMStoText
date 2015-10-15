#!/usr/bin/env python2.7
import re
import sys
import argparse as ap


def count_messages(fileName):
    """
    Count the number of text messages received by all contacts in the
    data set.
    """

    try:
        with open(fileName, 'r') as file_:
            contacts = {}

            header = file_.readline()
            for line in file_:

                # Check to see that the first thing in the line is a date
                text_line = re.search(r'^\d+?[/-]\d+?[/-]\d+?,', line, flags=re.UNICODE)

                # Just to be sure, make sure it's not JUST a date.
                if len(line.split(',')) < len(header.split(',')):
                    continue

                if text_line:
                    row = line.split(',')
                    date, time, type_, number, contactName = row[0:5]
                    msgBody = ''.join(row[5:])
                    msgBody = msgBody.replace('\r\n', '')
                    contactName = contactName.replace('+', '')
                    if contactName not in contacts:
                        contacts[contactName] = 1
                    else:
                        contacts[contactName] += 1
    except:
        sys.stderr.write("Could not open file: {0}!\n".format(fileName))
        return

    for contact in sorted(contacts.keys()):
        print "File: {0}".format(fileName)
        print "Name: {0} - {1:,} messages\n".format(contact, contacts[contact])

def search_messages(fileName, word):
    """
    Searches the message data for the specified words.
    """

    try:
        with open(fileName, 'r') as file_:
            for line in file_:
                if word.lower() in line.lower():
                    print line.strip()
    except:
        sys.stderr.write("Could not open file: {0}!\n".format(fileName))
        return
    

def run(args):
    """
    Main entry point of the script. Manages passing args to each
    function.
    """

    if args.count:
        for each in args.files:
            count_messages(each)

    # Search for words!
    debug=False
    if debug:
        for each in args.files:
            search_messages(each, "http")

if __name__ == "__main__":
    descStr = "Parses the text data from SMSToText"
    parser = ap.ArgumentParser( description=descStr )
    parser.add_argument( '--count', default=False, action='store_true')
    parser.add_argument( 'files', default='./input.csv', nargs='*',
                         help="Files to be parsed")
    args = parser.parse_args()
    run( args )
