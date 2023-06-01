"""Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que
será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y
otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al
al objetivo. Comprobar que no se puede retirar más dinero de lo que tengo ahorrado."""
print('  ** Simulador de alcancía **  ')
meta = float(input('Ingrese su moto meta de ahorro: '))
ahorr = float()
depos = float(input('Ingrese sus monto de ahorro: '))
ahorr = + depos
while ahorr < meta:
    print('Aún no sobrepasa la meta. continúe  ahorrando!!!')
    depos = float(input('Ingrese sus monto de ahorro: '))
    if  (depos < 0) >=ahorr:
        print('No puede retirar más de lo ahorrado')
    else:
        ahorr = + depos
print('Ud ha sobrepasado su meta de ahorro de $ {}!!!'.format(meta))
print('El monto total a retirar será: $ {}'.format(ahorr))