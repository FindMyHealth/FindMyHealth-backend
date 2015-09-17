import sqlite3;
from datetime import datetime, date;
 
conn = sqlite3.connect('banklist.sqlite3')
c = conn.cursor()
c.execute('drop table if exists USER_DATA')
c.execute('create table USER_DATA \
	(id integer primary key autoincrement, \
	hosp_address text, hosp_phone text, \
	lat float, lng float, wait_time float)'
	)

#some sample Swift code as a starting point?
"""
@IBAction func saveData(sender: AnyObject) {
    let dbPATH = FMDatabase(path: databasePath as String)

    if dbPATH.open() {

    	#assumed user is anonymous 
    	#add to the INSERT statement using other data from API call
        let insertSQL = "INSERT INTO USER_DATA (wait_time) VALUES ('\(wait_time.text)')"

        let result = dbPATH.executeUpdate(insertSQL, 
			withArgumentsInArray: nil)

        if !result {
            status.text = "Failed to update database"
            println("Error: \(dbPATH.lastErrorMessage())")
        } else {
			wait_time = ""
        }
    } else {
        println("Error: \(dbPATH.lastErrorMessage())")
    }
}
"""