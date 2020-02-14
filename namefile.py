import pickle

namesfile_open=open("all_ppl_name","wb");
lis=['ashish','shashank','shreyank','karthik','nikhil']
pickle.dump(lis,namesfile_open)
namesfile_open.close()
