import subprocess
import sys
import os

BINDIFF_PATH = "C:\\Program Files\\zynamics\\BinDiff 4.2\\bin\\differ.exe"
IDAQ_PATH = "C:\\Program Files\\IDA 6.9\\idaq.exe"

if len(sys.argv) < 3:
	print "Usage: python diff_binaries.py $bin1 $bin2"
	sys.exit(1)

bindiff_script_path = os.getcwd() + os.sep + "bindiff_export.idc"

dir_path = os.getcwd() + os.sep

name_one = dir_path + sys.argv[1].split('.')[0]
name_two = dir_path + sys.argv[2].split('.')[0]


subprocess.call([IDAQ_PATH,"-B","-P+",sys.argv[1]])
subprocess.call([IDAQ_PATH,"-OExporterModule:" + name_one,"-S\"" + bindiff_script_path +"\"", name_one + ".idb"])
subprocess.call([IDAQ_PATH,"-B","-P+",sys.argv[2]])
subprocess.call([IDAQ_PATH,"-OExporterModule:" + name_two,"-S\"" + bindiff_script_path +"\"", name_two + ".idb"])

subprocess.call([BINDIFF_PATH,"-log_format", "--primary", name_one + ".BinExport", "--secondary", name_two + ".BinExport"])