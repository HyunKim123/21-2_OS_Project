import kivy
from kivy.app import App 
kivy.require('1.9.0')
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.spinner  import SpinnerOption
from kivy.uix.popup import Popup
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import get_feature
import get_region
import get_festival
import get_landmark
import get_landmark_info
import get_festival_info

fontName = './HMKMRHD.ttf'

class WindowManager(ScreenManager):
    pass

class MySpinnerOption(SpinnerOption):
    def __init__(self, **kwargs):
        self.font_name = fontName
        super(MySpinnerOption, self).__init__(**kwargs)

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
    
    values_dict = {'강원':['강릉시','고성군','동해시','삼척시','속초시','양구군','양양군','영월군','원주시','인제군','정선군','철원군','춘천시','태백시','평창군','홍천군','화천군','횡성군'],
    '경기':['가평군','고양시','과천시','광명시','광주시','구리시','군포시','김포시','남양주시','동두천시','부천시','성남시','수원시','시흥시','안산시','안성시','안양시','양주시','양평군','여주시','연천군','오산시','용인시','의왕시','의정부시','이천시','파주시','평택시','포천시','하남시','화성시'],
    '경남':['거제시','거창군','고성군','김해시','남해군','마산시','밀양시','사천시','산청군','양산시','의령군','진주시','진해시','창녕군','창원시','통영시','하동군','함안군','함양군','합천군'],
    '경북':['경산시','경주시','고령군','구미시','군위군','김천시','봉화군','상주시','성주군','안동시','영덕군','영양군','영주시','영천시','예천군','을릉도','을진군','의성군','청도군','청송군','칠곡군','포항시'],
    '광주':['광산구','남구','동구','북구','서구'],
    '대구':['남구','달서구','달성군','동구','북구','서구','수성구','중구'],
    '대전':['대덕구','동구','서구','유성구','중구'],
    '부산':['강서구','금정구','기장군','남구','동구','동래구','부산진구','북구','사상구','사하구','서구','수영구','연제구','영도구','중구','해운대구'],
    '서울':['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구'],
    '세종':['세종시'],
    '울산':['남구','동구','북구','울주군','중구'],
    '인천':['강화군','계양구','남동구','동구','미추홀구','부평구','서구','연수구','옹진군','중구'],
    '전남':['강진군','고흥군','곡성군','광양시','구례군','나주시','담양군','목포시','무안군','보성군','순천시','신안군','여수시','영광군','영암군','완도군','장성군','진도군','함평군','해남군','화순군'],
    '전북':['고창군','군산시','김제시','남원시','무주군','부안군','순창군','완주군','익산시','임실군','장수군','전주시','정읍시','진안군'],
    '제주도':['서귀포시','제주시'],
    '충남':['계룡시','공주시','금산군','논산시','당진시','보령시','부여군','서산시','서천군','아산시','연기군','예산군','천안시','청양군','태안군','홍성군'],
    '충북':['괴산군','단양군','보은군','영동군','옥천군','음성군','제천시','증편군','진천군','청주시','충주시']}
    
    sub_values = ListProperty()
    
    #지역 keyword가져오기 / DB에서 지역에 해당하는 main keyword값들 가져올 예정..
    def getKeyword(self):
        sm = self.manager
        maint = self.ids.main_drop.text
        subt = self.ids.sub_drop.text
        features = get_feature.get_f(maint + '_' + subt)

        for i in range(1,11):
            k = 'key' + str(i)
            sm.get_screen('result').ids[k].text = features[i-1]

    #지역을 모두 선택했는지 확인(안했을시 알림창 팝업)/ 선택한 지역에 해당하는 키워드를 DB로부터 가져옴
    def convert2r(self):
        sm = self.manager
        popup = Popup(title ='Alert!!', content=Label(text='지역을 선택해주세요!',font_name = fontName),
size_hint=(None, None), size=(600, 400))
        if self.ids.sub_drop.text =='시/군/구 선택' or self.ids.main_drop.text == self.ids.sub_drop.text:
            popup.open()
        else:
            self.getKeyword()
            sm.current = 'result'
    
    #종료
    def onExit(self):
        App.get_running_app().stop()

    #maindrop과 subdrop
    def values_update(self,text):
        self.sub_values = self.values_dict[text]
        if text != '시/군/구 선택' :
            self.ids.sub_drop.text = text
         
        
            

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        sm = self.manager    
        
    
    key_values=ListProperty()
    region = ListProperty()
    landmark = ListProperty()
    festival = ListProperty()

    popup = Popup(title ='Alert!!', content=Label(text='최소한 하나의 키워드를\n 선택해 주세요!',font_name = fontName),
size_hint=(None, None), size=(600, 400))

    #screen change
    def convert2m(self):
        sm = self.manager
        sm.get_screen('result').reset_all()
        sm.current = 'main'
        

    def convert2t(self,t):
        sm = self.manager
        sm.get_screen('third').ids.CityState2.text ='선택하신 여행지 ' + t + '(은)는 ...'
        sm.get_screen('third').ids.reg_temp.text = t
        landmark = get_landmark.get_lm(t)
        festival = get_festival.get_fstv(t)
        ## 여기다가 third화면에 있는 추천관광지와 축제에 뿌려주는 코드 작성
        
        for idx, val in enumerate(landmark):
            if idx > 4:
                break
            if val != None:
                cur = idx + 1
                t1 = 'tourrec' + str(cur)
                t2 = 'tourrecom' + str(cur)
                sm.get_screen('third').ids[t1].text = landmark[idx]
                sm.get_screen('third').ids[t1].disabled = False
                sm.get_screen('third').ids[t2].disabled = False

        for idx, val in enumerate(festival):
            if idx > 4:
                break
            if val != None:
                cur = idx + 1
                t1 = 'fesrec' + str(cur)
                t2 = 'fesrecom' + str(cur)
                sm.get_screen('third').ids[t1].text = festival[idx]
                sm.get_screen('third').ids[t1].disabled = False
                sm.get_screen('third').ids[t2].disabled = False
        sm.current = 'third'

    def get_keyval(self):
        sm = self.manager
        
        self.key_values.append(sm.get_screen('main').ids.main_drop.text + '_' + sm.get_screen('main').ids.sub_drop.text)

        for i in range(1, 11):
            chk = 'chk_key' + str(i)
            k = 'key' + str(i)
            if self.ids[chk].active:
                self.key_values.append(self.ids[k].text)

        if len(self.key_values)==1:
            self.key_values.clear()
            self.popup.open()
        else:
            Region = get_region.get_r(self.key_values)
            self.ids.recom.disabled = False
            for i in range(1,6):
                r = 'recom' + str(i)
                self.ids[r].text = Region[i-1]
            #추천지역에 값 할당해준후 배열 초기화
            Region.clear()
            self.key_values.clear()
        
    #result화면을 떠났을 때 키워드 제외 값 초기화
    def reset_all(self):
        self.ids.recom.disabled = True
        for i in range(1, 11):
            k = 'chk_key' + str(i)
            self.ids[k].active = False


