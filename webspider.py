
import re
import requests
from bs4 import BeautifulSoup

filepath="E:/7.3/LoveStory/";

class Tool:
    removeImg = re.compile('<img.*?>| {7}|')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD= re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine,"\n",x)
        x = re.sub(self.replaceTD,"\t",x)
        x = re.sub(self.replacePara,"\n    ",x)
        x = re.sub(self.replaceBR,"\n",x)
        x = re.sub(self.removeExtraTag,"",x)
        return x.strip()

tool=Tool()




#url="http://www.mx-xz.com/sc-zl/qinggan/";
#url = "http://www.xiaogushi.com/Article/love/";
url = "http://www.59xihuan.cn/aiqing/";
htmlr=requests.get(url);

bsObjHtml=BeautifulSoup(htmlr.content,'html.parser',from_encoding='gb18030');
for pagelist in bsObjHtml.findAll("div",{"class":"page"}):
        for page in pagelist:
            urlpage=str(page);
            urlpage=urlpage[9:23]#cut 
            rpage=requests.get(url+urlpage);
            bsObjPage=BeautifulSoup(rpage.content,'html.parser',from_encoding='gb18030');
            print (urlpage);
            for titlelist in bsObjPage.findAll("div",{"class":"detail1"}):
                if (titlelist.a != None):
                    urltext=titlelist.a["href"];
                    filename=titlelist.a["title"];
                    print (urltext+" "+filename+" success!")
                    fp=open(filepath+filename+".txt","w",encoding="utf-8");

                    rtext=requests.get("http://www.59xihuan.cn"+urltext);
                    bsObjtext=BeautifulSoup(rtext.content,'html.parser',from_encoding='gb18030');

                    #filetext=bsObjtext.find("div",{"id":"sdcms_content"});
                    filetext=bsObjtext.find("div",{"class":"post"});
                    fp.write(tool.replace(filetext.__str__()));

                    fp.close();
           

            
