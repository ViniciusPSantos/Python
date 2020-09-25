from PythonStrings.extratorArgumentosUrl import extratorArgumentosUrl

url = "https://bytebank.com/cambio?moedaorigem=moedadestino&moedadestino=dolar"

argumentosUrl = extratorArgumentosUrl(url)
moedaOrigem,moedaDestino = argumentosUrl.extraiArgumentos()

print(moedaDestino,moedaOrigem)

