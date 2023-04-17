from barcode import EAN13
from barcode.writer import ImageWriter
from datetime import *
import qrcode

for x in range(2):
    agora = datetime.now().strftime('%d%m%y%H%M')
    print(f'Data: {agora}')
    cod_funcionario = 3301
    cod_uva = 11
    codigo_produto = f'{agora}{cod_funcionario}{cod_uva}'

    codigo_barra = EAN13(f'{codigo_produto}', ImageWriter())
    codigo_barra.save(filename=f'{x}-CODIGO DE BARRA - UVA', text=f'{codigo_produto}')

    imagem_qr = qrcode.make(codigo_produto)
    imagem_qr.save(F'{x}-CODIGO QR - UVA.PNG')

    agora = datetime.now().strftime('%d%m%Y%H%M%S')
    imagem_qr2 = qrcode.make(agora)
    imagem_qr2.save(F'{x}-CODIGO QR 2 - UVA.PNG')

    import time