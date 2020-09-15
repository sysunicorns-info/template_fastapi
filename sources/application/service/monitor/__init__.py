from application.database import Database

class MonitorService():
    """
    """

    database: Database = None

    def __init__(self, database: Database):
        """
        """
        self.database = database

    async def get_health_report(self) -> dict:
        """
        """
        if isinstance(self.database, Database):
            return {
                'health': True,
                'database': {
                    'health': self.database.health,
                    'pool_minsize': self.database.engine.minsize,
                    'pool_maxsize': self.database.engine.maxsize,
                    'pool_size': self.database.engine.size,
                    'pool_freesize': self.database.engine.freesize,
                    'closed': self.database.engine.closed,
                }
            }
        else:
            return {
                'health': False,
                'database': None
            }
