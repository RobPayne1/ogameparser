import psycopg2, logging
from psycopg2 import sql
from configparser import ConfigParser

class DatabaseSetup:
    def config(self, filename='database.ini', section='postgresql'):
        # create a parser & read config file
        parser = ConfigParser()
        parser.read(filename)

        # get section, default to postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))

        return db

    def connect(self):
        """ Connect to the PostgreSQL database server """
        conn = None
        try:
            # read connection parameters & connect to PostgreSQL server
            params = self.config()
            conn = psycopg2.connect(**params)
            
            # create a cursor
            cur = conn.cursor()
            
            #Look through tables in database to see if there is already a players table created for this client
            tableName = 'players'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerName\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerStatus\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerAlliance\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerTotalPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerTotalScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerResearchPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerResearchScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelShips\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryLostPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryLostScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryBuiltPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryBuiltScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryDestroyedPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryDestroyedScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHonorPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHonorScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformTechnologyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformTechnologyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformDiscoveriesPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformDiscoveriesScore\" int8;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Beginning next table check.")

            #Look through tables in database to see if there is already an alliances table created for this client
            tableName = 'alliances'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceName\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTag\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"founderID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"foundDate\" integer;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceOpen\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"alliancePlayerCount\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLogo\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTotalPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTotalScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceResearchPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceResearchScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryLostPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryLostScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryBuiltPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryBuiltScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryDestroyedPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryDestroyedScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHonorPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHonorScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformTechnologyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformTechnologyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformDiscoveriesPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformDiscoveriesScore\" int8;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Beginning next table check.")

            #Look through tables in database to see if there is already a planets table created for this client
            tableName = 'planets'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Removing rows and beginning next table check.")
                SQL = "DELETE FROM public.\"%s\"" % tableName
                cur.execute(SQL)
                conn.commit()

            #Look through tables in database to see if there is already a players table created for this client
            tableName = 'playersDaily'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerName\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerStatus\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerAlliance\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerTotalPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerTotalScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerResearchPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerResearchScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHighLevelShips\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryLostPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryLostScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryBuiltPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryBuiltScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryDestroyedPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryDestroyedScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHonorPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerMilitaryHonorScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformTechnologyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformTechnologyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformDiscoveriesPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerLifeformDiscoveriesScore\" int8;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Beginning next table check.")

            #Look through tables in database to see if there is already an alliances table created for this client
            tableName = 'alliancesDaily'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceName\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTag\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"founderID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"foundDate\" integer;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceOpen\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"alliancePlayerCount\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLogo\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTotalPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceTotalScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceResearchPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceResearchScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryLostPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryLostScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryBuiltPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryBuiltScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryDestroyedPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryDestroyedScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHonorPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceMilitaryHonorScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformHighLevelPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformHighLevelScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformEconomyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformEconomyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformTechnologyPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformTechnologyScore\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformDiscoveriesPosition\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"allianceLifeformDiscoveriesScore\" int8;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Beginning next table check.")

            #Look through tables in database to see if there is already a planets table created for this client
            tableName = 'planetsWeekly'
            SQL = "SELECT tablename FROM pg_catalog.pg_tables WHERE tablename = (%s)"
            SQLdata = (tableName, )
            cur.execute(SQL, SQLdata)
            tableinfo = cur.fetchone()
    
            #If a table isn't created in Supabase then create one. If it is, then don't worry about creating one.
            if tableinfo is None:
                logging.info(tableName + " table for client doesnt exist. Creating now.")
                cur.execute(sql.SQL("CREATE TABLE {} ();").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"id\" int8 PRIMARY KEY;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"playerID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet1Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet2Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet3Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet4Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet5Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet6Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet7Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet8Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9ID\" int8;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9Name\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"planet9Coords\" text;").format(sql.Identifier(tableName)))
                cur.execute(sql.SQL("ALTER TABLE {} ADD COLUMN \"fetchDate\" timestamptz;").format(sql.Identifier(tableName)))
                conn.commit()
            else:
                logging.info(tableName + " table for client exists in database. Beginning next table check.")

            # close the communication with the PostgreSQL
            cur.close()

        except (Exception, psycopg2.DatabaseError) as error:
            logging.info(error)
        finally:
            if conn is not None:
                conn.close()
                logging.info('Database connection closed.')
