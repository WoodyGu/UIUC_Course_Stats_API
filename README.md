# UIUC_Course_Stats_API
## An API returning the statistics of every courses in UIUC

## Base URL: https://fa18-cs242-finalproject-api.herokuapp.com/

GET /api/course/<string:Subject>/<string:Number>
Example https://fa18-cs242-finalproject-api.herokuapp.com/api/course/cs/225
Expected return value: 
{"Average_GPA":2.89,"Course_Title":"Data Structures","Grade_Distribution":[{"A+":418},{"A":2378},{"A-":910},{"B+":586},{"B":1113},{"B-":401},{"C+":356},{"C":642},{"C-":154},{"D+":51},{"D":453},{"D-":33},{"F":380}],"Instructors":[{"Average_Grade":2.87,"name":"Earls, John C"},{"Average_Grade":3.06,"name":"Fagen-Ulmschnei, Wade A"},{"Average_Grade":2.86,"name":"Geigle, Chase A"},{"Average_Grade":2.96,"name":"Heeren, Cinda"},{"Average_Grade":2.23,"name":"Karahan, Ibrahim"},{"Average_Grade":2.49,"name":"Kassa, Debessay F"},{"Average_Grade":2.8,"name":"Massung, Sean A"},{"Average_Grade":2.46,"name":"Singh, Varun K"},{"Average_Grade":2.6,"name":"Toole, John D"},{"Average_Grade":2.84,"name":"Yershova, Ganna"}],"Number":"225","Status":"200 OK","Subject":"CS","Total_Students":7954}



