# Extraindo vagas de todas empresas que utilizam Gupy como forma de contratação

- Rotas disponíveis

    * Empresas: 
            GET// http://127.0.0.1:8000/empresas/ ( Retorna todas empresas que estão cadastradas no Gupy e com status code ( 200 Ok, 404 Foi excluída ) )
    * Vagas:
            GET// http://127.0.0.1:8000/vagas/ ( Retorna todas as vagas disponíveis )