def gen_function():
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