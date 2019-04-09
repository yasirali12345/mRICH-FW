#!/usr/bin/env python
'''
OVERVIEW:
Test script for sending UDP commands.
 
AUTHORS:
Bronson Edralin <bedralin@hawaii.edu> & Isar Mostafanezhad
University of Hawaii at Manoa
Instrumentation Development Lab (IDLab), WAT214
DESCRIPTION:
chmod +x tst_sendUDP.py
./tst_sendUDP.py
9/18/2015, IM: Separated each ASIC config sequence and added wait states.
9/21/2015, IM: Updated config values to the latest
'''




import sys
import os
SCRIPTPATH = os.path.dirname(__file__)
sys.path.append( SCRIPTPATH+'/lib/' )
import linkEth
import time

usageMSG="Usage: setMBTXConfig <interface> \n This command will set the config parameters of all the ASICs on the MB";
if len(sys.argv)!=2:
	print usageMSG
	exit(-1)



# Ethernet Configuration
addr_fpga = '192.168.20.5'
addr_pc = '192.168.20.1'
port_pc = '28672'
port_fpga = '24576'
interface = sys.argv[1]

# Make UDP class for receiving/sending UDP Packets
ctrl = linkEth.UDP(addr_fpga, port_fpga, addr_pc, port_pc, interface)

ctrl.open()
syncwd="000000010253594e4300000000"


cmd_pre="01234567AE000100AF000000AE000100AF008000AE000100AE008000AE000100"+\
"AE000100AF00FFFFAE000100AE000100AF008000AE000100AF050080AE000100"+"AF060140AE000100";

cmd_a0="B00005AA"+"AE000010"+"B00205AA"+"AE000010"+"B00405AA"+"AE000010"+\
"B00605AA"+"AE000010"+"B00805AA"+"AE000010"+"B00A05AA"+"AE000010"+"B00C05AA"+"AE000010"+\
"B00E05AA"+"AE000010"+"B01005AA"+"AE000010"+"B01205AA"+"AE000010"+"B01405AA"+"AE000010"+\
"B01605AA"+"AE000010"+"B01805AA"+"AE000010"+"B01A05AA"+"AE000010"+"B01C05AA"+"AE000010"+\
"B01E05AA"+"AE000010"+"B00103D9"+"AE000010"+"B00303D9"+"AE000010"+"B00503D9"+"AE000010"+\
"B00703D9"+"AE000010"+"B00903D9"+"AE000010"+"B00B03D9"+"AE000010"+"B00D03D9"+"AE000010"+\
"B00F03D9"+"AE000010"+"B01103D9"+"AE000010"+"B01303D9"+"AE000010"+"B01503D9"+"AE000010"+\
"B01703D9"+"AE000010"+"B01903D9"+"AE000010"+"B01B03D9"+"AE000010"+"B01D03D9"+"AE000010"+\
"B01F03D9"+"AE000010"+"B0300514"+"AE000010"+"B0310000"+"AE000010"+"B0320A5A"+"AE000010"+\
"B033044C"+"AE000010"+"B03405DC"+"AE000010"+"B0350426"+"AE000010"+"B03604B9"+"AE000010"+\
"B0370000"+"AE000010"+"B0380480"+"AE000010"+"B0390000"+"AE000010"+"B03A08BB"+"AE000010"+\
"B03B0000"+"AE000010"+"B03D046A"+"AE000010"+"B03E044C"+"AE000010"+"B03F044C"+"AE000010"+\
"B040008F"+"AE000010"+"B04100A3"+"AE000010"+"B0420005"+"AE000010"+"B0430019"+"AE000010"+\
"B0440014"+"AE000010"+"B0450028"+"AE000010"+"B0460021"+"AE000010"+"B0470035"+"AE000010"+\
"B0480038"+"AE000010"+"B049000C"+"AE000010"+"B04A0028"+"AE000010"+"B04B003A"+"AE000010"+\
"B04C02E1"+"AE000010"+"B04D0C28"+"AE000010"+"B04E0480"+"AE000010"+"B04F0AAA"+"AE000010";

