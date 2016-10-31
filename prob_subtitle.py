'''
This code will help when the subtitles are not in sync with the audio.
You have to judge by how much time is the subtitles getting delayed
and give the time as input in this program.
This code is only for .srt files.
'''

def chntime(string,add):

    st=list(string)
    hr= int(st[0]+st[1])
    min=int(st[3]+st[4])
    sec=int(st[6]+st[7])

    init= hr*3600 +min*60 + sec

    init+=add

    sec = init%60
    init=int(init/60)

    min = init%60
    init=int(init/60)

    hr = init

    st[0]=str(int(hr/10))
    st[1]=str(hr%10)
    st[3]=str(int(min/10))
    st[4]=str(min%10)
    st[6]=str(int(sec/10))
    st[7]=str(sec%10)

    string="".join(st)

    return string


fo=open('English.srt','r')#Give the location of the srt file.
data=fo.read()
fo.close()
datanew=data.split(sep='\n')
n= int(input("How may seconds do you want to add or subtract:"))

for i in range(len(datanew)):
    if datanew[i].isdigit():
        temp=datanew[i+1].split(sep=' ')
        temp[0]=chntime(temp[0],n)
        temp[2]=chntime(temp[2],n)
        datanew[i+1]=" ".join(temp)
    else :
        pass


data="\n".join(datanew)

fo=open('English.srt','w')#Give the location of the srt file that will be created.
fo.write(data)
fo.close()