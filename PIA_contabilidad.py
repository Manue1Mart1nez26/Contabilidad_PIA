#PIA de contabilidad
#Programa para sacar el presupuesto maestro
#Equipo 3 de contabilidad

SEPARADOR = ("*" * 50) + "\n"
print("BIENVENIDO AL PRESUPUESTO MAESTRO")
print(SEPARADOR)

print("Presupuesto de Ventas")
print("Favor de ingresar los datos a calcular")
print(SEPARADOR)

print("Producto CL          Primer Semestre")
U1= int(input("Unidades a Vender: "))
P1= int(input("Precio de Venta: "))
IVD1= (U1*P1)
print("El importe de venta del primer semestre del prodcuto CL es de: ")
print(IVD1)
print(SEPARADOR)

print("Producto CL           Segundo Semestre")
U2= int(input("Unidades a Vender: "))
P2= int(input("Precio de Venta: "))
IVD2= (U2*P2)
print("El importe de venta del segundo semestre del prodcuto CL es de: ")
print(IVD2)
print(SEPARADOR)

print("El total del Producto CL del año 2016 es de: ")
Total1= (IVD1+IVD2)
print(Total1)
print(SEPARADOR)

print("Producto CE          Primer Semestre")
U3= int(input("Unidades a Vender: "))
P3= int(input("Precio de Venta: "))
IVDi1= (U3*P3)
print("El importe de venta del primer semestre del prodcuto CE es de: ")
print(IVDi1)
print(SEPARADOR)

print("Producto CE           Segundo Semestre")
U4= int(input("Unidades a Vender: "))
P4= int(input("Precio de Venta: "))
IVDi2= (U4*P4)
print("El importe de venta del segundo semestre del prodcuto CE es de: ")
print(IVDi2)
print(SEPARADOR)

print("El total del Producto CE es de: ")
Total2= (IVDi1+IVDi2)
print(Total2)
print(SEPARADOR)

print("Producto CR          Primer Semestre")
U5= int(input("Unidades a Vender: "))
P5= int(input("Precio de Venta: "))
IVZ1= (U5*P5)
print("El importe de venta del primer semestre del prodcuto CR es de: ")
print(IVZ1)
print(SEPARADOR)

print("Producto CR           Segundo Semestre")
U6= int(input("Unidades a Vender: "))
P6= int(input("Precio de Venta: "))
IVZ2= (U6*P6)
print("El importe de venta del segundo semestre del prodcuto CR es de: ")
print(IVZ2)
print(SEPARADOR)

print("El total del Producto CR es de: ")
Total3= (IVZ1+IVZ2)
print(Total3)
print(SEPARADOR)
#AQUI ME QUEDE 27 DE OCTUBRE DEL 2021 A LAS 8:40 AM##############################################################################
TotalS1= (IVD1+IVDi1+IVZ1)
TotalS2= (IVD2+IVDi2+IVZ2)
Total2016= (Total1+Total2+Total3)
print("El total de Ventas Por Semestre es de:       Primer Semestre          Segundo Semestre        Total")
print("                                                ",TotalS1,"                 ",TotalS2,"          ",Total2016)
print(SEPARADOR)

print("Determinacion del Saldo de Clientes y Flujo de Entradas")
print("Saldo de los clientes del 31 de diciembre del 2015: ")
Saldo1= int(input())
print("Saldo de Ventas 2016:")
print(Total2016)
TotalClientes2016= (Saldo1+Total2016)
print("El total del saldo de clientes del 2016 es: ")
print(TotalClientes2016)
print(SEPARADOR)
print("Entradas de Efectivo")
print("Cobranza del Año 2015: ") #Jalar el dato de la linea 84-85 de codigo
Año2015= int(input())
print("Cobranza del Año 2016: ") #Jalar datos de la linea 86-87
Año2016= int(input())
Entradas= (Año2015+Año2016)
print("El total de las entradas del 2016 es: ")
print(Entradas)
print(SEPARADOR)
Totalclientes2= (TotalClientes2016-Entradas)
print("El saldo de los clientes del 2016 es de: ")
print(Totalclientes2)
print(SEPARADOR)