cmd_a1="B10005AA"+"AE000010"+"B10205AA"+"AE000010"+"B10405AA"+"AE000010"+"B10605AA"+"AE000010"+\
"B10805AA"+"AE000010"+"B10A05AA"+"AE000010"+"B10C05AA"+"AE000010"+"B10E05AA"+"AE000010"+\
"B11005AA"+"AE000010"+"B11205AA"+"AE000010"+"B11405AA"+"AE000010"+"B11605AA"+"AE000010"+\
"B11805AA"+"AE000010"+"B11A05AA"+"AE000010"+"B11C05AA"+"AE000010"+"B11E05AA"+"AE000010"+\
"B10103D9"+"AE000010"+"B10303D9"+"AE000010"+"B10503D9"+"AE000010"+"B10703D9"+"AE000010"+\
"B10903D9"+"AE000010"+"B10B03D9"+"AE000010"+"B10D03D9"+"AE000010"+"B10F03D9"+"AE000010"+\
"B11103D9"+"AE000010"+"B11303D9"+"AE000010"+"B11503D9"+"AE000010"+"B11703D9"+"AE000010"+\
"B11903D9"+"AE000010"+"B11B03D9"+"AE000010"+"B11D03D9"+"AE000010"+"B11F03D9"+"AE000010"+\
"B1300514"+"AE000010"+"B1310000"+"AE000010"+"B1320A5A"+"AE000010"+"B133044C"+"AE000010"+\
"B13405DC"+"AE000010"+"B1350426"+"AE000010"+"B13604B9"+"AE000010"+"B1370000"+"AE000010"+\
"B1380480"+"AE000010"+"B1390000"+"AE000010"+"B13A08BB"+"AE000010"+"B13B0000"+"AE000010"+\
"B13D046A"+"AE000010"+"B13E044C"+"AE000010"+"B13F044C"+"AE000010"+"B140008F"+"AE000010"+\
"B14100A3"+"AE000010"+"B1420005"+"AE000010"+"B1430019"+"AE000010"+"B1440014"+"AE000010"+\
"B1450028"+"AE000010"+"B1460021"+"AE000010"+"B1470035"+"AE000010"+"B1480038"+"AE000010"+\
"B149000C"+"AE000010"+"B14A0028"+"AE000010"+"B14B003A"+"AE000010"+"B14C02E1"+"AE000010"+\
"B14D0C28"+"AE000010"+"B14E0480"+"AE000010"+"B14F0AAA"+"AE000010";

cmd_a2="B20005AA"+"AE000010"+\
"B20205AA"+"AE000010"+"B20405AA"+"AE000010"+"B20605AA"+"AE000010"+"B20805AA"+"AE000010"+\
"B20A05AA"+"AE000010"+"B20C05AA"+"AE000010"+"B20E05AA"+"AE000010"+"B21005AA"+"AE000010"+\
"B21205AA"+"AE000010"+"B21405AA"+"AE000010"+"B21605AA"+"AE000010"+"B21805AA"+"AE000010"+\
"B21A05AA"+"AE000010"+"B21C05AA"+"AE000010"+"B21E05AA"+"AE000010"+"B20103D9"+"AE000010"+\
"B20303D9"+"AE000010"+"B20503D9"+"AE000010"+"B20703D9"+"AE000010"+"B20903D9"+"AE000010"+\
"B20B03D9"+"AE000010"+"B20D03D9"+"AE000010"+"B20F03D9"+"AE000010"+"B21103D9"+"AE000010"+\
"B21303D9"+"AE000010"+"B21503D9"+"AE000010"+"B21703D9"+"AE000010"+"B21903D9"+"AE000010"+\
"B21B03D9"+"AE000010"+"B21D03D9"+"AE000010"+"B21F03D9"+"AE000010"+"B2300514"+"AE000010"+\
"B2310000"+"AE000010"+"B2320A5A"+"AE000010"+"B233044C"+"AE000010"+"B23405DC"+"AE000010"+\
"B2350426"+"AE000010"+"B23604B9"+"AE000010"+"B2370000"+"AE000010"+"B2380480"+"AE000010"+\
"B2390000"+"AE000010"+"B23A08BB"+"AE000010"+"B23B0000"+"AE000010"+"B23D046A"+"AE000010"+\
"B23E044C"+"AE000010"+"B23F044C"+"AE000010"+"B240008F"+"AE000010"+"B24100A3"+"AE000010"+\
"B2420005"+"AE000010"+"B2430019"+"AE000010"+"B2440014"+"AE000010"+"B2450028"+"AE000010"+\
"B2460021"+"AE000010"+"B2470035"+"AE000010"+"B2480038"+"AE000010"+"B249000C"+"AE000010"+\
"B24A0028"+"AE000010"+"B24B003A"+"AE000010"+"B24C02E1"+"AE000010"+"B24D0C28"+"AE000010"+\
"B24E0480"+"AE000010"+"B24F0AAA"+"AE000010";

