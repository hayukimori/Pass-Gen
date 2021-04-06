def gen_function():
    #gerador de senha
    from random import randint
    from random import choices
    user_choose = int(input('Qual o tamanho da senha que você deseja usar: '))
    
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890#!@$%'
    fake_passw = choices(chars,k=int(user_choose))
    passw = ''.join(fake_passw)
    print(passw)
    
    arquivo = open('Senhas.txt','w')
    arquivo.write(passw)
    arquivo.close
    pass

def gen_credits():
    #gerando os créditos
    print('Este programa foi criado e testado por KitsuneSemCalda ')
    pass