from barcode import EAN13
from barcode.writer import ImageWriter
from datetime import *
import qrcode


agora = datetime.now().strftime('%d%m%y%H%M')
print(f'Data: {agora}')
cod_funcionario = 111122223333

codigo_produto = f'{cod_funcionario}'

# codigo_barra = EAN13(f'{codigo_produto}', ImageWriter())
# codigo_barra.save(filename=f'{x}-CODIGO DE BARRA - UVA', text=f'{codigo_produto}')

imagem_qr = qrcode.make(codigo_produto)
imagem_qr.save(F'CODIGO QR - FUNCIONARIO.PNG')

import time