cmd_a3="B30005AA"+"AE000010"+"B30205AA"+"AE000010"+\
"B30405AA"+"AE000010"+"B30605AA"+"AE000010"+"B30805AA"+"AE000010"+"B30A05AA"+"AE000010"+\
"B30C05AA"+"AE000010"+"B30E05AA"+"AE000010"+"B31005AA"+"AE000010"+"B31205AA"+"AE000010"+\
"B31405AA"+"AE000010"+"B31605AA"+"AE000010"+"B31805AA"+"AE000010"+"B31A05AA"+"AE000010"+\
"B31C05AA"+"AE000010"+"B31E05AA"+"AE000010"+"B30103D9"+"AE000010"+"B30303D9"+"AE000010"+\
"B30503D9"+"AE000010"+"B30703D9"+"AE000010"+"B30903D9"+"AE000010"+"B30B03D9"+"AE000010"+\
"B30D03D9"+"AE000010"+"B30F03D9"+"AE000010"+"B31103D9"+"AE000010"+"B31303D9"+"AE000010"+\
"B31503D9"+"AE000010"+"B31703D9"+"AE000010"+"B31903D9"+"AE000010"+"B31B03D9"+"AE000010"+\
"B31D03D9"+"AE000010"+"B31F03D9"+"AE000010"+"B3300514"+"AE000010"+"B3310000"+"AE000010"+\
"B3320A5A"+"AE000010"+"B333044C"+"AE000010"+"B33405DC"+"AE000010"+"B3350426"+"AE000010"+\
"B33604B9"+"AE000010"+"B3370000"+"AE000010"+"B3380480"+"AE000010"+"B3390000"+"AE000010"+\
"B33A08BB"+"AE000010"+"B33B0000"+"AE000010"+"B33D046A"+"AE000010"+"B33E044C"+"AE000010"+\
"B33F044C"+"AE000010"+"B340008F"+"AE000010"+"B34100A3"+"AE000010"+"B3420005"+"AE000010"+\
"B3430019"+"AE000010"+"B3440014"+"AE000010"+"B3450028"+"AE000010"+"B3460021"+"AE000010"+\
"B3470035"+"AE000010"+"B3480038"+"AE000010"+"B349000C"+"AE000010"+"B34A0028"+"AE000010"+\
"B34B003A"+"AE000010"+"B34C02E1"+"AE000010"+"B34D0C28"+"AE000010"+"B34E0480"+"AE000010"+\
"B34F0AAA"+"AE000010";

