#!/usr/bin/python

import sys
import datetime

class JournalEntry:
    
    # Class attributes
    timestamp = None
    body = ""

    # init
    def __init__(self, timestamp, body):
        self.timestamp = timestamp
        self.body = body

    # write the journal entry to disk
    def record(self):
        # open journal file
        journal_file = open("journal.txt", "a")

        # write header
        if not self.timestamp:
            # init timestamp to now
            self.timestamp = datetime.datetime.now()

        # TODO: dynamically calculate horizontal rule to be 80 char long
        journal_file.write("\n--- {date}, {time}---\n".format(
            date=self.timestamp.strftime("%m%d%y"),
            time=self.timestamp.strftime("%H:%M")
        ))

        # write body
        journal_file.write(self.body)

        # write footer
        journal_file.write("\n")

        # close journal file
        journal_file.close()

        # return stats
        return len(self.body)

    # read an existing entry from disk
    def read(self, timestamp):
        # open journal file
        journal_file = open("journal.txt", "r")

        # TODO: locate entry for specified timestamp
        # TODO: init with located entry or return error

        # close journal file
        journal_file.close()


def main():
    new_entry = JournalEntry(datetime.datetime.now(), None)

    if len(sys.argv) > 1:
        # collect string argument and store as entry
        new_entry.body = sys.argv[1] + "\n"
        new_entry.record()
    else:
        # print a header for the editing session
        header = "\n>>--- New Journal Entry: {date}, {time} ".format(
            date=new_entry.timestamp.strftime("%m%d%y"),
            time=new_entry.timestamp.strftime("%H:%M")
        )
        for i in range(1, (80 - len(header))):
            header = header + "-"
        header = header + "<<\n"
        print(header)

        # get input to populate entry
        # keep gathering input until a single "." is typed
        # TODO: there's probably a more elegant way to go about this read loop
        input_line = input(">> ")
        new_entry.body = input_line + "\n"

        while input_line != ".":
            input_line = input(">> ")
            # TODO: use modern formatting for this?
            if input_line == ".":
                break
            new_entry.body = new_entry.body + input_line + "\n"

        # record entry and exit
        footer = "\n>>--- {} characters recorded ".format(new_entry.record())
        for i in range(1, (80 - len(footer))):
            footer = footer + "-"
        footer = footer + "<<\n"
        print(footer)


if __name__ == "__main__":
    main()
