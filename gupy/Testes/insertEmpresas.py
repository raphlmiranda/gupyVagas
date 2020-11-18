import requests
import json
import bs4

base_url = 'http://127.0.0.1:8000'

class checkVagas:

    def __init__(self):
        self.req = requests.get(f'{base_url}/empresas/').json()

    def insertVagasRest(self, name, depart, link, date, id_empresa):
        r = requests.post(f'{base_url}/vagas/',
                        data=json.dumps(
                            {
                                "name": name,
                                "depart": depart,
                                "link": link,
                                "data": date,
                                "id_empresa": id_empresa
                            }
                            ),
                        headers={'Content-Type': 'application/json'}
                        )
    
    def checkExistVaga(self, vaga):
        r = requests.get(f'{base_url}/vagas/',
                headers={'Content-Type': 'application/json'}
                ).json()

        for req in r:
            if req['name'] in vaga:
                return True

    def extractVagas(self):
        import datetime
        for empresa in self.req:
            if empresa['status'] == 200:
                soup = bs4.BeautifulSoup(requests.get(f'http://{empresa["name"]}.gupy.io').text, 'html.parser')
                div = soup.findAll("div", {"class": "job-list jobs-to-filter"})
                for td in div[0].findAll('tr'):
                    dump = []
                    for span in td.findAll("span"):
                        dump.append(span.text.replace('\n', '').replace('  ', '').replace('            ', '').replace('          ', ''))
                    if not self.checkExistVaga(dump[0]):
                        # print('--------------------------------------')
                        # print(dump, f'http://{empresa["name"]}.gupy.io/')
                        self.insertVagasRest(
                                dump[0], 
                                dump[1], 
                                f'http://{empresa["name"]}.gupy.io{td.find("a", {"class": "job-list__item"})["href"]}', 
                                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d'), 
                                f'{empresa["id"]}'
                            )
                    else:
                        pass

checkVagas().extractVagas()
