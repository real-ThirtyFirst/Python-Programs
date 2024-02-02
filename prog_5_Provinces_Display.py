# Problem 1
provinces = '''PROVINCE	POP_2010	AREA_SQ_KM
Metro Manila	11855975	638.55
Cebu	4167320	5342.00
Cavite	3090691	1574.17
Bulacan	2924433	2796.10
Negros Occidental	2907859	7965.21
Pangasinan	2779862	5451.01
Laguna	2669847	1917.85
Rizal	2484840	1191.94
Batangas	2377395	3119.72
Pampanga	2340355	2062.47
Iloilo	2230195	5079.17
Davao del Sur	2024206	4607.59
Quezon	1987030	9069.60
Nueva Ecija	1955373	5751.33
Camarines Sur	1822371	5497.03
Leyte	1789158	6515.05
Zamboanga del Sur	1766814	5914.16
Isabela	1489645	12414.93
Misamis Oriental	1415944	3544.32
South Cotabato	1365286	4428.81
Bukidnon	1299192	10498.59
Negros Oriental	1286666	5385.53
Tarlac	1273240	3053.60
Bohol	1255128	4820.95
Albay	1233432	2575.77
Cotabato	1226508	9008.90
Maguindanao	1216504	6146.53
Cagayan	1124773	9295.75
Palawa	994340	17030.75
Zamboanga del Norte	957997	7301.00
Davao del Norte	945764	3426.97
Lanao del Sur	933260	3872.89
Lanao del Norte	930738	4159.94
Masbate	834650	4151.78
Oriental Mindoro	785602	4238.38
Zambales	755621	3830.83
Sultan Kudarat	747087	5298.34
La Union	741906	1497.70
Sorsogon	740743	2119.01
Samar	733377	6048.03
Benguet	722620	2826.59
Capiz	719685	2594.64
Sulu	718290	1600.40
Bataan	687482	1372.98
Compostela Valley	687195	4479.77
Ilocos Sur	658587	2596.00
Agusan del Sur	656418	9989.52
Agusan del Norte	642196	3546.86
Northern Samar	589013	3692.93
Zamboanga Sibugay	584685	3607.75
Ilocos Norte	568017	3467.89
Misamis Occidental	567642	2055.22
Surigao del Sur	561219	4932.70
Antique	546031	2729.17
Camarines Norte	542915	2320.07
Aklan	535725	1821.42
Davao Oriental	517618	5679.64
Sarangani	498904	3601.25
Occidental Mindoro	452971	5865.71
Surigao del Norte	442588	1972.93
Eastern Samar	428877	4660.47
Nueva Vizcaya	421355	3975.67
Southern Leyte	399137	1798.61
Basilan	391179	1379.02
Tawi-Tawi	366550	1087.40
Davao Occidental	293780	2163.45
Romblon	283930	1533.45
Catanduanes	246300	1492.16
Abra	234733	4165.25
Marinduque	227828	952.58
Kalinga	201613	3231.25
Aurora	201233	3147.32
Ifugao	191078	2628.21
Quirino	176786	2323.47
Guimaras	162943	604.57
Biliran	161760	536.01
Mountain Province	154187	2157.38
Dinagat Islands	126803	1036.34
Apayao	112636	4413.35
Siquijor	91066	337.49
Camiguin	83807	237.95
Batanes	16604	219.01'''
provinces = provinces.replace('\t',':').split('\n')
provinces_List = [provinces[0]] + sorted(provinces[1:])
with open('Txts\provinces.txt', 'w') as file:
    for i, province in enumerate(provinces_List):
        file.write(province)
        if i < len(provinces_List) - 1:
            file.write('\n')
# Problem 2
with open('Txts\provinces.txt', 'r') as file:
    data = file.read().split('\n')

header = data[0].strip().split(':')
data_List = [dict(zip(header, _.strip().split(':'))) for _ in data[1:]]

print(f'{'PROVINCE':20}|{'POPULATION(2010)':16}|{'AREA(SQ.KM.)':12}')
print(f'{((('-'*20)+'+'+('-'*16)+'+'+('-'*12)))}')
for data in data_List:
   province = data['PROVINCE']
   population = format(int(data['POP_2010']), ',')
   area = format(float(data['AREA_SQ_KM']), ',.2f')
   print(f'{province:20}|{population:>16}|{area:>12}')
