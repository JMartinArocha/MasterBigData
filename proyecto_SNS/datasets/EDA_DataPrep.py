# importación de librerias.
from dataprep.eda import create_report
import pandas as pd
import pdfkit

# Cargar los datos desde github
marketComplete = "https://media.githubusercontent.com/media/JMartinArocha/MasterBigData/main/proyecto_SNS/datasets/market_operaciones_2017_2.csv"
df = pd.read_csv(marketComplete)

# Crear el reporte
report = create_report(df)
# Guardar el reporte como HTML
report.save(filepath="EDA_DataPrep.html")

# Convertir el archivo HTML a PDF (requiere wkhtmltopdf instalado en tu sistema)
pdfkit.from_file('EDA_DataPrep.html', 'EDA_DataPrep.pdf')