cmd_a4="B40005AA"+"AE000010"+"B40205AA"+"AE000010"+"B40405AA"+"AE000010"+\
"B40605AA"+"AE000010"+"B40805AA"+"AE000010"+"B40A05AA"+"AE000010"+"B40C05AA"+"AE000010"+\
"B40E05AA"+"AE000010"+"B41005AA"+"AE000010"+"B41205AA"+"AE000010"+"B41405AA"+"AE000010"+\
"B41605AA"+"AE000010"+"B41805AA"+"AE000010"+"B41A05AA"+"AE000010"+"B41C05AA"+"AE000010"+\
"B41E05AA"+"AE000010"+"B40103D9"+"AE000010"+"B40303D9"+"AE000010"+"B40503D9"+"AE000010"+\
"B40703D9"+"AE000010"+"B40903D9"+"AE000010"+"B40B03D9"+"AE000010"+"B40D03D9"+"AE000010"+\
"B40F03D9"+"AE000010"+"B41103D9"+"AE000010"+"B41303D9"+"AE000010"+"B41503D9"+"AE000010"+\
"B41703D9"+"AE000010"+"B41903D9"+"AE000010"+"B41B03D9"+"AE000010"+"B41D03D9"+"AE000010"+\
"B41F03D9"+"AE000010"+"B4300514"+"AE000010"+"B4310000"+"AE000010"+"B4320A5A"+"AE000010"+\
"B433044C"+"AE000010"+"B43405DC"+"AE000010"+"B4350426"+"AE000010"+"B43604B9"+"AE000010"+\
"B4370000"+"AE000010"+"B4380480"+"AE000010"+"B4390000"+"AE000010"+"B43A08BB"+"AE000010"+\
"B43B0000"+"AE000010"+"B43D046A"+"AE000010"+"B43E044C"+"AE000010"+"B43F044C"+"AE000010"+\
"B440008F"+"AE000010"+"B44100A3"+"AE000010"+"B4420005"+"AE000010"+"B4430019"+"AE000010"+\
"B4440014"+"AE000010"+"B4450028"+"AE000010"+"B4460021"+"AE000010"+"B4470035"+"AE000010"+\
"B4480038"+"AE000010"+"B449000C"+"AE000010"+"B44A0028"+"AE000010"+"B44B003A"+"AE000010"+\
"B44C02E1"+"AE000010"+"B44D0C28"+"AE000010"+"B44E0480"+"AE000010"+"B44F0AAA"+"AE000010";


cmd_a5="B50005AA"+"AE000010"+"B50205AA"+"AE000010"+"B50405AA"+"AE000010"+"B50605AA"+"AE000010"+\
"B50805AA"+"AE000010"+"B50A05AA"+"AE000010"+"B50C05AA"+"AE000010"+"B50E05AA"+"AE000010"+\
"B51005AA"+"AE000010"+"B51205AA"+"AE000010"+"B51405AA"+"AE000010"+"B51605AA"+"AE000010"+\
"B51805AA"+"AE000010"+"B51A05AA"+"AE000010"+"B51C05AA"+"AE000010"+"B51E05AA"+"AE000010"+\
"B50103D9"+"AE000010"+"B50303D9"+"AE000010"+"B50503D9"+"AE000010"+"B50703D9"+"AE000010"+\
"B50903D9"+"AE000010"+"B50B03D9"+"AE000010"+"B50D03D9"+"AE000010"+"B50F03D9"+"AE000010"+\
"B51103D9"+"AE000010"+"B51303D9"+"AE000010"+"B51503D9"+"AE000010"+"B51703D9"+"AE000010"+\
"B51903D9"+"AE000010"+"B51B03D9"+"AE000010"+"B51D03D9"+"AE000010"+"B51F03D9"+"AE000010"+\
"B5300514"+"AE000010"+"B5310000"+"AE000010"+"B5320A5A"+"AE000010"+"B533044C"+"AE000010"+\
"B53405DC"+"AE000010"+"B5350426"+"AE000010"+"B53604B9"+"AE000010"+"B5370000"+"AE000010"+\
"B5380480"+"AE000010"+"B5390000"+"AE000010"+"B53A08BB"+"AE000010"+"B53B0000"+"AE000010"+\
"B53D046A"+"AE000010"+"B53E044C"+"AE000010"+"B53F044C"+"AE000010"+"B540008F"+"AE000010"+\
"B54100A3"+"AE000010"+"B5420005"+"AE000010"+"B5430019"+"AE000010"+"B5440014"+"AE000010"+\
"B5450028"+"AE000010"+"B5460021"+"AE000010"+"B5470035"+"AE000010"+"B5480038"+"AE000010"+\
"B549000C"+"AE000010"+"B54A0028"+"AE000010"+"B54B003A"+"AE000010"+"B54C02E1"+"AE000010"+\
"B54D0C28"+"AE000010"+"B54E0480"+"AE000010"+"B54F0AAA"+"AE000010";