class ThirdScreen(Screen):
    popup = Popup(title ='Alert!!', content=Label(text='죄송합니다 해당 지역에 대한 정보가 없네요',font_name = fontName),
size_hint=(None, None), size=(600, 400))

    def __init__(self, **kwargs):
        super(ThirdScreen, self).__init__(**kwargs)

    def convert2m(self):
        sm = self.manager
        sm.get_screen('result').reset_all()
        sm.current = 'main'

    def convert2r(self):
        sm = self.manager
        sm.current = 'result'

    def convert2if(self, region, text):

        sm = self.manager
        inf = get_festival_info.get_fstv_info(region, text)
        if type(inf[0]) == float and type(inf[1]) == float:
            self.popup.open()
        else :
            if type(inf[1]) != float:
                sm.get_screen('info').ids.location.text = '주소: ' + inf[1]
            if type(inf[0]) != float:
                cnt = 0
                le = len(inf[0])
                for i in range(le):
                    if inf[0][i] == " " and cnt > 20:
                        L = list(inf[0])
                        L[i] = "\n"
                        inf[0]=''.join(L)
                        cnt = 0
                    else:
                        cnt+=1
                sm.get_screen('info').ids.info.text = inf[0]  

            sm.get_screen('info').ids.choose.text = text
            sm.current = 'info'

    def convert2il(self, region, text):
        sm = self.manager
        inf = get_landmark_info.get_lm_info(region, text)
        if type(inf[0]) == float and type(inf[1]) == float:
            self.popup.open()
        else :
            if type(inf[1]) != float:
                sm.get_screen('info').ids.location.text = '주소: ' + inf[1]
            if type(inf[0]) != float:
                cnt = 0
                le = len(inf[0])
                for i in range(le):
                    if inf[0][i] == " " and cnt > 20:
                        L = list(inf[0])
                        L[i] = "\n"
                        inf[0]=''.join(L)
                        cnt = 0
                    else:
                        cnt+=1
                sm.get_screen('info').ids.info.text = inf[0]    
            sm.get_screen('info').ids.choose.text = text
            sm.current = 'info'
        

class InfoScreen(Screen):
    def __init__(self, **kwargs):
        super(InfoScreen, self).__init__(**kwargs)

    def convert2t(self):
        sm = self.manager
        self.ids.location.text = '주소 정보를 가져오지 못했어요'
        self.ids.info.text = '해당 지역/축제에 관한 정보를 가져오지 못했어요'
        sm.current = 'third'

class MainApp(App):
    def build(self):
        sm = WindowManager()
        sm.add_widget(MainScreen())
        sm.add_widget(ResultScreen())
        sm.add_widget(ThirdScreen())
        sm.add_widget(InfoScreen())
        return sm

if __name__ == '__main__':
    MainApp().run()