print("Presupuesto de Produccion")
print("*"*10,"Producto CL de Presupuesto de Produccion Primer Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U1 linea 14
UAV= (int(input()))
print("Inventario Final") #Lo introdusco los 10,000 de teclado
INVF= (int(input()))
print("Total de unidades es de: ")
TotalU= (UAV+INVF)
print(TotalU)
print("Inventario  incial") #Inventario inicial (-) traerlo de la linea 111 podriaa ser INVF = INVI
INVI= int(input())
print("Las unidades a producir en primer semestre son: ")
UNIP= (TotalU-INVI)
print(UNIP)

print("*"*10,"Producto CL de Presupuesto de Produccion Segundo Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U2 linea 22
UAV1= (int(input()))
print("Inventario Final") #Lo introduso los 6,500 desde teclado
INVF1= (int(input()))
print("Total de unidades es de: ")
TotalU1= (UAV1+INVF1)
print(TotalU1)
print("Inventario  incial") #Inventario inicial (-) traerlo de la linea 111 podriaa ser INVF = INVI1
INVI1= int(input())
print("Las unidades a producir en segundo semestre son: ")
UNIP1= (TotalU1-INVI1)
print(UNIP1)

print("*"*10,"Producto CL de Presupuesto de Produccion Total del 2016","*"*10)
print("Unidades a Vender")
UAVT= (UAV+UAV1)
print(UAVT)
print("Inventario Final")
INVFT= (INVF1)
print(INVFT)
print("Total de unidades de prducto CL es de: ")
TotalUnidadesT= (UAVT+INVFT)
print(TotalUnidadesT)
print("Inventario Inicial") #Traer dato, INVIT = INVF osea 10,00 y al final seran 18,500 y hacer print(INVIT)
INVIT= int(input())
print("Total de unidades a Producir de Producto CL")
TotalT= (TotalUnidadesT-INVIT)
print(TotalT)
print(SEPARADOR)

print("*"*10,"Producto CE de Presupuesto de Produccion Primer Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U3 linea 35, UAVDi = U3 y hacer print(UAVDi)
UAVDi= (int(input()))
print("Inventario Final") #ingresar de teclado 8500 (redacción)
INVFDi= (int(input()))
print("Total de unidades es de: ")
TotalUDi= (UAVDi+INVFDi)
print(TotalUDi)
print("Inventario  incial") #Jalar datos que se ingresaron del teclado INVFDi, entonces INVIDi = INVFDi, print(INVIDi)
INVIDi= int(input())
print("Las unidades a producir en primer semestre son: ")
UNIPDi= (TotalUDi-INVIDi)
print(UNIPDi)

print("*"*10,"Producto CE de Presupuesto de Produccion Segundo Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U4 linea 43, UAVDi1 = U4 y hacer print(UAVDi1)
UAVDi1= (int(input()))
print("Inventario Final") #Ingresar de teclado 7500 (redacción)
INVFDi1= (int(input()))
print("Total de unidades es de: ")
TotalUDi1= (UAVDi1+INVFDi1)
print(TotalUDi1)
print("Inventario  incial") #Jalar datos que se ingresaron del teclado 8,500- el TotalUDi1 (32800)= 24,300
INVIDi1= int(input())
print("Las unidades a producir en segundo semestre son: ")
UNIPDi1= (TotalUDi1-INVIDi1)
print(UNIPDi1)
print(SEPARADOR)

print("*"*10,"Producto CE de Presupuesto de Produccion Total del 2016","*"*10)
print("Unidades a Vender")
UAVDiT= (UAVDi+UAVDi1)
print(UAVDiT)
print("Inventario Final")
INVFDiT= (INVFDi1)
print(INVFDiT)
print("Total de unidades de prducto CE es de: ")
TotalUnidadesDiT= (UAVDiT+INVFDiT)
print(TotalUnidadesDiT)
print("Inventario Inicial") #Traer dato, INVIT = INVF osea 10,00 y al final seran 18,500 y hacer print(INVIT)
INVIDiT= int(input())
print("Total de unidades a Producir de Producto CE")
TotalDiT= (TotalUnidadesDiT-INVIDiT)
print(TotalDiT)
print(SEPARADOR)

print("*"*10,"Producto CR de Presupuesto de Produccion Primer Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U5 linea 56, UAVZ = U5 y hacer print(UAVZ)
UAVZ= (int(input()))
print("Inventario Final")  #Ingresar de teclado 6000 (redacción)
INVFZ= (int(input()))
print("Total de unidades es de: ")
TotalUZ= (UAVZ+INVFZ)
print(TotalUZ)
print("Inventario  incial")  #Jalar datos que se ingresaron del teclado INVFZ, entonces INVIZ = INVFZ, print(INVIZ)
INVIZ= int(input())
print("Las unidades a producir en primer semestre son: ")
UNIPZ= (TotalUZ-INVIZ)
print(UNIPZ)

print("*"*10,"Producto CR de Presupuesto de Produccion Segundo Semestre","*"*10)
print("Unidades a vender") #Jalar datos de la linea de codigo unidades a vender U6 linea 64, UAVZ1 = U6 y hacer print(UAVZ1)
UAVZ1= (int(input()))
print("Inventario Final")#Ingresar de teclado 5,000 (redacción)
INVFZ1= (int(input()))
print("Total de unidades es de: ")
TotalUZ1= (UAVZ1+INVFZ1)
print(TotalUZ1)
print("Inventario  incial") #Jalar datos que se ingresaron del teclado 6,000 - el TotalUZ1 (13500)= 7,500
INVIZ1= int(input())
print("Las unidades a producir en segundo semestre son: ")
UNIPZ1= (TotalUZ1-INVIZ1)
print(UNIPZ1)
print(SEPARADOR)

print("*"*10,"Producto CR de Presupuesto de Produccion Total","*"*10)
print("Unidades a Vender")
UAVZT= (UAVZ+UAVZ1)
print(UAVZT)
print("Inventario Final")
INVFZT= (INVFZ1)
print(INVFZT)
print("Total de unidades de prducto CR es de: ")
TotalUnidadesZT= (UAVZT+INVFZT)
print(TotalUnidadesZT)
print("Inventario Inicial")#Traer dato, 20,500 - (6,000) = 14,500
INVIZT= int(input())
print("Total de unidades a Producir de Producto CR")
TotalZT= (TotalUnidadesZT-INVIZT)
print(TotalZT)
print(SEPARADOR)
#####IMPORTANTE TE QUEDASTE AQUI EN EL 29 DE OCTUBRE A LAS 10:11 PM SEGUNDA NOTA| mejorar las variables de entre la primera y esta nota, forma de hacerlo mas corto y agregar distintos separadores.
print("*"*10,"Presupuesto de Requerimento de Materiales","*"*10)
print("*"*10,"Producto CL","*"*10)
print("Unidades a producir: ")
UAPRM1A= int(input())
UAPRM2A= int(input())
print("Requerimentos de los Materiales A, B y C")
RMAD= float(input("Requermientos Material A: "))
RMBD= float(input("Requerimentos Material B: "))#Hacer que acepte decimales
RMCD= float(input("Requerimentos Material C: "))
RMAD2= float(input("Requermientos Material A: "))
RMBD2= float(input("Requerimentos Material B: "))#Hacer que acepte decimales
RMCD2= float(input("Requerimentos Material C: "))
Total1SDA= (UAPRM1A*RMAD)
Total2SDA= (UAPRM2A*RMAD2)
TotalASD= (Total1SDA+Total2SDA)
Total1SDB= (UAPRM1A*RMBD)
Total2SDB= (UAPRM2A*RMBD2)
TotalBSD= (Total1SDB+Total2SDB)
Total1SDC= (UAPRM1A*RMCD)
Total2SDC= (UAPRM2A*RMCD2)
TotalCSD= (Total1SDC+Total2SDC)

print("Total de Material A Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDA,"\t\t",Total2SDA,"\t\t",TotalASD)

print("Total de Material B Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDB,"\t\t",Total2SDB,"\t\t",TotalBSD)

print("Total de Material C Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDC,"\t\t",Total2SDC,"\t\t",TotalCSD)

print("*"*10,"Presupuesto de Requerimento de Materiales","*"*10)
print("*"*10,"Producto CE","*"*10)
print("Unidades a producir: ")
UAPRM1B= int(input())
UAPRM2B= int(input())
print("Requerimentos de los Materiales A, B y C")
RMAD1= float(input("Requermientos Material A: "))#Hacer que acepte decimales
RMBD1= float(input("Requerimentos Material B: "))#Hacer que acepte decimales
RMCD1= float(input("Requerimentos Material C: "))
RMAD21= float(input("Requermientos Material A: "))#Hacer que acepte decimales
RMBD21= float(input("Requerimentos Material B: "))#Hacer que acepte decimales
RMCD21= float(input("Requerimentos Material C: "))
Total1SDA1= (UAPRM1B*RMAD1)
Total2SDA1= (UAPRM2B*RMAD21)
TotalASD1= (Total1SDA1+Total2SDA1)
Total1SDB1= (UAPRM1B*RMBD1)
Total2SDB1= (UAPRM2B*RMBD21)
TotalBSD1= (Total1SDB1+Total2SDB1)
Total1SDC1= (UAPRM1B*RMCD1)
Total2SDC1= (UAPRM2B*RMCD21)
TotalCSD1= (Total1SDC1+Total2SDC1)

print("Total de Material A Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDA1,"\t\t",Total2SDA1,"\t\t",TotalASD1)

print("Total de Material B Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDB1,"\t\t",Total2SDB1,"\t\t",TotalBSD1)

print("Total de Material C Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDC1,"\t\t",Total2SDC1,"\t\t",TotalCSD1)

print("*"*10,"Presupuesto de Requerimento de Materiales","*"*10)
print("*"*10,"Producto CR","*"*10)
print("Unidades a producir: ")
UAPRM1C= int(input())
UAPRM2C= int(input())
print("Requerimentos de los Materiales A, B y C")
RMAZ= float(input("Requermientos Material A: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
RMBZ= float(input("Requerimentos Material B: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
RMCZ= float(input("Requerimentos Material C: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
RMAZ2= float(input("Requermientos Material A: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
RMBZ2= float(input("Requerimentos Material B: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
RMCZ2= float(input("Requerimentos Material C: "))#Hacer que acepte decimales|en la redacción no lleva decimales pero tambien
Total1SDA2= (UAPRM1C*RMAZ)
Total2SDA2= (UAPRM2C*RMAZ2)
TotalASD2= (Total1SDA2+Total2SDA2)
Total1SDB2= (UAPRM1C*RMBZ)
Total2SDB2= (UAPRM2C*RMBZ2)
TotalBSD2= (Total1SDB2+Total2SDB2)
Total1SDC2= (UAPRM1C*RMCZ)
Total2SDC2= (UAPRM2C*RMCZ2)
TotalCSD2= (Total1SDC2+Total2SDC2)

print("Total de Material A Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDA2,"\t\t",Total2SDA2,"\t\t",TotalASD2)

print("Total de Material B Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDB2,"\t\t",Total2SDB2,"\t\t",TotalBSD2)

print("Total de Material C Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total1SDC2,"\t\t",Total2SDC2,"\t\t",TotalCSD2)

Total_requerimientos1SA = (Total1SDA+Total1SDA1+Total1SDA2)
Total_requerimientos2SA = (Total2SDA+Total2SDA1+Total2SDA2)
Total_requerimientosTotal2016A = (TotalASD+TotalASD1+TotalASD2)

Total_requerimientos1SB = (Total1SDB+Total1SDB1+Total1SDB2)
Total_requerimientos2SB = (Total2SDB+Total2SDB1+Total2SDB2)
Total_requerimientosTotal2016B = (TotalBSD+TotalBSD1+TotalBSD2)

Total_requerimientos1SC = (Total1SDC+Total1SDC1+Total1SDC2)
Total_requerimientos2SC = (Total2SDC+Total2SDC1+Total2SDC2)
Total_requerimientosTotal2016C = (TotalCSD+TotalCSD1+TotalCSD2)
print(SEPARADOR)
print("*"*5,"Total de Requerimientos","*"*5)
print("Total de Material A Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total_requerimientos1SA,"\t\t",Total_requerimientos2SA,"\t\t",Total_requerimientosTotal2016A)
print(SEPARADOR)
print("Total de Material B Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total_requerimientos1SB,"\t\t",Total_requerimientos2SB,"\t\t",Total_requerimientosTotal2016B)
print(SEPARADOR)
print("Total de Material C Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",Total_requerimientos1SC,"\t\t",Total_requerimientos2SC,"\t\t",Total_requerimientosTotal2016C)
print(SEPARADOR)
print(SEPARADOR)
#####TE QUEDASTE AQUI EL 30 OCTUBRE 8:30 PM corregir las variables anteriores
print("*"*10,"Presupuesto de Compra de Materiales","*"*10)
print("*"*10,"Material A Primer Semestre","*"*10)
print("Requerimento de materiales: ")
RDMA1= Total_requerimientos1SA
print(RDMA1)
print("Inventario final: ")
IFM1= int(input())
TotalM1= (RDMA1+IFM1)
print("Rl total de materiales es: ", TotalM1)
print("Inventario incial: ")
II1= IFM1
print(II1)
TotalM1A= (TotalM1-II1)
print("El material a comprar es de: ", TotalM1A)
print("Cual va a ser el precio de compra?: ")
PC= int(input())
TotalMatA= (TotalM1A*PC)
print("El total de Material A en $ es de: ")
print(TotalMatA)

print("*"*10,"Material A Segundo Semestre","*"*10)
print("Requerimento de materiales: ")
RDMA2= Total_requerimientos2SA
print(RDMA2)
print("Inventario final: ")
IFM2= int(input())
TotalM2= (RDMA2+IFM2)
print("Rl total de materiales es: ", TotalM2)
print("Inventario incial: ")
II2= IFM1
print(II2)
TotalM2A= (TotalM2-II2)
print("El material a comprar es de: ", TotalM2A)
print("Cual va a ser el precio de compra?: ")
PC2= int(input())
TotalMatA2= (TotalM2A*PC2)
print("El total de Material A en $ es de: ")
print(TotalMatA2)
print(SEPARADOR)

print("El total de Material A")
print("Total en Requerimento de Materiales es de: ")
print(RDMA1+RDMA2)
print("El inventario final de Material A fue: ")
print(IFM2)
print("El total de Materiales fue: ")
print(TotalM1+TotalM2)
print("El inventario incial fue de: ")
print(II2)
print("El total de material a comprar es de: ")
print(TotalM1A+TotalM2A)
print("El total de material A en $ fue de: ")
print(TotalMatA+TotalMatA2)
print(SEPARADOR)

print("*"*10,"Material B Primer Semestre","*"*10)
print("Requerimento de materiales: ")
RDMB= Total_requerimientos1SB
print(RDMB)
print("Inventario final: ")
IFB= int(input())
TotalMB= (RDMB+IFB)
print("Rl total de materiales es: ", TotalMB)
print("Inventario incial: ")
II1B= IFB
print(II1B)
TotalM1B= (TotalMB-II1B)
print("El material a comprar es de: ", TotalM1B)
print("Cual va a ser el precio de compra?: ")
PCB= int(input())
TotalMatB= (TotalM1B*PCB)
print("El total de Material B en $ es de: ")
print(TotalMatB)

print("*"*10,"Material B Segundo Semestre","*"*10)
print("Requerimento de materiales: ")
RDMB2= Total_requerimientos2SB
print(RDMB2)
print("Inventario final: ")
IFB2= int(input())
TotalM2B= (RDMB2+IFB2)
print("Rl total de materiales es: ", TotalM2B)
print("Inventario incial: ")
II2B= IFB
print(II2B)
TotalM2B= (TotalM2B-II2B)
print("El material a comprar es de: ", TotalM2B)
print("Cual va a ser el precio de compra?: ")
PC2B= int(input())
TotalMatB2= (TotalM2B*PC2B)
print("El total de Material B en $ es de: ")
print(TotalMatB2)
print(SEPARADOR)

print("El total de Material B")
print("Total en Requerimento de Materiales es de: ")
print(RDMB+RDMB2)
print("El inventario final de Material B fue: ")
print(IFB2)
print("El total de Materiales fue: ")
print(TotalMB+TotalM2B)
print("El inventario incial fue de: ")
print(II2B)
print("El total de material a comprar es de: ")
print(TotalM2B+TotalM1B)
print("El total de material B en $ fue de: ")
print(TotalMatB+TotalMatB2)
print(SEPARADOR)

print("*"*10,"Material C Primer Semestre","*"*10)
print("Requerimento de materiales: ")
RDMC= Total_requerimientos1SC
print(RDMC)
print("Inventario final: ")
IFC= int(input())
TotalMC= (RDMC+IFC)
print("Rl total de materiales es: ", TotalMC)
print("Inventario incial: ")
IIC= IFC
print(IIC)
TotalMC= (TotalMC-IIC)
print("El material a comprar es de: ", TotalMC)
print("Cual va a ser el precio de compra?: ")
PCC= int(input())
TotalMatC= (TotalMC*PCC)
print("El total de Material C en $ es de: ")
print(TotalMatC)

print("*"*10,"Material C Segundo Semestre","*"*10)
print("Requerimento de materiales: ")
RDMC2= Total_requerimientos2SC
print(RDMC2)
print("Inventario final: ")
IFC2= int(input())
TotalMC2= (RDMC2+IFC2)
print("Rl total de materiales es: ", TotalMC2)
print("Inventario incial: ")
IIC2= IFC
print(IIC2)
TotalM2C= (TotalMC2-IIC2)
print("El material a comprar es de: ", TotalM2C)
print("Cual va a ser el precio de compra?: ")
PC2C= int(input())
TotalMatC2= (TotalM2C*PC2C)
print("El total de Material C en $ es de: ")
print(TotalMatC2)
print(SEPARADOR)

print("El total de Material C")
print("Total en Requerimento de Materiales es de: ")
print(RDMC+RDMC2)
print("El inventario final de Material C fue: ")
print(IFC2)
print("El total de Materiales fue: ")
print(TotalMC+TotalM2C)
print("El inventario incial fue de: ")
print(IIC2)
print("El total de material a comprar es de: ")
print(TotalMC+TotalM2C)
print("El total de material C en $ fue de: ")
print(TotalMatC+TotalMatC2)
print(SEPARADOR)

print("*"*10,"COMPRAS TOTALES","*"*10)
CPT1S = (TotalMatA+TotalMatB+TotalMatC)
CPT2S = (TotalMatA2+TotalMatB2+TotalMatC2)
CPTotal2016 = (CPT1S+CPT2S)
print("Total de Material C Requerido:      1er Semestre     2do Semestre     Total")
print("\t\t\t\t\t",CPT1S,"\t\t",CPT2S,"\t\t",CPTotal2016)
print(SEPARADOR)
print(SEPARADOR)
#####TE QUEDASTE AQUI A LAS 11:10 PM AQUI TE QUEDASTE TE QUEDASTE AQUI A LAS 11:50 PM en el presupuesto 6
print("Determinacion del saldo de Proveedores y Flujos de Salida") #PRESUPUESTO 6
print("Saldo de proveedores 31-dic-2015: ")
Saldo_2015= int(input())
print("Compras 2016: ")
print(CPTotal2016)
TotalClientes= (Saldo_2015 + CPTotal2016)
print("El total de Proveedores 2016 es de $: ")
print(TotalClientes)
print(SEPARADOR)
print("Salidas de Efectivo")
print("Por Proveedores del 2015:: ")
Año_2015= Saldo_2015
print(Año2015)
print("Por proveedores del 2016: ")
Año_2016= (CPTotal2016*0.50)
print(Año_2016)
Entradas= (Año_2015+Año_2016)
print("Total de salidas 2016: ")
print(Entradas)
print(SEPARADOR)
Total_Clientes2= (TotalClientes-Entradas)
print("El saldo de los clientes es de: ")
print(Total_Clientes2)
print(SEPARADOR)

print("*"*10,"Presupuesto de Mano de Obra Directa","*"*10) #Te quedaste aqui el 31 de octubre a las 10:07 pm

print("*"*10,"PRODUCTO CL       1er. Semestre","*"*10)
print("Unidades a producir: ")
UAPCL1= UNIP
print(UAPCL1)
print("Horas requeridas por unidad: ")
HRPUCL1= int(input())
TDHRCL1= (UAPCL1 * HRPUCL1)
print("Total de horas requeridas: ",TDHRCL1)
print("Cuota por hora: ")
CPHCL1= int(input())
IDMODCL1= TDHRCL1 * CPHCL1
print("El importe de M.O.D es: ", IDMODCL1)

print("*"*10,"PRODUCTO CL       2do. Semestre","*"*10)
print("Unidades a producir: ")
UAPCL2= UNIP1
print(UAPCL2)
print("Horas requeridas por unidad: ")
HRPUCL2= int(input())
TDHRCL2= (UAPCL2 * HRPUCL2)
print("Total de horas requeridas: ",TDHRCL2)
print("Cuota por hora: ")
CPHCL2= int(input())
IDMODCL2= TDHRCL2 * CPHCL2
print("El importe de M.O.D es: ", IDMODCL2)

TUAPCL2016= (UAPCL1 + UAPCL2)
print("El total de unidades a producir es de: ", TUAPCL2016)
THRPUCL2016= (HRPUCL1)
print("El total de horas requeridas por unidad es de: ", THRPUCL2016)
TTDHRCL2016= (TUAPCL2016 * THRPUCL2016)
print("El total de horas requeridas es de: ", TTDHRCL2016)
TIDMODCL2016= (IDMODCL1 + IDMODCL2)
print("El total del importe de M.O.D es de: ", TIDMODCL2016)



print("*"*10,"PRODUCTO CE       1er. Semestre","*"*10)
print("Unidades a producir: ")
UAPCE1= UNIPDi
print(UAPCE1)
print("Horas requeridas por unidad: ")
HRPUCE1= int(input())
TDHRCE1= (UAPCE1 * HRPUCE1)
print("Total de horas requeridas: ",TDHRCE1)
print("Cuota por hora: ")
CPHCE1= CPHCL1
print(CPHCE1)
IDMODCE1= TDHRCE1 * CPHCE1
print("El importe de M.O.D es: ", IDMODCE1)

print("*"*10,"PRODUCTO CE       2do. Semestre","*"*10)
print("Unidades a producir: ")
UAPCE2= UNIPDi1
print(UAPCE2)
print("Horas requeridas por unidad: ")
HRPUCE2= int(input())
TDHRCE2= (UAPCE2 * HRPUCE2)
print("Total de horas requeridas: ",TDHRCE2)
print("Cuota por hora: ")
CPHCE2= CPHCL2
print(CPHCE2)
IDMODCE2= TDHRCE2 * CPHCE2
print("El importe de M.O.D es: ", IDMODCE2)

TUAPCE2016= (UAPCE1 + UAPCE2)
print("El total de unidades a producir es de: ", TUAPCE2016)
THRPUCE2016= (HRPUCE1)
print("El total de horas requeridas por unidad es de: ", THRPUCE2016)
TTDHRCE2016= (TUAPCE2016 * THRPUCE2016)
print("El total de horas requeridas es de: ", TTDHRCE2016)
TIDMODCE2016= (IDMODCE1 + IDMODCE2)
print("El total del importe de M.O.D es de: ", TIDMODCE2016)



print("*"*10,"PRODUCTO CR       1er. Semestre","*"*10)
print("Unidades a producir: ")
UAPCR1= UNIPZ
print(UAPCR1)
print("Horas requeridas por unidad: ")
HRPUCR1= float(input())
TDHRCR1= (UAPCR1 * HRPUCR1)
print("Total de horas requeridas: ",TDHRCR1)
print("Cuota por hora: ")
CPHCR1= CPHCE1
print(CPHCR1)
IDMODCR1= TDHRCR1 * CPHCR1
print("El importe de M.O.D es: ", IDMODCR1)

print("*"*10,"PRODUCTO CR       2do. Semestre","*"*10)
print("Unidades a producir: ")
UAPCR2= UNIPZ1
print(UAPCR2)
print("Horas requeridas por unidad: ")
HRPUCR2= float(input())
TDHRCR2= (UAPCR2 * HRPUCR2)
print("Total de horas requeridas: ",TDHRCR2)
print("Cuota por hora: ")
CPHCR2= CPHCE2
print(CPHCR2)
IDMODCR2= TDHRCR2 * CPHCR2
print("El importe de M.O.D es: ", IDMODCR2)

TUAPCR2016= (UAPCR1 + UAPCR2)
print("El total de unidades a producir es de: ", TUAPCR2016)
THRPUCR2016= (HRPUCR1)
print("El total de horas requeridas por unidad es de: ", THRPUCR2016)
TTDHRCR2016= (TUAPCR2016 * THRPUCR2016)
print("El total de horas requeridas es de: ", TTDHRCR2016)
TIDMODCR2016= (IDMODCR1 + IDMODCR2)
print("El total del importe de M.O.D es de: ", TIDMODCR2016)



TDHRPS1= (TDHRCL1 + TDHRCE1 + TDHRCR1)
print("El total de horas requeridas por el primer semestre es de: ", TDHRPS1)
TDHRPS2= (TDHRCL2 + TDHRCE2 + TDHRCR2)
print("El total de horas requeridas por el segundo semestre es de: ", TDHRPS2)
TTDHRPS= (TTDHRCL2016 + TTDHRCE2016 + TTDHRCR2016)
print("El total de horas requeridas por semestre en 2016 es de: ", TTDHRPS)

TDMODPS1= (IDMODCL1 + IDMODCE1 + IDMODCR1)
print("El total de M.O.D por el primer semestre es de: ", TDMODPS1)
TDMODPS2= (IDMODCL2 + IDMODCE2 + IDMODCR2)
print("El total de M.O.D por el segundo semestre es de: ", TDMODPS2)
TTDMODPS= (TIDMODCL2016 + TIDMODCE2016 + TIDMODCR2016)
print("El total de M.O.D por semestre es de: ",TTDMODPS)
print(SEPARADOR)
#############AQUI TERMINA EL PRESPUESTO 7 AQUI TERMINA EL PRSUPUESTO 7 AQUI TERMINA EL PRESUPUESTO 7
############TE QUEDASTE EN EL PRESUPUESTO 8 TE QUEDEASTE EN EL PRESUPUESTO DE GASTOS INDIRECTOS DE FABRICACIÓN LNIEA 691 SOLO FALTASN 550 APROX LINEAS DE CODIGO
print("*"*10,"Presupuesto de Gastos Indirectos de Fabricacion","*"*10)
print("*"*10,"1er. Semestre","*"*10)
print("Depreciacion: ")
DEP1= int(input())
print("Seguros: ")
SEG1= int(input())
print("Mantenimiento: ")
MANT1= int(input())
print("Energeticos: ")
ENERG1= int(input())
print("Varios: ")
VAR1= int(input())
TGIFPS1= (DEP1 + SEG1 + MANT1 + ENERG1 + VAR1)
print("El total de G.I.F por el primer semestre es de: ", TGIFPS1)

print("*"*10,"2do. Semestre","*"*10)
print("Depreciacion: ")
DEP2= int(input())
print("Seguros: ")
SEG2= int(input())
print("Mantenimiento: ")
MANT2= int(input())
print("Energeticos: ")
ENERG2= int(input())
print("Varios: ")
VAR2= int(input())
TGIFPS2= (DEP2 + SEG2 + MANT2 + ENERG2 + VAR2)
print("El total de G.I.F por el segundo semestre es de: ", TGIFPS2)

print("*"*10)
TD2016= (DEP1 + DEP2)
print("El total de depreciacion en 2016 es de: ", TD2016)
TS2016= (SEG1 + SEG2)
print("El total de seguros en 2016 es de: ", TS2016)
TMANT2016= (MANT1 + MANT2)
print("El total de mantenimiento en 2016 es de: ", TMANT2016)
TENERG2016= (ENERG1 + ENERG2)
print("El total de energeticos en 2016 es de: ", TENERG2016)
TVAR2016= (VAR1 + VAR2)
print("El total de varios en 2016 es de: ",TVAR2016)
TTGIFPS= (TD2016 + TS2016 + TMANT2016 + TENERG2016 + TVAR2016)
print("El total G.I.F por semestre es de: ", TTGIFPS)


print("*"*10,"Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricacion","*"*10)
print("Total de G.I.F: ", TTGIFPS)
THMODA= (TTDHRPS)
print("El total de horas M.O.D anual es de: ", THMODA)
TTGIFPS= (TTGIFPS / TTDHRPS)
print("El costo por hora de G.I.F es de: ", TTGIFPS)

print(SEPARADOR)

print("*"*5,"Presupuesto de Gastos de Operación","*"*5) #Presupuesto 9
print("*"*10," Primer Semestre","*"*10)

print("Depreciacion : ")
DEPR1 = int(input())

print("Sueldos y salarios: ")
SUELYSAL1 = int(input())

print("Comisiones: ")
COMIS1 = (TotalS1*0.01)
print(COMIS1)

print("Varios: ")
VARI1 = int(input())

print("Intereses por prestamo: ")
INPRES1 = int(input())

print("** Total de Gastos de Operación **")
print(DEPR1 + SUELYSAL1 + COMIS1 + VARI1 + INPRES1)

#Segundo semestre

print("*"*5,"Presupuesto de Gastos de Operación","*"*5)
print("*"*10," Segundo Semestre","*"*10)

print("Depreciacion : ")
DEPR2 = int(input())

print("Sueldos y salarios: ")
SUELYSAL2 = int(input())


print("Comisiones: ")
COMIS2 = (TotalS2*0.01)
print(COMIS2)

print("Varios: ")
VARI2 = int(input())

print("Intereses por prestamo: ")
INPRES2 = int(input())

print("** Total de Gastos de Operación **")
print(DEPR2 + SUELYSAL2 + COMIS2 + VARI2 + INPRES2)



#parte 3
print("*"*5,"TOTAL 2016: ","*"*5)

print("Total Depreciacion")
print(DEPR1 + DEPR2)

print("Sueldos y Salarios")
print(SUELYSAL1 + SUELYSAL2)

print("Comisiones")
print(COMIS1 + COMIS2)

print("Varios")
print(VARI1 + VARI2)

print("Intereses por Préstamo")
print(INPRES1 + INPRES2)

print("Total de Gastos de Operación: ")
TotalGOP = (DEPR1+ SUELYSAL1 +COMIS1+ VARI1 + INPRES1 + DEPR2 +SUELYSAL2 +COMIS2 + VARI2 + INPRES2 )
print(TotalGOP)

print("*"*10,"Determinacion del Costo Unitario de Productos Terminados","*"*10) #JALAR DATOS DE LOS PRESUPUESTOS ANTERIORES
##*******PRODUCTI Cl********
print("*"*10,"PRODUCTO CL","*"*10)
print("")
print("*"*10,"Material A","*"*10)
print("Costo")
CMA1= PC2
print(CMA1)
print("Cantidad")
CAMA1= RMAD #TE QUEDASTE AQUI HOY 1 DE NOVIEMBRE ESTAS JALANDO DATOS EN EL EXCEL AHORA SEGUIRA EL MATERIAL B DE CL
print(CAMA1)
CUI1=CMA1*CAMA1 
print("El Costo Unitario es: ",CUI1)
print("")
print("*"*10,"Material B","*"*10)
print("Costo")
CMA2= PC2B
print("Cantidad")
CAMA2= RMBD
print(CAMA2)
CUI2=CMA2*CAMA2 
print("El Costo Unitario es: ",CUI2)
print("")
print("*"*10,"Material C","*"*10)
print("Costo")
CMA3= PC2C
print(CMA3)
print("Cantidad")
CAMA3= RMCD
print(CAMA3)
CUI3=CMA3*CAMA3 
print("El Costo Unitario es: ",CUI3)
print("")
print("*"*10,"Mano de Obra","*"*10)
print("Costo")
CMA4= CPHCL2
print(CMA4)
print("Cantidad")
CAMA4= HRPUCL2
print(CAMA4)
CUI4=CMA4*CAMA4 
print("El Costo Unitario es: ",CUI4)
print("")
print("*"*10,"Gastos Indirectos de Fabricacion","*"*10)
print("Costo")
CMA5= TTGIFPS 
print(CMA5)
print("Cantidad")
CAMA5= CAMA4
print(CAMA5)
CUI5=CMA5*CAMA5 
print("El Costo Unitario es: ",CUI5)
print("")
print("*"*10,"Costo Unitario","*"*10)
print("$",CUI1+CUI2+CUI3+CUI4+CUI5)
print("")
##*******PRODUCTI CE********
print("*"*10,"PRODUCTO CE","*"*10)
print("*"*10,"Material A","*"*10)
print("Costo")
CMA6= PC2
print(CMA6)
print("Cantidad")
CAMA6= RMAD21
print(CAMA6)
CUI6=CMA6*CAMA6 
print("El Costo Unitario es: ",CUI6)
print("")
print("*"*10,"Material B","*"*10)
print("Costo")
CMA7= CMA2
print(CMA7)
print("Cantidad")
CAMA7= RMBD21
print(CAMA7)
CUI7=CMA7*CAMA7 
print("El Costo Unitario es: ",CUI7)
print("")
print("*"*10,"Material C","*"*10)
print("Costo")
CMA8= CMA3
print(CMA8)
print("Cantidad")
CAMA8= RMCD21
print(CAMA8)
CUI8=CMA8*CAMA8 
print("El Costo Unitario es: ",CUI8)
print("")
print("*"*10,"Mano de Obra","*"*10)
print("Costo")
CMA9= CMA4
print(CMA9)
print("Cantidad")
CAMA9= HRPUCE2
CUI9=CMA9*CAMA9 
print("El Costo Unitario es: ",CUI9)
print("")
print("*"*10,"Gastos Indirectos de Fabricacion","*"*10)
print("Costo")
CMA10= CMA5
print(CMA10)
print("Cantidad")
CAMA10= CAMA9
print(CAMA10)
CUI10=CMA10*CAMA10 
print("El Costo Unitario es: ",CUI10)
print("")
print("*"*10,"Costo Unitario","*"*10)
print("$",CUI6+CUI7+CUI8+CUI9+CUI10)
print("")
##*******PRODUCTI CR********
print("*"*10,"PRODUCTO CR","*"*10)
print("*"*10,"Material A","*"*10)
print("Costo")
CMA11= CMA6
print(CMA11)
print("Cantidad")
CAMA11= RMAZ2
print(CAMA11)
CUI11=CMA11*CAMA11 
print("El Costo Unitario es: ",CUI11)
print("")
print("*"*10,"Material B","*"*10)
print("Costo")
CMA12= CMA7
print(CMA12)
print("Cantidad")
CAMA12= RMBZ2
print(CAMA12)
CUI12=CMA12*CAMA12 
print("El Costo Unitario es: ",CUI12)
print("")
print("*"*10,"Material C","*"*10)
print("Costo")
CMA13= CMA8
print(CMA13)
print("Cantidad")
CAMA13= RMCZ2
print(CAMA13)
CUI13=CMA13*CAMA13 
print("El Costo Unitario es: ",CUI13)
print("")
print("*"*10,"Mano de Obra","*"*10)
print("Costo")
CMA14= float(input())
print("Cantidad")
CAMA14= float(input())
CUI14=CMA14*CAMA14 
print("El Costo Unitario es: ",CUI14)
print("")
print("*"*10,"Gastos Indirectos de Fabricacion","*"*10)
print("Costo")
CMA15= CMA10
print(CMA15)
print("Cantidad")
CAMA15= HRPUCR2
print(CAMA15)
CUI15=CMA15*CAMA15 
print("El Costo Unitario es: ",CUI15)
print("")
print("*"*10,"Costo Unitario","*"*10)
print("$",CUI11+CUI12+CUI13+CUI14+CUI15)

print(SEPARADOR)

print("*"*10,"Valuación de Inventarios Finales","*"*10) #Presupuesto 11

print("*"*10,"Inventario Final de Materiales","*"*10)
print("*"*10,"Material A","*"*10)
print("Unidades: ")
UDSA1= int(input())
print("Costo Unitario: ")
CUA1= float(input())
CTA1= (UDSA1 * CUA1)
print("El costo total es de: ", CTA1)

print("*"*10,"Material B","*"*10)
print("Unidades: ")
UDSB1= int(input())
print("Costo Unitario: ")
CUB1= float(input())
CTB1= (UDSB1 * CUB1)
print("El costo total es de: ", CTB1)

print("*"*10,"Material C","*"*10)
print("Unidades: ")
UDSC1= int(input())
print("Costo Unitario: ")
CUC1= float(input())
CTC1= (UDSC1 * CUC1)
print("El costo total es de: ", CTC1)

TIFDM= (CTA1 + CTB1 + CTC1)
print("El inventario final de materiales es de: ", TIFDM)

print(SEPARADOR)

print("*"*10,"Inventario Final de Producto Terminado","*"*10)
print("Producto CL")
print("Unidades: ")
UDSA2= int(input())
print("Costo Unitario: ")
CUA2= (CUI1+CUI2+CUI3+CUI4+CUI5)
print(CUA2)
CTA2= (UDSA2 * CUA2)
print("El costo total es de: ", CTA2)

print("Producto CE")
print("Unidades: ")
UDSB2= int(input())
print("Costo Unitario: ")
CUB2= (CUI6+CUI7+CUI8+CUI9+CUI10)
print(CUB2)
CTB2= (UDSB2 * CUB2)
print("El costo total es de: ", CTB2)

print("Producto CR")
print("Unidades: ")
UDSC2= int(input())
print("Costo Unitario: ")
CUC2= (CUI11+CUI12+CUI13+CUI14+CUI15)
print(CUC2)
CTC2= (UDSC2 * CUC2)
print("El costo total es de: ", CTC2)

TIFDM2= (CTA2 + CTB2 + CTC2)
print("El inventario final de producto terminado es de: ", TIFDM2)
print(SEPARADOR)
print(" PRESUPUESTO FINANCIERO ") #PRESUPUESTO FINANCIERO LINEA DE CODIGO 984 DE 1200(APROX)
print(SEPARADOR)
print("*"*10,"Estado de Costo de Producción y Ventas","*"*10)
print('Saldo Inicial de Materiales: ')
SIM= int(input())
print('Compras de Materiales: ')
CM= CPTotal2016
print(CM)
MD= CM+SIM
print('Material Disponible: ')
print(MD)
print('Inventario Final de Materiales: ')
IFM= TIFDM
print(IFM)
MU= MD-IFM
print('Materiales Utilizados: ')
print(MU)
print('Mano de Obra Directa: ')
MOD= TTDMODPS
print(MOD)
print('Gastos de Fabricación Indirectos: ')
GFI= TTGIFPS
print(GFI)
print('Costo de Producción: ')
CP= MU+MOD+GFI
print(CP)
print('Inventario Inicial de Productos Terminados: ')
IIPT= int(input())
print('Total de Producción Disponible: ')
TPD= CP+IIPT
print(TPD)
print('Inventario Final de Productos Terminados: ')
IFPT= TIFDM2
print(IFPT)
print('Costo de Ventas: ')
CV= TPD-IFPT
print(CV)
print(SEPARADOR)

print("*"*15, "Estado de Resultados", "*"*15)

print("Cuanto es de Ventas" )
VER1= Total2016
print(VER1)
print("Cuanto fue de Costo de Ventas")
CDV1= CV
print(CDV1)
UtilidadBruta= (VER1-CDV1)
print("El total de la utilidad Bruta es de: ", )
print (UtilidadBruta)
print ("Cuanto fue de lso Gastos de Operacion: ")
GastosO= TotalGOP
print(GastosO)
print ("El total de la Utilidad de la operacion fue: ")
UtilidadO= (UtilidadBruta-GastosO)
print (UtilidadO)
print ("Cuanto fue de ISR: ?")
ISR1= (UtilidadO*0.35)
print(ISR1)
print ("Cuanto fue PTU: ?")
PTU1= (UtilidadO*0.10)
print(PTU1)
print ("El total de la Utilidad Neta fue: ")
UtilidadN= (UtilidadO-ISR1-PTU1)
print (UtilidadN)

print(SEPARADOR)

print("*"*10,"Estado de Flujo de Efectivo","*"*10)
print('Saldo Inicial de Efectivo: ')
SIE= int(input())
print('Entradas: ')
print('Cobranza 2015: ')
Cob1= Año2015
print(Cob1)
print('Cobranza 2016: ')
Cob2= Año2016
print(Cob2)
print('Total de Entrasas: ')
TE= Cob1+Cob2
print(TE)
print('Efectivo Disponible: ')
ED= (TE+SIE)
print(ED)
print('Salidas: ')
print(' Proveedores 2016: ')
Prov1= Año_2016
print(Prov1)
print(' Proveedores 2015: ')
Prov2= Año_2015
print(Prov2)
print('Pago de Mano de Obra Directa: ')
PMOD= TTDMODPS
print(PMOD)
print('Pago de Gastos Indirectos de Fabricación: ')
PGIF= (TTGIFPS-TD2016)
print(PGIF)
print('Pago de Gastos de Operación: ')
PGO= (TotalGOP-(DEPR1 + DEPR2))
print(PGO)
print('Compra de Activo Dijo(Maquinaria): ')
CAD= int(input())
print('Pago ISR 2015: ')
ISR1= int(input())
print('Pago ISR 2016: ')
ISR2= int(input())
print('Total de Salidas: ')
TS= (Prov1+Prov2+PMOD+PGIF+PGO+CAD+ISR1+ISR2)
print(TS)
print('Flujo de Efectivo Actual $: ')
FEA= (ED-TS)
print(FEA)
print(SEPARADOR)

print("*"*10,"Maquilados Mexicanos, S.A. de C.V.","*"*10)
print("*"*10,"Balance General","*"*10)
print("*"*10,"Presupuesto al 31 de Diciembre del 2016","*"*10)
print("ACTIVO")
print("**Circulante**")
print("-Efectivo")
EFEC= FEA
print(EFEC)
print("-Clientes")
CLI=Totalclientes2
print(CLI)
print("-Deudores Diversos")
DD=int(input())
print("-Funcionarios y Empleados")
FE=int(input())
print("-Inventario de Materiales")
IDM= TIFDM
print(IDM)
print("-Inventario de Producto Terminado")
IPT=TIFDM2
print(IPT)
Total1=EFEC+CLI+DD+FE+IDM+IPT
print("-Total de activos circulantes: $",Total1)
print("")
print("**No Circulante**")
print("-Terreno")
TR=int(input())
print("-Planta y equipo")
PYE=int(input())
print("-Depreciación Acumulada")
DA=int(input())
Total2=TR+PYE-DA
print("Total Activos No Circulante: $",Total2)
print("")
print("Activo Total: ",Total1+Total2)
print("")
print("PASIVO")
print("**Corto Plazo**")
print("Proveedores")
PROVE=Total_Clientes2
print(PROVE)
print("Documentos por Pagar")
DPP=int(input())
print("ISR por Pagar")
ISR=ISR1
print(ISR)
print("PTU por pagar")
PTU=PTU1
print(PTU)
Total3=PROVE+DPP+ISR+PTU
print("Total de Pasivo a Corto Plazo: $",Total3)
print("")
print("**Largo Plazo**")
print("Obligaciones por Pagar:")
PB=int(input())
print("Total de Pasivo a Largo Plazo: $",PB)
PTT=Total3+PB
print("Pasivo Total: ",PTT)
print("")
print("**Capital Contable**")
print("Capital Aportado")
CAP=int(input())
print("Capital Ganado")
CAG=int(input())
print("Utilidad del Ejercicio")
UDE=UtilidadN
print(UDE)
TCCC=CAP+CAG+UDE
print("Total de Capital Contable: $",TCCC)
print("*"*20)
print("****SUMA DE PASIVO Y CAPITAl****")
print("$",TCCC+PTT)