cmd_a6="B60005AA"+"AE000010"+\
"B60205AA"+"AE000010"+"B60405AA"+"AE000010"+"B60605AA"+"AE000010"+"B60805AA"+"AE000010"+\
"B60A05AA"+"AE000010"+"B60C05AA"+"AE000010"+"B60E05AA"+"AE000010"+"B61005AA"+"AE000010"+\
"B61205AA"+"AE000010"+"B61405AA"+"AE000010"+"B61605AA"+"AE000010"+"B61805AA"+"AE000010"+\
"B61A05AA"+"AE000010"+"B61C05AA"+"AE000010"+"B61E05AA"+"AE000010"+"B60103D9"+"AE000010"+\
"B60303D9"+"AE000010"+"B60503D9"+"AE000010"+"B60703D9"+"AE000010"+"B60903D9"+"AE000010"+\
"B60B03D9"+"AE000010"+"B60D03D9"+"AE000010"+"B60F03D9"+"AE000010"+"B61103D9"+"AE000010"+\
"B61303D9"+"AE000010"+"B61503D9"+"AE000010"+"B61703D9"+"AE000010"+"B61903D9"+"AE000010"+\
"B61B03D9"+"AE000010"+"B61D03D9"+"AE000010"+"B61F03D9"+"AE000010"+"B6300514"+"AE000010"+\
"B6310000"+"AE000010"+"B6320A5A"+"AE000010"+"B633044C"+"AE000010"+"B63405DC"+"AE000010"+\
"B6350426"+"AE000010"+"B63604B9"+"AE000010"+"B6370000"+"AE000010"+"B6380480"+"AE000010"+\
"B6390000"+"AE000010"+"B63A08BB"+"AE000010"+"B63B0000"+"AE000010"+"B63D046A"+"AE000010"+\
"B63E044C"+"AE000010"+"B63F044C"+"AE000010"+"B640008F"+"AE000010"+"B64100A3"+"AE000010"+\
"B6420005"+"AE000010"+"B6430019"+"AE000010"+"B6440014"+"AE000010"+"B6450028"+"AE000010"+\
"B6460021"+"AE000010"+"B6470035"+"AE000010"+"B6480038"+"AE000010"+"B649000C"+"AE000010"+\
"B64A0028"+"AE000010"+"B64B003A"+"AE000010"+"B64C02E1"+"AE000010"+"B64D0C28"+"AE000010"+\
"B64E0480"+"AE000010"+"B64F0AAA"+"AE000010";

cmd_a7="B70005AA"+"AE000010"+"B70205AA"+"AE000010"+\
"B70405AA"+"AE000010"+"B70605AA"+"AE000010"+"B70805AA"+"AE000010"+"B70A05AA"+"AE000010"+\
"B70C05AA"+"AE000010"+"B70E05AA"+"AE000010"+"B71005AA"+"AE000010"+"B71205AA"+"AE000010"+\
"B71405AA"+"AE000010"+"B71605AA"+"AE000010"+"B71805AA"+"AE000010"+"B71A05AA"+"AE000010"+\
"B71C05AA"+"AE000010"+"B71E05AA"+"AE000010"+"B70103D9"+"AE000010"+"B70303D9"+"AE000010"+\
"B70503D9"+"AE000010"+"B70703D9"+"AE000010"+"B70903D9"+"AE000010"+"B70B03D9"+"AE000010"+\
"B70D03D9"+"AE000010"+"B70F03D9"+"AE000010"+"B71103D9"+"AE000010"+"B71303D9"+"AE000010"+\
"B71503D9"+"AE000010"+"B71703D9"+"AE000010"+"B71903D9"+"AE000010"+"B71B03D9"+"AE000010"+\
"B71D03D9"+"AE000010"+"B71F03D9"+"AE000010"+"B7300514"+"AE000010"+"B7310000"+"AE000010"+\
"B7320A5A"+"AE000010"+"B733044C"+"AE000010"+"B73405DC"+"AE000010"+"B7350426"+"AE000010"+\
"B73604B9"+"AE000010"+"B7370000"+"AE000010"+"B7380480"+"AE000010"+"B7390000"+"AE000010"+\
"B73A08BB"+"AE000010"+"B73B0000"+"AE000010"+"B73D046A"+"AE000010"+"B73E044C"+"AE000010"+\
"B73F044C"+"AE000010"+"B740008F"+"AE000010"+"B74100A3"+"AE000010"+"B7420005"+"AE000010"+\
"B7430019"+"AE000010"+"B7440014"+"AE000010"+"B7450028"+"AE000010"+"B7460021"+"AE000010"+\
"B7470035"+"AE000010"+"B7480038"+"AE000010"+"B749000C"+"AE000010"+"B74A0028"+"AE000010"+\
"B74B003A"+"AE000010"+"B74C02E1"+"AE000010"+"B74D0C28"+"AE000010"+"B74E0480"+"AE000010"+\
"B74F0AAA"+"AE000010";

