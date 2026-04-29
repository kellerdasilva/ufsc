class Ordenacao():

    def ordena(self, array_para_ordenar: list):
        lista_ordenada = []
        numero = array_para_ordenar[0]
        for item in array_para_ordenar:
            if item < numero:
                numero = item
            lista_ordenada.append(numero)
            array_para_ordenar.remove(numero)
        
        print(lista_ordenada)
        
        """Realiza a ordenacao do conteudo do array recebido como parâmetro"""
        ...
        return ...

    def to_string(self, array_ordenado: list):
        """Converte o conteudo do array em String formatado
           Exemplo: 
           Para o conteudo do array: [1,2,3,4,5]
           Retorna: "1,2,3,4,5"
           @return String com o conteudo do array formatado
     """
        ...
        return ...
    
Ordenacao.ordena([4, 3, 2, 1, 5])