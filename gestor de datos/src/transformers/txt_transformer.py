from src.extractors.txt_extractor import TXTExtractor
from os.path import join
import luigi, os, json

class TXTTransformer(luigi.Task):

    def requires(self):
        return TXTExtractor()

    def run(self):
        result = []
        for file in self.input():
            with file.open() as txt_file:
                # Saltar la primera línea (nombres de los campos)
                next(txt_file)
                
                # Por cada renglón, separa cada registro por ";", 
                for registro in txt_file.read().split(";"):
                    # Procesar los campos de cada registro
                    # Ejemplo de registro: 
                    # 581481,22721,SET OF 3 CAKE TINS SKETCHBOOK,12,12/09/2011 09:07,14.29584,17490,Brazil

                    # En fields, cada posición [] Almacena un campo, separa por ",".
                    # Del ejemplo anterior de registro fields[0] = [581481], que es el número de factura o "Invoice".
                    fields = registro.strip().split(",")
                    
                    if len(fields) >= 8:
                        entry = {

                            # Estos son los nombres de los campos que van en txt.json

                            "description": fields[2],
                            "quantity": fields[3],
                            "price": fields[5],
                            "total": float(fields[3]) * float(fields[5]),

                            # Por ejemplo "La posición 0 es invoice."
                            "invoice": fields[0],
                            "provider": fields[1],
                            "country": fields[7]
                        }
                        result.append(entry)

        with self.output().open('w') as out:
            out.write(json.dumps(result, indent=4))

    def output(self):
        project_dir = os.path.dirname(os.path.abspath("loader.py")) # Agarra la ruta del proyecto ubicando "loader.py"
        result_dir = join(project_dir, "result")
        return luigi.LocalTarget(join(result_dir, "txt.json"))