cmd_a8="B80005AA"+"AE000010"+"B80205AA"+"AE000010"+"B80405AA"+"AE000010"+\
"B80605AA"+"AE000010"+"B80805AA"+"AE000010"+"B80A05AA"+"AE000010"+"B80C05AA"+"AE000010"+\
"B80E05AA"+"AE000010"+"B81005AA"+"AE000010"+"B81205AA"+"AE000010"+"B81405AA"+"AE000010"+\
"B81605AA"+"AE000010"+"B81805AA"+"AE000010"+"B81A05AA"+"AE000010"+"B81C05AA"+"AE000010"+\
"B81E05AA"+"AE000010"+"B80103D9"+"AE000010"+"B80303D9"+"AE000010"+"B80503D9"+"AE000010"+\
"B80703D9"+"AE000010"+"B80903D9"+"AE000010"+"B80B03D9"+"AE000010"+"B80D03D9"+"AE000010"+\
"B80F03D9"+"AE000010"+"B81103D9"+"AE000010"+"B81303D9"+"AE000010"+"B81503D9"+"AE000010"+\
"B81703D9"+"AE000010"+"B81903D9"+"AE000010"+"B81B03D9"+"AE000010"+"B81D03D9"+"AE000010"+\
"B81F03D9"+"AE000010"+"B8300514"+"AE000010"+"B8310000"+"AE000010"+"B8320A5A"+"AE000010"+\
"B833044C"+"AE000010"+"B83405DC"+"AE000010"+"B8350426"+"AE000010"+"B83604B9"+"AE000010"+\
"B8370000"+"AE000010"+"B8380480"+"AE000010"+"B8390000"+"AE000010"+"B83A08BB"+"AE000010"+\
"B83B0000"+"AE000010"+"B83D046A"+"AE000010"+"B83E044C"+"AE000010"+"B83F044C"+"AE000010"+\
"B840008F"+"AE000010"+"B84100A3"+"AE000010"+"B8420005"+"AE000010"+"B8430019"+"AE000010"+\
"B8440014"+"AE000010"+"B8450028"+"AE000010"+"B8460021"+"AE000010"+"B8470035"+"AE000010"+\
"B8480038"+"AE000010"+"B849000C"+"AE000010"+"B84A0028"+"AE000010"+"B84B003A"+"AE000010"+\
"B84C02E1"+"AE000010"+"B84D0C28"+"AE000010"+"B84E0480"+"AE000010"+"B84F0AAA"+"AE000010";


