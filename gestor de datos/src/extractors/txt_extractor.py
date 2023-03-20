
# Este archivo define una tarea de Luigi que se encarga de definir los objetivos (targets)
# para los archivos CSV extraídos del archivo ZIP, para que puedan ser utilizados 
# por otras tareas de procesamiento de datos.

import luigi
import os
from os.path import isfile, join
from src.readers.zip_reader import ZIPReader

class TXTExtractor(luigi.Task):

    def requires(self): # Método que define las tareas que deben ejecutarse antes de esta tarea.
        
        return ZIPReader()

    def output(self): 
        
        # Este método define la salida de la tarea.
        # En este caso, la salida es una lista de objetivos de destino (targets) que representan los archivos de texto plano (txt) extraídos. 
        # <Luigi LocalTarget, path = /...>
        
        project_dir = os.path.dirname(os.path.abspath("loader.py"))
        assets_dir = join(project_dir, "assets")
        files = [f for f in os.listdir(assets_dir) if isfile(join(assets_dir, f))]
        txt_files = [f for f in files if f.endswith(".txt")]
        targets = []
        for file in txt_files:
            targets.append(luigi.LocalTarget(join(assets_dir, file)))
        return targets
        
