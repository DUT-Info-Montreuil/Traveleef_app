import psycopg


class PostgresqlDriver:
    _instance = None
    _conn = None

    def __new__(cls):
        # Si l'instance n'existe pas, on la crée
        if cls._instance is None:
            cls._instance = super(PostgresqlDriver, cls).__new__(cls)
            cls._conn = None  # On initialise la connexion à None
        return cls._instance

    def get_db_password(self):
        """Lire le mot de passe depuis le secret du docker-compose."""
        with open('/run/secrets/db_password', 'r') as file:
            return file.read().strip()

    def connect(self):
        """Établit la connexion à la base de données."""
        if self._conn is None or self._conn.closed:
            db_password = self.get_db_password()
            self._conn = psycopg.connect(f'dbname=traveleef user=sae host=db password={db_password}')
        return self._conn

    def close_connection(self):
        """Ferme la connexion si elle est ouverte."""
        if self._conn and not self._conn.closed:
            self._conn.close()

    def execute_query(self, query):
        """Exécute une requête SQL et retourne les résultats."""
        conn = self.connect()
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def __del__(self):
        """Ferme la connexion à la base de données lors de la destruction de l'objet."""
        self.close_connection()