cmd_a9="B90005AA"+"AE000010"+"B90205AA"+"AE000010"+"B90405AA"+"AE000010"+"B90605AA"+"AE000010"+\
"B90805AA"+"AE000010"+"B90A05AA"+"AE000010"+"B90C05AA"+"AE000010"+"B90E05AA"+"AE000010"+\
"B91005AA"+"AE000010"+"B91205AA"+"AE000010"+"B91405AA"+"AE000010"+"B91605AA"+"AE000010"+\
"B91805AA"+"AE000010"+"B91A05AA"+"AE000010"+"B91C05AA"+"AE000010"+"B91E05AA"+"AE000010"+\
"B90103D9"+"AE000010"+"B90303D9"+"AE000010"+"B90503D9"+"AE000010"+"B90703D9"+"AE000010"+\
"B90903D9"+"AE000010"+"B90B03D9"+"AE000010"+"B90D03D9"+"AE000010"+"B90F03D9"+"AE000010"+\
"B91103D9"+"AE000010"+"B91303D9"+"AE000010"+"B91503D9"+"AE000010"+"B91703D9"+"AE000010"+\
"B91903D9"+"AE000010"+"B91B03D9"+"AE000010"+"B91D03D9"+"AE000010"+"B91F03D9"+"AE000010"+\
"B9300514"+"AE000010"+"B9310000"+"AE000010"+"B9320A5A"+"AE000010"+"B933044C"+"AE000010"+\
"B93405DC"+"AE000010"+"B9350426"+"AE000010"+"B93604B9"+"AE000010"+"B9370000"+"AE000010"+\
"B9380480"+"AE000010"+"B9390000"+"AE000010"+"B93A08BB"+"AE000010"+"B93B0000"+"AE000010"+\
"B93D046A"+"AE000010"+"B93E044C"+"AE000010"+"B93F044C"+"AE000010"+"B940008F"+"AE000010"+\
"B94100A3"+"AE000010"+"B9420005"+"AE000010"+"B9430019"+"AE000010"+"B9440014"+"AE000010"+\
"B9450028"+"AE000010"+"B9460021"+"AE000010"+"B9470035"+"AE000010"+"B9480038"+"AE000010"+\
"B949000C"+"AE000010"+"B94A0028"+"AE000010"+"B94B003A"+"AE000010"+"B94C02E1"+"AE000010"+\
"B94D0C28"+"AE000010"+"B94E0480"+"AE000010"+"B94F0AAA"+"AE000010";


cmd_hvoff="C00000FFC00100FFC00200FFC00300FFC00400FFC00500FFC00600FFC00700FF"+\
"C00800FFC00900FFC00A00FFC00B00FFC00C00FFC00D00FFC00E00FFC00F00FF"+\
"C01000FFC01100FFC01200FFC01300FFC01400FFC01500FFC01600FFC01700FF"+\
"C01800FFC01900FFC01A00FFC01B00FFC01C00FFC01D00FFC01E00FFC01F00FF"+\
"C02000FFC02100FFC02200FFC02300FFC02400FFC02500FFC02600FFC02700FF"+\
"C02800FFC02900FFC02A00FFC02B00FFC02C00FFC02D00FFC02E00FFC02F00FF"+\
"C03000FFC03100FFC03200FFC03300FFC03400FFC03500FFC03600FFC03700FF"+\
"C03800FFC03900FFC03A00FFC03B00FFC03C00FFC03D00FFC03E00FFC03F00FF"+\
"C04000FFC04100FFC04200FFC04300FFC04400FFC04500FFC04600FFC04700FF"+\
"C04800FFC04900FFC04A00FFC04B00FFC04C00FFC04D00FFC04E00FFC04F00FF"+\
"C05000FFC05100FFC05200FFC05300FFC05400FFC05500FFC05600FFC05700FF"+\
"C05800FFC05900FFC05A00FFC05B00FFC05C00FFC05D00FFC05E00FFC05F00FF"+\
"C06000FFC06100FFC06200FFC06300FFC06400FFC06500FFC06600FFC06700FF"+\
"C06800FFC06900FFC06A00FFC06B00FFC06C00FFC06D00FFC06E00FFC06F00FF"+\
"C07000FFC07100FFC07200FFC07300FFC07400FFC07500FFC07600FFC07700FF"+\
"C07800FFC07900FFC07A00FFC07B00FFC07C00FFC07D00FFC07E00FFC07F00FF"+\
"C08000FFC08100FFC08200FFC08300FFC08400FFC08500FFC08600FFC08700FF"+\
"C08800FFC08900FFC08A00FFC08B00FFC08C00FFC08D00FFC08E00FFC08F00FF"+\
"C09000FFC09100FFC09200FFC09300FFC09400FFC09500FFC09600FFC09700FF"+\
"C09800FFC09900FFC09A00FFC09B00FFC09C00FFC09D00FFC09E00FFC09F00FF";

