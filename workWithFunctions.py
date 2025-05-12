import json
import os

alunos_json = "alunos.json"
alunos = []

def carregas_dados(alunos):
    if os.path.exists(alunos_json):
        with open(alunos_json, "r", encoding="utf-8") as get_alunos:
            alunos = json.load(get_alunos)
            return alunos
    return alunos

print(carregas_dados(alunos))