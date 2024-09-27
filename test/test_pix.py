import sys#como o test esta em uma pasta, ele nao consegue acessar normalmente os outros arquivos que estao nas pastas anteriores, se usa o sys para reverter esse problema
sys.path.append('../')#o ../ faz com que volte uma pasta

import pytest
import os
from payments.pix import Pix

def test_pix_create_payment():
    payment_istance = Pix()

    payment_info = payment_istance.create_payment(base_dir='../')#aqui tambem foi necesario fazer uma modificação na classe Pix para
                                                                 #que pudesse reverter o problema do test esta em uma pasta
    print(payment_info)
    assert 'bank_payment_id' in payment_info #se o ank_payment_id nao tiver no payment_info, o teste quebra
    assert 'qr_code_path' in payment_info

    qr_code_path = payment_info['qr_code_path']
    os.path.isfile(f'../static/img/{qr_code_path}.png')