cmd_hvon="C0000000C0010000C0020000C0030000C0040000C0050000C0060000C0070000"+\
"C0080000C0090000C00A0000C00B0000C00C0000C00D0000C00E0000C00F0000"+\
"C0100000C0110000C0120000C0130000C0140000C0150000C0160000C0170000"+\
"C0180000C0190000C01A0000C01B0000C01C0000C01D0000C01E0000C01F0000"+\
"C0200000C0210000C0220000C0230000C0240000C0250000C0260000C0270000"+\
"C0280000C0290000C02A0000C02B0000C02C0000C02D0000C02E0000C02F0000"+\
"C0300000C0310000C0320000C0330000C0340000C0350000C0360000C0370000"+\
"C0380000C0390000C03A0000C03B0000C03C0000C03D0000C03E0000C03F0000"+\
"C0400000C0410000C0420000C0430000C0440000C0450000C0460000C0470000"+\
"C0480000C0490000C04A0000C04B0000C04C0000C04D0000C04E0000C04F0000"+\
"C0500000C0510000C0520000C0530000C0540000C0550000C0560000C0570000"+\
"C0580000C0590000C05A0000C05B0000C05C0000C05D0000C05E0000C05F0000"+\
"C0600000C0610000C0620000C0630000C0640000C0650000C0660000C0670000"+\
"C0680000C0690000C06A0000C06B0000C06C0000C06D0000C06E0000C06F0000"+\
"C0700000C0710000C0720000C0730000C0740000C0750000C0760000C0770000"+\
"C0780000C0790000C07A0000C07B0000C07C0000C07D0000C07E0000C07F0000"+\
"C0800000C0810000C0820000C0830000C0840000C0850000C0860000C0870000"+\
"C0880000C0890000C08A0000C08B0000C08C0000C08D0000C08E0000C08F0000"+\
"C0900000C0910000C0920000C0930000C0940000C0950000C0960000C0970000"+\
"C0980000C0990000C09A0000C09B0000C09C0000C09D0000C09E0000C09F0000";

cmd_post="01234567AE000100AF000000AE000100AF008000AE000100AE008000AE000100"+\
"AE000100AF00FFFFAE000100AE000100AF008000AE000100AF050080AE000100"+\
"AF060140AE000100AF140000AE000100AF1E0000AE000100AF1F0000AE000100AF320000AE000100"+\
"AF2C0000AE000100AF2D0001AE000100AF2D0000AE000100AF330100AE000100"+\
"AF340000AE000100AF350000AE000100AF360003AE000100AF370001AE000100"+\
"AF370000AE000100AF380000AE000100AF390004AE000100AF3A0000AE000100"+\
"AF4803FFAE000100AF3D0F00AE000100AF260000AE000100AF260800AE000100"+\
"AF260000AE000100AF261080AE000100AF25C000AE000100AF4B0000AE000100"+\
"AF4C0003AE000100AF270000AE000100AF0B8001AE000100AF0A0000AE000100"+\
"AF0A0001AE000100AF0A0000AE000100AF3E0000AE000100AF460000AE000100"+\
"AF470000AE000100AF470001AE000100AF470000AE000100AF460001AE000100"+\
"AF270000AE000100AF4D0450AE000100AF4DC450AE000100AF008D0EAE000100";

ctrl.send(syncwd+cmd_pre)
time.sleep(.1)
ctrl.send(syncwd+cmd_a0)
time.sleep(.3)
ctrl.send(syncwd+cmd_a1)
time.sleep(.3)
ctrl.send(syncwd+cmd_a2)
time.sleep(.3)
ctrl.send(syncwd+cmd_a3)
time.sleep(.3)
ctrl.send(syncwd+cmd_a4)
time.sleep(.3)
ctrl.send(syncwd+cmd_a5)
time.sleep(.3)
ctrl.send(syncwd+cmd_a6)
time.sleep(.3)
ctrl.send(syncwd+cmd_a7)
time.sleep(.3)
ctrl.send(syncwd+cmd_a8)
time.sleep(.3)
ctrl.send(syncwd+cmd_a9)
time.sleep(.3)
ctrl.send(syncwd+cmd_post)
time.sleep(.1)

ctrl.close()

