from csv_class import CsvProcessor

arquivo_csv = './exemplo.csv'
coluna = 'estado'
valor = 'SP'


csv_processor = CsvProcessor(arquivo_csv)
csv_processor.carregar_csv()
print(csv_processor.filtrar_por(coluna, valor))

print(csv_processor.filtrar_por(coluna, 'SC'))
