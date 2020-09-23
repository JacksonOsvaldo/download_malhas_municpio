#!/usr/bin/env python3
# -*- ecoding: utf-8 -*-

import os


# Definindo variável com url do diretório de todos os arquivos do servidor FTP.
url = 'ftp://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2019/UFs/'

# Fazendo download de todos os arquivos utilizando o wget do Linux.
os.system("wget -r {}".format(url))
