import mysql.connector

class flights:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host = "database-olap.chgy644asy9m.eu-north-1.rds.amazonaws.com",
                user = 'admin',
                password = 'olapdatabase85',
                database = 'flights_data'
            )
            self.mycursor = self.connection.cursor()
            print('Connection established')

        except:
            print('Conneciton error')


    #  FETCH CITY NAME
    def fetch_city_name(self):
        self.mycursor.execute("""
        SELECT DISTINCT Source FROM flights
        UNION
        SELECT DISTINCT Destination FROM flights
            """)

        data = self.mycursor.fetchall()

        city = []
        for item in data:
            city.append(item[0])

        return city

    def fetch_cities_data(self, source, destination):
        self.mycursor.execute("""
        SELECT * FROM flights
        WHERE Source = '{}' AND Destination = '{}'
        """.format(source, destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_count_flights(self):

        airline = []
        frequency =  []


        self.mycursor.execute("""
        SELECT Airline, COUNT(*) AS 'count' FROM flights
        GROUP BY Airline
        ORDER BY count DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency


    def fetch_bussy_airport(self):
        self.mycursor.execute("""
            SELECT Source, COUNT(*) FROM (
                                SELECT Source FROM flights
                                UNION ALL
                                SELECT Destination FROM flights) t
            
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
        """)

        source = []
        numbers = []

        data2 = self.mycursor.fetchall()

        for item in data2:
            source.append(item[0])
            numbers.append(item[1])

        return source, numbers
