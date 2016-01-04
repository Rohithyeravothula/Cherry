import json
def write_personal_info(filename,name,version):
	info={}
	info["Name"]=name
	info["Version"]=version
	file_pointer=open(filename,'w')
	json.dump(info,file_pointer)
	file_pointer.close()


filename="../Information/Cherry_personal_info.txt"
name="Cherry"
version=1.0
write_personal_info(filename,name,version)



