from models import FireIncidents
import os
import pandas as pd
from utils import get_session
from datetime import date, timedelta

ingestion_date = date.today().strftime("%Y-%m-%d")
tomorrow = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")

class IngestRaw:

    source_url = os.environ["SOURCE_URL"]

    def download(self):
        # schema = FireIncidents.get_json_schema(pandas=True)
        self.data = pd.read_csv(self.source_url)


    def transform(self):
        self.data = self.data.astype(str)
        self.data.columns = self.data.columns.str.replace(" ", "")
        self.array_dicts = self.data.to_dict('records')
        with get_session() as (session, _):
            session.execute(f"""
            CREATE TABLE IF NOT EXISTS {FireIncidents.__tablename__}_{ingestion_date.replace('-', '_')}
            PARTITION OF {FireIncidents.__tablename__}
            FOR VALUES FROM ('{ingestion_date}') to ('{tomorrow}')
            """)
            session.commit()

    def load_to_postgres(self):
        with get_session() as (session, _):
            for d in self.data_dict:
                d.update({"IngestionDate": ingestion_date})
                t = FireIncidents(**d)
                session.add(t)

            session.commit()